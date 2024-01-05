from datetime import datetime, timedelta

class Habit:
    """
    Represents a generic habit that users can track and mark as completed.

    Parameters:
    - name (str): The name of the habit.
    - start_date (datetime): The start date of the habit.

    Attributes:
    - name (str): The name of the habit.
    - start_date (datetime): The start date of the habit.
    - completed_dates (set): A set containing dates on which the habit was completed.
    - broken (bool): A flag indicating whether the habit has been broken.

    Methods:
    - mark_completed(completion_date=None): Marks the habit as completed for the specified date.
    - mark_incomplete(completion_date): Marks the habit as incomplete for the specified date.
    - calculate_end_date(start_date, frequency): Calculates the end date of the habit based on the start date and frequency.
    - check_break_status(): Checks if the habit has been broken based on completion status.

    Raises:
    - ValueError: If the completion date is outside the habit period.
    - NotImplementedError: Subclasses must implement the calculate_end_date method.
    """

    def __init__(self, name, start_date):
        """
        Initializes a Habit object.

        Parameters:
        - name (str): The name of the habit.
        - start_date (datetime): The start date of the habit.
        """
        self.name = name
        self.start_date = start_date
        self.completed_dates = set()
        self.broken = False

    def mark_completed(self, completion_date=None):
        """
        Marks the habit as completed for the specified date.

        Parameters:
        - completion_date (datetime): The date on which the habit is completed. Defaults to the current date.

        Raises:
        - ValueError: If the completion date is outside the habit period.
        """
        if completion_date is None:
            completion_date = datetime.now()

        if self.start_date <= completion_date:
            self.completed_dates.add(completion_date.date())
            self.broken = False  # Reset broken status when the habit is completed
        else:
            raise ValueError("Completion date is outside the habit period.")

    def mark_incomplete(self, completion_date):
        """
        Marks the habit as incomplete for the specified date.

        Parameters:
        - completion_date (datetime): The date on which the habit is marked incomplete.
        """
        self.completed_dates.discard(completion_date.date())

    def calculate_end_date(self, start_date, frequency):
        """
        Calculates the end date of the habit based on the start date and frequency.

        Parameters:
        - start_date (datetime): The start date of the habit.
        - frequency (int): The frequency of the habit.

        Raises:
        - NotImplementedError: Subclasses must implement the calculate_end_date method.
        """
        raise NotImplementedError("Subclasses must implement the calculate_end_date method.")

    def check_break_status(self):
        """
        Checks if the habit has been broken based on completion status.

        Returns:
        bool: True if the habit is broken (not completed at all), False otherwise.
        """
        if not self.completed_dates:
            self.broken = True
        return self.broken
