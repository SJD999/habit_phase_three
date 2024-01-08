"""
@brief Represents a weekly habit that users can track and mark as completed.

@file WeeklyHabit.py
"""

from src.Habit import *

class WeeklyHabit(Habit):
    """
    @brief Represents a weekly habit that users can track and mark as completed.

    @param name (str): The name of the habit.
    @param start_date (datetime): The start date of the habit.
    @param weekdays (list): List of weekdays when the habit should be completed (0 for Monday, 1 for Tuesday, ..., 6 for Sunday).

    @details
    Attributes:
    - weekdays (list): List of weekdays when the habit should be completed.

    Inherits from:
    - Habit

    Methods:
    - mark_completed(completion_date=None): Marks the habit as completed for the specified date.
    - calculate_end_date(start_date, frequency): Calculates the end date of the habit based on the start date and frequency.
    """

    def __init__(self, name, start_date, weekdays):
        """
        @brief Initializes a WeeklyHabit object.

        @param name (str): The name of the habit.
        @param start_date (datetime): The start date of the habit.
        @param weekdays (list): List of weekdays when the habit should be completed (0 for Monday, 1 for Tuesday, ..., 6 for Sunday).
        """
        super().__init__(name, start_date)
        self.weekdays = weekdays
        self.end_date = start_date + timedelta(weeks=1)

    def mark_completed(self, completion_date=None):
        """
        @brief Marks the weekly habit as completed for the specified date.

        @param completion_date (datetime): The date on which the habit is completed. Defaults to the current date.

        @throws ValueError: If the completion date is not on a specified weekday.
        """
        if completion_date is None:
            completion_date = datetime.now()
        if completion_date.weekday() in self.weekdays:
            super().mark_completed(completion_date)
        else:
            raise ValueError("Completion date is not on a specified weekday.")

    def calculate_end_date(self, start_date, frequency):
        """
        @brief Calculates the end date of the weekly habit based on the start date and frequency.

        @param start_date (datetime): The start date of the habit.
        @param frequency (int): The frequency of the habit.

        @return datetime: The calculated end date of the habit.
        """
        return start_date + timedelta(weeks=frequency)
