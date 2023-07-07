def add_time(start_time, duration, start_day=None):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))

    total_minutes = start_hour * 60 + start_minute
    total_minutes += duration_hour * 60 + duration_minute

    new_hour = total_minutes // 60 % 12
    new_minute = total_minutes % 60
    new_period = period

    if total_minutes // 720 == 1:
        new_period = "PM" if period == "AM" else "AM"

    days_passed = total_minutes // 1440

    if start_day:
        start_day = start_day.lower().capitalize()
        new_day_index = (days_of_week.index(start_day) + days_passed) % 7
        new_day = days_of_week[new_day_index]

    new_time = f"{new_hour or 12}:{str(new_minute).zfill(2)} {new_period}"

    if start_day:
        if days_passed == 1:
            new_time += f", {new_day} (next day)"
        elif days_passed > 1:
            new_time += f", {new_day} ({days_passed} days later)"
        else:
            new_time += f", {new_day}"
    else:
        if days_passed == 1:
            new_time += " (next day)"
        elif days_passed > 1:
            new_time += f" ({days_passed} days later)"

    return new_time
