from datetime import date, datetime

def convert_str_to_date(date_as_str):
    if date_as_str == None:
        return None
    return datetime.strptime(date_as_str, "%Y-%m-%d").date()

def convert_date_to_str(date):
    if date == None:
        return None
    return date.strftime("%Y-%m-%d")

def date_validation_and_format(date_to_val):
        if date_to_val == None:
            return None
        try:
            parsed_date = convert_str_to_date(date_to_val)
        except:
            raise ValueError("Date given not in a good format 'YYYY-mm-dd' or with incorrect values")
        if parsed_date > date.today():
            raise ValueError("The date given is in the future!")
        if parsed_date < date(2020, 1, 1):
            raise ValueError("The date given seems too far in the past (before 2020)")
        return convert_date_to_str(parsed_date)

def get_monthly_range(month:int, year:int):
    start_of_monthly_range = date(year, month, 1)
    if month == 12:
        end_of_monthly_range = date(year + 1, 1, 1)
    else:
        end_of_monthly_range = date(year, month + 1, 1)
    return start_of_monthly_range, end_of_monthly_range

def calc_duration(start_date, end_date):
        start_date = convert_str_to_date(start_date)
        end_date = convert_str_to_date(end_date)
        if start_date > end_date:
            raise ValueError("End date cannot be before start date")
        else:
            duration = end_date - start_date
            duration = duration.days
            return duration