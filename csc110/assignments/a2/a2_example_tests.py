"""CSC110 Fall 2021 Assignment 2, Part 3: Programming Tests

Instructions (READ THIS FIRST!)
===============================
This Python module contains example tests you can run for Part 3 of this assignment. Please note
that passing all these tests does NOT mean you have a 100% correct solution.

Some of the tests are empty, consider completing them. Also consider adding more of your own tests.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import pytest
import datetime

import a2_part3 as a2_courses
import a2_part4

###################################################################################################
# Sample Meeting Times
###################################################################################################
MON_9_TO_11 = ('Monday', datetime.time(9), datetime.time(11))
MON_12_TO_1 = ('Monday', datetime.time(12), datetime.time(13))

TUE_9_TO_11 = ('Tuesday', datetime.time(9), datetime.time(11))
TUE_10_TO_12 = ('Tuesday', datetime.time(10), datetime.time(12))

WED_9_TO_11 = ('Wednesday', datetime.time(9), datetime.time(11))
WED_12_TO_1 = ('Wednesday', datetime.time(12), datetime.time(13))

THU_3_TO_4 = ('Thursday', datetime.time(15), datetime.time(16))
THU_1_TO_2_30 = ('Thursday', datetime.time(13), datetime.time(14, 30))

FRI_9_TO_11 = ('Friday', datetime.time(9), datetime.time(11))
FRI_12_TO_1 = ('Friday', datetime.time(12), datetime.time(13))
FRI_1_TO_2 = ('Friday', datetime.time(13), datetime.time(14))

###################################################################################################
# Sample Sections
###################################################################################################
MAT137_LEC0101 = ('LEC0101', 'Y', (MON_9_TO_11, TUE_9_TO_11, WED_9_TO_11))
MAT137_LEC0201 = ('LEC0201', 'Y', (MON_12_TO_1, WED_12_TO_1, FRI_12_TO_1))

CSC110_LEC0101 = ('LEC0101', 'F', (MON_9_TO_11, TUE_9_TO_11, WED_9_TO_11))
CSC111_LEC0301 = ('LEC0301', 'S', (MON_9_TO_11, TUE_9_TO_11, FRI_1_TO_2))

CON123_LEC0123 = ('LEC0123', 'F', (FRI_1_TO_2,))
CON123_LEC0321 = ('LEC0321', 'S', (TUE_10_TO_12, FRI_1_TO_2))

CON333_LEC1337 = ('LEC1337', 'F', (WED_9_TO_11,))
CON333_LEC2001 = ('LEC2001', 'F', (MON_9_TO_11,))

STA130_LEC0101 = ('LEC0101', 'F', (THU_3_TO_4,))
STA130_LEC0201 = ('LEC0201', 'F', (THU_1_TO_2_30,))

###################################################################################################
# Sample Courses
###################################################################################################
CSC110 = ('CSC110', 'Foundations of Computer Science I', {CSC110_LEC0101})
CSC111 = ('CSC111', 'Foundations of Computer Science II', {CSC111_LEC0301})

CON123 = ('CON123', 'Foundation Construction', {CON123_LEC0123, CON123_LEC0321})
CON333 = ('CON333', 'Advanced Brick Laying', {CON333_LEC1337, CON333_LEC2001})

MAT137 = ('MAT137', 'Calculus!', {MAT137_LEC0101, MAT137_LEC0201})

STA130 = ('STA130', 'Introduction to Statistical Reasoning',
          {STA130_LEC0101, STA130_LEC0201})

###################################################################################################
# Sample Schedule
###################################################################################################
SCHEDULE_1 = {
    'CSC110': CSC110_LEC0101,
    'CSC111': CSC111_LEC0301
}

SCHEDULE_2 = {
    'CON123': CON123_LEC0123,
    'CSC111': CSC111_LEC0301,
    'CON333': CON333_LEC1337
}

SCHEDULE_3 = {
    'CSC110': CSC110_LEC0101,
    'CSC111': CSC111_LEC0301,
    'MAT137': MAT137_LEC0201,
    'CON123': CON123_LEC0321
}

# Note that this is SCHEDULE_1 but with CON123 added
SCHEDULE_4 = {
    'CSC110': CSC110_LEC0101,
    'CSC111': CSC111_LEC0301,
    'CON123': CON123_LEC0123
}

###################################################################################################
# Sample Raw Data
###################################################################################################
WED_9_TO_11_RAW = {'day': 'Wednesday', 'startTime': '09:00', 'endTime': '11:00'}
MON_9_TO_11_RAW = {'day': 'Monday', 'startTime': '09:00', 'endTime': '11:00'}
CON333_LEC1337_RAW = {'sectionCode': 'LEC1337', 'term': 'F', 'meetingTimes': [WED_9_TO_11_RAW]}
CON333_LEC2001_RAW = {'sectionCode': 'LEC2001', 'term': 'F', 'meetingTimes': [MON_9_TO_11_RAW]}
CON333_RAW = {'courseCode': 'CON333', 'courseTitle': 'Advanced Brick Laying',
              'sections': [CON333_LEC1337_RAW, CON333_LEC2001_RAW]}


###################################################################################################
# Part 3 Question 1
###################################################################################################
def test_num_sections() -> None:
    """
    Test num_sections with 1 section from CSC110
    """
    assert a2_courses.num_sections(CSC110) == 1


def test_num_lecture_hours() -> None:
    """
    Test num_lecture_hours with MAT137
    """
    assert a2_courses.num_lecture_hours(MAT137_LEC0101) == 6


# TODO: Create more tests

###################################################################################################
# Part 3 Question 2
###################################################################################################
def test_times_conflict() -> None:
    """
        Test times_conflict with conflicting meetings times that overlap
    """
    m1 = TUE_9_TO_11
    m2 = TUE_10_TO_12
    expected = True
    actual = a2_courses.times_conflict(m1, m2)
    assert actual == expected


def test_times_no_conflict() -> None:
    """
    Test times_conflict with non-conflicting meetings times
    """
    # TODO: Create a test


def test_sections_conflict() -> None:
    """
    Test sections_conflict with conflicting sections
    """
    # TODO: Create a test


def test_sections_no_conflict() -> None:
    """
    Test sections_conflict with non-conflicting sections
    """
    s1 = CON123_LEC0123
    s2 = CON123_LEC0321
    expected = False
    actual = a2_courses.sections_conflict(s1, s2)
    assert actual == expected


def test_is_valid() -> None:
    """
    Test is_valid with valid schedule
    """
    # TODO: Create a test


def test_not_valid() -> None:
    """
    Test is_valid with invalid schedule
    """
    # TODO: Create a test


def test_2_possible_schedule_combinations() -> None:
    """
    Test possible_schedule_combinations with 2 possible combinations
    """
    c1 = MAT137
    c2 = CSC111
    expected = 2
    actual = a2_courses.possible_schedules(c1, c2)
    assert len(actual) == expected


def test_4_possible_schedule_combinations() -> None:
    """
    Test possible_schedule_combinations with 4 possible combinations
    """
    # TODO: Create a test


def test_1_valid_schedule_combinations() -> None:
    """
    Test valid_schedule_combinations with valid schedule combination, bounds of 1
    """
    c1 = MAT137
    c2 = CSC111
    expected = 1
    actual = a2_courses.valid_schedules(c1, c2)
    assert len(actual) == expected


def test_4_valid_schedule_combinations() -> None:
    """
    Test valid_schedule_combinations with 4 valid schedule combinations
    """
    # TODO: Create a test


def test_possible_five_course_schedules() -> None:
    """
    Test possible_five_course_schedules with five possible course schedules
    """
    c1 = CSC110
    c2 = CSC111
    c3 = CON123
    c4 = CON333
    c5 = MAT137
    expected = 8
    actual = a2_courses.possible_five_course_schedules(c1, c2, c3, c4, c5)
    assert len(actual) == expected


def test_invalid_five_course_schedules() -> None:
    """
    Test valid_five_course_schedules with invalid five course schedule
    """
    # TODO: Create a test


# TODO: Create more tests

###################################################################################################
# Part 3 Question 3
###################################################################################################
def test_section_compatible() -> None:
    """
    Test is_section_compatible with compatible sections
    """
    # TODO: Create a test


def test_section_not_compatible() -> None:
    """
    Test is_section_compatible with incompatible sections
    """
    # TODO: Create a test


def test_course_compatible() -> None:
    """
    Test is_course_compatible with compatible course
    """
    # TODO: Create a test


def test_course_not_compatible() -> None:
    """
    Test is_course_compatible with incompatible course
    """
    # TODO: Create a test


def test_compatible_sections() -> None:
    """
    Test compatible_sections with compatible sections
    """
    actual = a2_courses.compatible_sections(SCHEDULE_1, CON123) == {CON123_LEC0123}
    expected = True
    assert actual == expected


# TODO: Create more tests

###################################################################################################
# Part 4
###################################################################################################
def test_transform_course_data() -> None:
    """
    Test transform_course_data
    """
    expected = CON333
    actual = a2_part4.transform_course_data(CON333_RAW)
    assert actual == expected


def test_transform_section_data() -> None:
    """
    Test transform_section_data
    """
    expected = CON333_LEC2001
    actual = a2_part4.transform_section_data(CON333_LEC2001_RAW)
    assert actual == expected


def test_transform_meeting_time_data() -> None:
    """
    Test transform_meeting_time_data
    """
    expected = MON_9_TO_11
    actual = a2_part4.transform_meeting_time_data(MON_9_TO_11_RAW)
    assert actual == expected


# TODO: Create more tests

if __name__ == "__main__":
    pytest.main(['a2_example_tests.py'])
