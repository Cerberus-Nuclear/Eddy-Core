![logo](https://cerberusnuclear.com/wp-content/uploads/2020/10/EddyLinkedin.jpg)


[![PyPI version](https://badge.fury.io/py/eddy-mc-core.svg)](https://badge.fury.io/py/eddy-mc-core)

Eddy is an HTML output generator for MCNP and SCALE, it imports an MCNP or SCALE output file, extracts the important 
data, and writes it to a user-friendly HTML file.

This repository contains the core source code version of Eddy. It is intended to be accessed via PIP and used as a 
python module. 
A stand-alone version of Eddy is also available [here](https://github.com/Cerberus-Nuclear/Eddy-Wrapper) (it has this 
package as one of its requirements), and Eddy is also available 
as [a pre-compiled executable](https://github.com/Cerberus-Nuclear/Eddy).

This package is available on the PyPI Python Package index as eddy-mc-core, in order to allow easier integration 
into other programs. It can be installed using pip:

```bash
pip install eddy-mc-core
```

and accessed using:

```python
from eddymc_core import eddy
eddy.main()
```

where `eddy.main()` has one non-optional argument; the filepath for the MCNP output, and one optional argument; a scaling factor to multiply any tally results by.
Features include:
- Eddy can convert F2, F4, F5, F5a, F6 and F6+ tallies
- Eddy can accept average tallies, given in the form `F4:N (4 5)`
- Eddy can take an MCNP criticality output and show k-effective for the 
first half, second half and total calculation.
- Eddy will present a warning if an MCNP case was halted due to lost particles
- Eddy will clearly present any FATAL ERROR messages in the MCNP output
- Eddy currently **does not** accept multi-particle tallies of the form `F4:N,P`
- For F2, F4 and F5 tallies, the units are presented as microSieverts per hour.
  The actual result from MCNP is typically multiplied by some conversion factor, so the
  tally output could be in any unit. The uSv/h units have been left in for now as this
  seems to be by far the most common conversion factor used for shielding calculations. 

Requirements

- Python 3.6 or later
- Jinja2 Python package is required (will be included automatically if Eddy is installed via pip)
- importlib_resources may be required for versions of python < 3.9
- pytest and pytest-mock Python packages are required to run the unit tests

<details>
  <summary>Example HTML outputs</summary>
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/eddy-screen-shot-2.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Summary-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Stats-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/WarningsComments.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/particles-1.jpg" name="image-name">
</details>
