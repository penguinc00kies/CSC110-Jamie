"""CSC110 Fall 2021 Assignment 3, Part 4: Forest Fires (SOLUTIONS)

Instructions (READ THIS FIRST!)
===============================
Implement each of the functions in this file. As usual, do not change any function headers
or preconditions. You do NOT need to add doctests.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""
import csv
import plotly.graph_objects as go

from a3_ffwi_system import WeatherMetrics, FfwiOutput
import a3_ffwi_system as ffwi


def load_data(filename: str) -> tuple[list[WeatherMetrics], list[FfwiOutput]]:
    """Return a tuple of two parallel lists based on the data in filename. The first list contains
    WeatherMetrics. The second list contains the corresponding FfwiOutput.

    The data in filename is in a csv format with 12 columns. The first six columns correspond to
    the month, day, temperature, relative humidity, wind speed, and precipitation, in that order.
    The last six columns correspond to the FFMC, DMC, DC, ISI, BUI, and FWI values that would be
    calculated based on the first six columns and the previous day's values.
    """
    # ACCUMULATOR inputs_so_far: The WeatherMetrics parsed from filename so far
    inputs_so_far = []
    # ACCUMULATOR outputs_so_far: The FfwiOutputs parsed from filename so far
    outputs_so_far = []

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            assert len(row) == 12, 'Expected every row to contain 12 elements.'
            # row is a list of strings
            # Your task is to extract the relevant data from row and add it
            # to the accumulator.

    return inputs_so_far, outputs_so_far


def calculate_ffwi_outputs(readings: list[WeatherMetrics]) -> dict[tuple[int, int], FfwiOutput]:
    """Return a dictionary mapping (month, day) tuples to their corresponding FfwiOutput based on
    the daily weather measurements found in readings.

    Use the functions in a3_ffwi_system for initial FFMC, DMC, and DC values and to calculate each
    attribute needed for FfwiOutput.

    Preconditions:
        - Every reading in readings has a unique (month, day) pair
    """


def get_xy_data(outputs: dict[tuple[int, int], FfwiOutput], attribute: str) -> \
        tuple[list[str], list[float]]:
    """Return a tuple of two parallel lists. The first list contains the keys of outputs as
    strings in the format 'month, day'. The second list contains the corresponding value of
    the attribute of FfwiOutput.

    You can access an attribute from a data class using the getattr built-in function. For example,
        >>> output = FfwiOutput(2.0, 3.0, 4.0, 5.0, 6.0, 7.0)
        >>> getattr(output, 'ffmc')
        2.0
    """


def plot_ffwi_attribute(outputs: dict[tuple[int, int], FfwiOutput], attribute: str) -> None:
    """Plot an attribute from FfwiOutput as a time series.

    Preconditions:
        - attribute in {'ffmc', 'dmc', 'dc', 'isi', 'bui', 'fwi'}
        - outputs != {}
    """
    # Convert the outputs into parallel x and y lists
    x_data, y_data = get_xy_data(outputs, attribute)

    # Create the figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, name=attribute))

    # Configure the figure
    fig.update_layout(title=f'Time Series of {attribute}',
                      xaxis_title='(Month, Day)',
                      yaxis_title=f'Calculated {attribute}')

    # Show the figure in the browser
    fig.show()
    # Is the above not working for you? Comment it out, and uncomment the following:
    # fig.write_html('my_figure.html')
    # You will need to manually open the my_figure.html file created above.


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # python_ta.check_all(config={
    #     'allowed-io': ['load_data'],
    #     'extra-imports': ['python_ta.contracts', 'csv', 'plotly.graph_objects', 'a3_ffwi_system'],
    #     'max-line-length': 100,
    #     'max-args': 6,
    #     'max-locals': 25,
    #     'disable': ['R1705'],
    # })
