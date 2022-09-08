"""CSC110 Fall 2021 Assignment 3: Part 4 (Student Test Suite)

Instructions (READ THIS FIRST!)
===============================
Complete the unit tests in this file based on their docstring descriptions.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""
import pytest

from a3_part4 import load_data
from a3_ffwi_system import WeatherMetrics, FfwiOutput

import a3_ffwi_system as ffwi


class TestCalculateMr:
    """A collection of unit tests for calculate_mr."""

    def test_equation_3a_branch(self) -> None:
        """Test the branch calculate_mr that contains Equation 3a."""
        expected = 98.70101979
        actual = ffwi.calculate_mr(2.4, 51.0)
        assert pytest.approx(actual) == expected

    def test_equation_3b_branch(self) -> None:
        """Test the branch calculate_mr that contains Equation 3b."""
        expected = 179.9341986
        actual = ffwi.calculate_mr(2.4, 151.0)
        assert pytest.approx(actual) == expected


class TestCalculateM:
    """A collection of unit tests for calculate_m."""

    def test_no_mutation_mo_equals_ed(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo == ed."""
        some_weather_metric = WeatherMetrics(1, 1, 0.0, 0.0, 0.0, 0.0)
        previous_id = id(some_weather_metric)
        ffwi.calculate_m(some_weather_metric, 1.0, 1.0)
        assert previous_id == id(some_weather_metric)

    def test_no_mutation_mo_leq_ew(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo <= ew."""
        some_weather_metric = WeatherMetrics(1, 1, 0.0, 0.0, 0.0, 0.0)
        previous_id = id(some_weather_metric)
        ffwi.calculate_m(some_weather_metric, 1.0, 0.0)
        assert previous_id == id(some_weather_metric)

    def test_no_mutation_mo_greater_than_ew(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo > ew."""
        some_weather_metric = WeatherMetrics(1, 1, 0.0, 0.0, 0.0, 0.0)
        previous_id = id(some_weather_metric)
        ffwi.calculate_m(some_weather_metric, 101.0, 100.0)
        assert previous_id == id(some_weather_metric)

    def test_no_mutation_mo_greater_than_ed(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo > ed."""
        some_weather_metric = WeatherMetrics(1, 1, 0.0, 0.0, 0.0, 0.0)
        previous_id = id(some_weather_metric)
        ffwi.calculate_m(some_weather_metric, 0.0, 1.0)
        assert previous_id == id(some_weather_metric)


@pytest.fixture
def sample_data() -> tuple[list[WeatherMetrics], list[FfwiOutput]]:
    """A pytest fixture containing the data in data/ffwi/sample_data.csv

    NOTE: Do not change this function. Do not call this function directly. It is a pytest fixture,
    so pytest will call it automatically and pass it to test_ffmc_against_ground_truth below.
    """
    return load_data('data/ffwi/sample_data.csv')


def test_ffmc_against_ground_truth(sample_data) -> None:
    """Test the correctness of calculate_ffmc, calculate_dmc, calculate_dc, calculate_isi,
     calculate_bui, and calculate_fwi based on sample_data.

    Ensure that, for every WeatherMetric element in sample_data[0] passed to each of the calculate_
    functions mentioned above, the return value, rounded to the nearest decimal, matches the
    corresponding value from the FfwiOutput element in sample_data[1].

    Hints:
        - You will need to use the built-in function round.
        - You may want to use pytest.approx since you are comparing float values.
    """
    ffmc = ffwi.INITIAL_FFMC
    dmc = ffwi.INITIAL_DMC
    dc = ffwi.INITIAL_DC

    inputs, outputs = sample_data

    for i in range(0, len(inputs)):
        ffmc = ffwi.calculate_ffmc(inputs[i], ffmc)
        dmc = ffwi.calculate_dmc(inputs[i], dmc)
        dc = ffwi.calculate_dc(inputs[i], dc)
        isi = ffwi.calculate_isi(inputs[i], ffmc)
        bui = ffwi.calculate_bui(dmc, dc)
        fwi = ffwi.calculate_fwi(isi, bui)

        assert outputs[i].ffmc == round(ffmc, 1)
        assert outputs[i].dmc == round(dmc, 1)
        assert outputs[i].dc == round(dc, 1)
        assert outputs[i].isi == round(isi, 1)
        assert outputs[i].bui == round(bui, 1)
        assert outputs[i].fwi == round(fwi, 1)


# if __name__ == '__main__':
#     pytest.main(['a3_part4_tests.py'])
#
#     # When you are ready to check your work with python_ta, uncomment the following lines.
#     # (Delete the "#" and space before each line.)
#     # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
#     import python_ta
#     import python_ta.contracts
#     python_ta.contracts.DEBUG_CONTRACTS = False
#     python_ta.contracts.check_all_contracts()
#     python_ta.check_all(config={
#         'allowed-io': ['load_data'],
#         'extra-imports': ['a3_ffwi_system', 'a3_part4', 'pytest'],
#         'max-line-length': 100,
#         'max-args': 6,
#         'max-locals': 25,
#         'disable': ['R1705', 'R0201', 'C0103', 'W0621', 'E9970'],
#     })
