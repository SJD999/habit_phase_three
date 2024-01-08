"""
@brief Represents a monthly habit that users can track and mark as completed.

@file MonthlyHabit.py
"""

from src.Habit import *

class MonthlyHabit(Habit):
    """
    @brief Represents a monthly habit that users can track and mark as completed.

    @param name (str): The name of the habit.
    @param start_date (datetime): The start date of the habit.
    @param target_days (list): List of days in the month when the habit should be completed.

    @details
    Attributes:
    - target_days (list): List of days in the month when the habit should be completed.

    Inherits from:
    - Habit

    Methods:
    - mark_completed(completion_date=None): Marks the habit as completed for the specified date.
    - calculate_end_date(start_date, frequency): Calculates the end date of the habit based on the start date and frequency.
    """

    def __init__(self, name, start_date, target_days):
        """
        @brief Initializes a MonthlyHabit object.

        @param name (str): The name of the habit.
        @param start_date (datetime): The start date of the habit.
        @param target_days (list): List of days in the month when the habit should be completed.
        """
        super().__init__(name, start_date)
        self.target_days = target_days
        next_month = start_date.replace(day=28) + timedelta(days=4)
        self.end_date = (next_month.replace(day=1) - timedelta(days=1)).replace(hour=23, minute=59, second=59)

    def mark_completed(self, completion_date=None):
        """
        @brief Marks the monthly habit as completed for the specified date.

        @param completion_date (datetime): The date on which the habit is completed. Defaults to the current date.

        @throws ValueError: If the completion date is not on a specified day.
        """
        if completion_date is None:
            completion_date = datetime.now()
        if completion_date.day in self.target_days:
            super().mark_completed(completion_date)
        else:
            raise ValueError("Completion date is not on a specified day.")

    def calculate_end_date(self, start_date, frequency):
        """
        @brief Calculates the end date of the monthly habit based on the start date and frequency.

        @param start_date (datetime): The start date of the habit.
        @param frequency (int): The frequency of the habit.

        @return datetime: The calculated end date of the habit.
        """
        next_month = start_date.replace(day=28) + timedelta(days=4)
        return (next_month.replace(day=1) - timedelta(days=1)).replace(hour=23, minute=59, second=59)
