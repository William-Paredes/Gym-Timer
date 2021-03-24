from datetime import datetime


def current_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    return current_time