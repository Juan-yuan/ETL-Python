import time

def ts10_to_date_str(ts, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.localtime(ts)
    return time.strftime(format_string, time_array)

def ts13_to_date_str(ts, format_string="%Y-%m-%d %H:%M:%S"):
    ts10 = int(ts / 1000)
    return ts10_to_date_str(ts10, format_string)
