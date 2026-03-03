import datetime

def get_time_information() -> str:
    now = datetime.datetime.now()
    return (
        f"Current Real-time Information:\n"
        f"Day: {now.strftime('%A')}\n" #tuesday
        f"Date: {now.strftime('%d')}\n" #03
        f"Month: {now.strftime('%B')}\n" #march
        f"Year: {now.strftime('%Y')}\n" #2026
        f"Time: {now. strftime('%H')} hours, {now.strftime('%M')} minutes, {now.strftime('%S')} seconds\n")
#this will return few lines of texts - day nmae, date, month, year, time(24h-format)