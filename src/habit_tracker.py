"""
@brief Utility functions for saving and loading Habit objects to/from JSON.

@file habit_utils.py
"""

from datetime import datetime, timedelta
import json

from src.DailyHabit import DailyHabit
from src.WeeklyHabit import WeeklyHabit
from src.MonthlyHabit import MonthlyHabit


def save_habits_to_json(habits, filename):
    """
    @brief Save a list of habit objects to a JSON file.

    @param habits (list): List of Habit objects to be saved.
    @param filename (str): The name of the JSON file.

    @return None
    """
    habit_data = []
    for habit in habits:
        habit_data.append({
            'name': habit.name,
            'start_date': habit.start_date.isoformat(),
            'completed_dates': [date.isoformat() for date in habit.completed_dates],
            'broken': habit.broken,
            'streak_count': getattr(habit, 'streak_count', None)
        })

    with open(filename, 'w') as file:
        json.dump(habit_data, file)


def load_habits_from_json(filename):
    """
    @brief Load a list of habit objects from a JSON file.

    @param filename (str): The name of the JSON file.

    @return list: List of loaded Habit objects.
    """
    habits = []
    with open(filename, 'r') as file:
        habit_data = json.load(file)
        for data in habit_data:
            if data.get('weekdays'):
                habit = WeeklyHabit(data['name'], datetime.fromisoformat(data['start_date']), data['weekdays'])
            elif data.get('target_days'):
                habit = MonthlyHabit(data['name'], datetime.fromisoformat(data['start_date']), data['target_days'])
            else:
                habit = DailyHabit(data['name'], datetime.fromisoformat(data['start_date']))

            habit.completed_dates = {datetime.fromisoformat(date).date() for date in data['completed_dates']}
            habit.broken = data['broken']
            setattr(habit, 'streak_count', data.get('streak_count', 0))
            habits.append(habit)

    return habits
