#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

""" This module contains all the code relating to SCALE tallies """


class Tally:
    """Each SCALE tally is represented by a Tally object."""
    def __init__(self, data):
        self.tally_number = data[0].split()[3][:-1]
        self.type = f"{data[0].split()[1]} {data[0].split()[2]}"
        try:
            self.title = data[0].split('.')[1]
        except IndexError:
            self.title = None
        self.particle = data[0].split()[0]
        self.response = float(data[6].split()[2])
        if self.response:
            self.rel_uncertainty = float(data[6].split()[4])
        else:
            self.rel_uncertainty = 0.0
        statistical_checks = data[6][69:80].split()
        self.passes = 0
        for check in statistical_checks:
            if check == 'X':
                self.passes += 1
        self.checks = {}
        for check, result in enumerate(statistical_checks, start=1):
            self.checks[check] = ('Pass' if result == 'X' else 'Fail')


    def scale_results(self, scaling_factor):
        """Scale the results of each tally by the project-level scaling factor

        Args:
            scaling_factor (float): A number to multiply results by
            """
        self.response *= scaling_factor
