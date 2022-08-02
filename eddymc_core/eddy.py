#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""Eddy is a programme to convert the text-based output files from MCNP and SCALE to
a user-friendly HTML format.

Copyright (C) 2020  Cerberus Nuclear Ltd

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


This module is the entry point for Eddy, the MCNP and SCALE to HTML output converter.
This script takes an output file and scaling factor, determines whether it is an MCNP or SCALE case,
determines whether it is a criticality or shielding case
and creates the relevant EddyMCNPCase or EddySCALECase object,
then calls the relevant HTML writer
"""

# Imports from standard library
import re
import os.path
from markupsafe import escape
# Local imports
from .scale import scale_html_writer
from .scale.eddy_scale_case import EddySCALECase
from .mcnp import mcnp_html_writer
from .mcnp.eddy_mcnp_case import EddyMCNPCase


class NotAcceptedFileTypeError(Exception):
    """Raised when the file selected is not recognised as a SCALE or MCNP output"""


def main(filename, scaling_factor=1):
    """Entry point to Eddy. Requires filename, optional scaling factor as arguments.
    Gets the output data and determines whether it is a crit case.
    Determine whether it is an MCNP or SCALE case;
    calls the relevant converter.

    Args:
        filename (str): the file path (including the name) of the output file
        scaling_factor (float): A number by which any tally results will be multiplied
    """

    # check file exists
    assert os.path.isfile(filename), "That output file does not exist in that location."

    # Check MCNP or SCALE, criticality or shielding case, get output data
    output_data, code, crit_case = get_args(filename)

    if code == 'SCALE':
        case = EddySCALECase(
            filepath=filename,
            file=output_data,
            scaling_factor=scaling_factor,
        )
        html = scale_html_writer.get_html(case)
    elif code == 'MCNP':
        case = EddyMCNPCase(
            filepath=filename,
            scaling_factor=scaling_factor,
            file=output_data,
            crit_case=crit_case,
        )
        html = mcnp_html_writer.get_html(case)
    else:
        raise NotAcceptedFileTypeError("This file doesn't seem to be an MCNP or SCALE output?")

    output_file, extension = os.path.splitext(filename)
    output_file += '.html'
    write_output(output_file, html)
    print(f"Eddy run complete, {output_file} created.\n")


def get_args(filename):
    """
    Determine if this is a crit case (for MCNP).
    Determine if this is a SCALE CASE
    Read in the output data from the mcnp output file.

    Args:
        filename (str): the file path (including the name) of the output file

    Returns:
        output_data (list): The contents of the output file
        crit_case (bool): True if kcode case, otherwise False
        code (str): 'SCALE' or 'MCNP'
    """

    # get contents of file
    output_data = read_file(filename)

    if 'SCALE' in output_data[2]:
        code = 'SCALE'
        print("Case identified as SCALE output.")
    elif 'Code Name &amp; Version = MCNP' in output_data[0] or '1mcnp     version' in output_data[0]:
        code = 'MCNP'
        print("Case identified as MCNP output.")
    else:
        raise NotAcceptedFileTypeError("This file doesn't seem to be an MCNP or SCALE output?")

    # Check if shielding or crit case
    if code == 'MCNP':
        crit_case = check_if_crit(output_data)
        if crit_case:
            print("MCNP case identified as criticality calculation.")
        else:
            print("MCNP case identified as shielding calculation.")

    else:
        crit_case = False

    return output_data, code, crit_case


def read_file(filename):
    """Read in the output file.

    Args:
        filename (str): The name (and location) of the .out file

    Returns:
        data (list): The lines from the output file
    """
    with open(filename, 'r') as file:
        data = file.readlines()
    data = sanitize_list(data)
    return data


def sanitize_list(text):
    """Replace any html control characters in any string in the
    list with the appropriate html codes to stop
    them from being interpreted as html tags.

    Args:
        text [list]: a list of strings

    Returns:
        list: The sanitized version of the list
    """
    sanitized_text = []
    for line in text:
        line = str(escape(line))
        sanitized_text.append(line)
    return sanitized_text


def check_if_crit(output_data):
    """Read through output data to check if case is crit or shielding

    Args:
        output_data (list): The text of the output file

    Returns:
        True if kcode found or False if not.

    """
    PATTERN_crit = re.compile(r"\s+\d+-\s{7}(kcode).*")
    for line in output_data:
        if re.match(PATTERN_crit, line):
            return True
    return False


def write_output(file, html):
    """Write the HTML to the desired file

    Args:
        file (str): The filepath of the html file to be written
        html (str): The contents to be written to the html file
    """
    with open(file, 'w') as f:
        f.write(html)


