from datetime import datetime, timedelta
from src.statistics_1 import *
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

def add_and_track_habits():
    """
    Function to demonstrate adding and tracking habits.

    The function creates instances of DailyHabit, WeeklyHabit, and MonthlyHabit,
    checks off some habits, and demonstrates using various methods.

    Example:
    - To check off a habit:
      brushteath_daily.mark_completed(habit_start_date + timedelta(days=1))
      brushteath_daily.mark_completed(habit_start_date + timedelta(days=2))
      Exercise_weekly.mark_completed(datetime(2024, 1, 15))

    - To check the break status of a habit:
      print(read_weekly.check_break_status())

    - To check the streak with a specific target:
      print(brushteath_daily.check_streak(target_streak=5))

    - To get the number of the streak count:
      print(brushteath_daily.get_streak_count())

    - Save habits to JSON file:
      save_habits_to_json([brushteath_daily, cleaningroom_daily, Exercise_weekly, read_weekly, skills_monthly, visiting_firends_Monthly], 'habits.json')
    """
    habit_start_date = datetime(2023, 11, 1)  

    brushteath_daily = DailyHabit('Brush Teath Daily', habit_start_date)
    cleaningroom_daily = DailyHabit('Cleaning room  Daily', habit_start_date)

    Exercise_weekly = WeeklyHabit('Exercise Weekly', habit_start_date, weekdays=[0, 2])
    read_weekly = WeeklyHabit('Read Weekly', habit_start_date, weekdays=[0, 2])

    skills_monthly= MonthlyHabit('Skills  Monthly', habit_start_date, target_days=[1, 15])
    visiting_firends_Monthly = MonthlyHabit('visiting firends Monthly', habit_start_date, target_days=[1, 15])

    
    # To check off a habit : 
    brushteath_daily.mark_completed(habit_start_date + timedelta(days=1)) 
    brushteath_daily.mark_completed(habit_start_date + timedelta(days=2)) 
    Exercise_weekly.mark_completed(datetime(2024, 1, 15))

    # To check a break status of a habit : 
    print(read_weekly.check_break_status())   

    # To check streak with a specific target : 
    print(brushteath_daily.check_streak(target_streak=5)) 

    # To get the number of the streak count : 
    print(brushteath_daily.get_streak_count())

    # Save habits to JSON file
    save_habits_to_json([brushteath_daily, cleaningroom_daily, Exercise_weekly, read_weekly, skills_monthly, visiting_firends_Monthly], 'habits.json')


def show_statistics():
    """
    Function to demonstrate habit statistics.

    The function loads habits from a JSON file, showcases different statistics,
    and visualizes completed dates, streak count, and broken status using Pandas and Matplotlib.

    Example:
    - to check the longest habit streak:
      print(longest_habit_streak(habits))

    - to check the current daily habits:
      print(current_daily_habits(habits))
    
    - to check habits struggled last month:
      habits_struggled_last_month(habits)
    
    - to check all tracked habits:
      print(all_tracked_habits(habits))

    - to check habits with the same periodicity (Enter DailyHabit, MonthlyHabit, or WeeklyHabit):
      print(habits_same_periodicity(habits , DailyHabit))

    - to visualize completed dates:
      visualize_completed_dates(habit_df)

    - to visualize streak count for daily habits:
      visualize_streak_count(daily_habits_df)

    - to visualize broken status:
      visualize_broken_status(habit_df)
    """
    # Load habits
    habits = load_habits_from_json('habits.json')

    # to check the longest habit streak 
    print(longest_habit_streak(habits))

    # to check the current daily habits 
    print(current_daily_habits(habits))
    

    
    # to chech the all tracked habits 
    print(all_tracked_habits(habits))

    # to check the habit with same period enter DailyHabit or MonthlyHabit or WeeklyHabit
    print(habits_same_periodicity(habits , DailyHabit))


    # Create DataFrame
    habit_df = create_habit_df(habits)

    # Visualize completed dates
    visualize_completed_dates(habit_df)

    # Visualize streak count for daily habits
    daily_habits_df = habit_df[habit_df['Type'] == 'DailyHabit']
    visualize_streak_count(daily_habits_df)

    # Visualize broken status : 
    visualize_broken_status(habit_df)

if __name__ == "__main__":

    """if you want to add habit and track them uncomment below """
    #add_and_track_habits()
    """if you want to show statics also uncomment below uncomment below """
    show_statistics()
