from datetime import datetime


def current_time_info(request):
    now = datetime.now()
    days = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "НД"]
    time_str = f"{days[now.weekday()]} {now.strftime('%H:%M')}"
    return {
        'display_time': time_str
    }