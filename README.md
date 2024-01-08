# Habit Tracker

The Habit Tracker is a Python project designed to help users create and monitor their habits, providing a flexible framework for daily, weekly, and monthly tracking.

## Introduction

In our fast-paced lives, cultivating positive habits is essential for personal development and well-being. The Habit Tracker simplifies the process of habit formation by allowing users to define and track their habits over customizable time intervals.

## Features

- **Versatile Tracking:**
  - Create and track daily, weekly, and monthly habits.

- **Flexibility:**
  - Customize habits with varying frequencies, weekdays, and target days.

- **Streaks:**
  - Establish streaks for daily habits to foster consistency.

- **Detailed Monitoring:**
  - View completion dates and streak counts for each habit.

## Installation

Follow these steps to set up the Habit Tracker:

1. Clone the repository:

    ```bash
    git clone https://github.com/SJD999/habit_tracker_backend.git
    ```

2. Navigate to the project directory:

    ```bash
    cd habit-tracker
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:

    ```bash
    python3 main.py
    ```

2. Follow the prompts to create habits and track completion.

## Classes

### Habit

The base class representing a generic habit.

- **Attributes:**
  - `name`: Name of the habit.
  - `start_date`: Start date of the habit.
  - `completed_dates`: Set of dates when the habit was completed.

- **Methods:**
  - `mark_completed(completion_date)`: Marks the habit as completed on the specified date.
  - `mark_incomplete(completion_date)`: Marks the habit as incomplete on the specified date.

### DailyHabit

A subclass of `Habit` representing a habit to be completed daily.

- **Additional Attributes:**
  - `end_date`: End date for daily habits.
  - `streak_count`: Count of consecutive days the habit has been completed.

- **Additional Methods:**
  - `check_streak(target_streak)`: Checks if the habit has a streak equal to or greater than the specified target streak.
  - `get_streak_count()`: Returns the current streak count.

### WeeklyHabit

A subclass of `Habit` representing a habit to be completed weekly.

- **Additional Attributes:**
  - `weekdays`: List of weekdays on which the habit should be completed.

### MonthlyHabit

A subclass of `Habit` representing a habit to be completed monthly.

- **Additional Attributes:**
  - `target_days`: List of days in the month on which the habit should be completed.

## Documentation

For more detailed information, check out the docstring provided withh all fucntions 

## Contributing

If you want to contribute to this project, follow these steps:

1. Fork the project.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request.


## Examples

### Add and Track Habits

\`\`\`python
# Example of adding and tracking habits
add_and_track_habits()
\`\`\`

### Show Statistics

\`\`\`python
# Example of showing statistics
show_statistics()
\`\`\`

## Documentation

### Classes

#### 1. \`Habit\`

Base class for all types of habits.

- **Methods:**
  - \`mark_completed(completion_date=None)\`: Mark the habit as completed on a specific date.
  - \`mark_incomplete(completion_date)\`: Mark the habit as incomplete on a specific date.
  - \`calculate_end_date(start_date, frequency)\`: Calculate the end date based on the start date and frequency.
  - \`check_break_status()\`: Check if the habit is broken.

#### 2. \`DailyHabit\`

A class for daily habits.

- **Methods:**
  - \`mark_completed(completion_date=None)\`: Mark the habit as completed on a specific date.
  - \`check_streak(target_streak)\`: Check if the habit has a streak equal to or greater than the target.
  - \`get_streak_count()\`: Get the current streak count.

#### 3. \`WeeklyHabit\`

A class for weekly habits.

- **Methods:**
  - \`mark_completed(completion_date=None)\`: Mark the habit as completed on a specific date.
  - \`calculate_end_date(start_date, frequency)\`: Calculate the end date based on the start date and frequency.

#### 4. \`MonthlyHabit\`

A class for monthly habits.

- **Methods:**
  - \`mark_completed(completion_date=None)\`: Mark the habit as completed on a specific date.
  - \`calculate_end_date(start_date, frequency)\`: Calculate the end date based on the start date and frequency.

### Functions

#### 1. \`save_habits_to_json(habits, filename)\`

Save a list of habits to a JSON file.

#### 2. \`load_habits_from_json(filename)\`

Load habits from a JSON file.

#### 3. \`create_habit_df(habits)\`

Create a Pandas DataFrame from habits.

#### 4. \`visualize_completed_dates(habit_df)\`

Visualize completed dates using Matplotlib and Pandas.

#### 5. \`visualize_streak_count(daily_habits_df)\`

Visualize streak counts for daily habits using Matplotlib and Pandas.

#### 6. \`visualize_broken_status(habit_df)\`

Visualize broken status for each habit using Matplotlib and Pandas.

## Unit Test

We have included a simple unit test to verify the correct functionality of the `get_streak_count` method in the `DailyHabit` class. This test ensures that the streak count is updated appropriately when loading habits from a JSON file.

### How to Run the Unit Test

To run the unit test, follow these steps:

1. Ensure you have Python installed on your machine.

2. Open a terminal or command prompt.

3. Navigate to the directory containing your habit tracker script and the unit test script.

4. Run the following command:

    ```bash
    python -m unittest unit-test/unittest.py 
    ```


5. Check the output. If the test passes without any errors, you should see the message "Unit test passed successfully!".

### Important Note

The unit test uses a temporary JSON file for testing purposes. If the test passes, the temporary file is automatically removed. If you encounter any issues, make sure you have the necessary permissions to create and delete files in the specified directory.



---


