import datetime
def solution_station2(date_str):
    # Parse the date string into a datetime object
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    # Get the day of the week (0 = Monday, 6 = Sunday)
    day_of_week = date_obj.strftime('%A')
    # Dictionary to map English day names to Japanese
    solution_station2 = {
        'Monday': '月曜日',
        'Tuesday': '火曜日',
        'Wednesday': '水曜日',
        'Thursday': '木曜日',
        'Friday': '金曜日',
        'Saturday': '土曜日',
        'Sunday': '日曜日'
    }
    # Return the Japanese day name
    return solution_station2[day_of_week]