def add_time(start, duration, day=None):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    next_day = False
    # getting hour, minute and am/pm
    start_t = start.split()
    h_m = start_t[0].split(":")
    hour, minute = int(h_m[0]), int(h_m[1])
    am_pm = start_t[1]
    if am_pm == "PM":
        hour += 12

    # duration hours, minutes
    d = duration.split(":")
    add_hour, add_minute = int(d[0]), int(d[1])

    # adding time
    total_h = hour + add_hour
    total_m = minute + add_minute

    # formatting
    # minutes
    m = total_m % 60
    if m < 10:
        m = "0" + str(m)

    # hours
    h = total_h % 24
    add_h = total_m // 60
    h += add_h

    # days
    d = (total_h + add_h) // 24
    if d == 1:
        next_day = "(next day)"
    if d > 1:
        next_day = f"({d} days later)"

    # day name

    if h == 24:
        final_time = str(h - 12) + ":" + str(m) + " AM"
    elif h > 12:
        final_time = str(h - 12) + ":" + str(m) + " PM"
    elif h == 12:
        final_time = str(h) + ":" + str(m) + " PM"
    else:
        final_time = str(h) + ":" + str(m) + " AM"

    if next_day and not day:
        final_time += " " + next_day
    if day and not next_day:
        d_name = day.capitalize()
        day_index = days.index(d_name)
        new_index = (day_index + d) % 7
        final_day = days[new_index]
        final_time += ", " + final_day

    if next_day and day:
        d_name = day.capitalize()
        day_index = days.index(d_name)
        new_index = (day_index + d) % 7
        final_day = days[new_index]
        final_time += ", " + final_day + " " + next_day

    return final_time


print(add_time("11:59 PM", "24:05"))
