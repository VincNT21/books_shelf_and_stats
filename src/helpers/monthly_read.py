from helpers.date_utils import convert_str_to_date, get_monthly_range

def get_books_monthly_read(user_data_library, month:int, year:int):
    start_monthly, end_monthly = get_monthly_range(month, year)
    monthly_list_id = []
    for item in user_data_library.library:
        if item["is_read"] == False:
            continue
        parsed_date = convert_str_to_date(item["end_date"])
        if parsed_date >= start_monthly and parsed_date < end_monthly:
            monthly_list_id.append(item["id"])
    return monthly_list_id

def get_books_yearly_read(user_data_library, year:int):
    yearly_list_id = []
    for item in user_data_library.library:
        if item["is_read"] == False:
            continue
        parsed_date = convert_str_to_date(item["end_date"])
        if parsed_date.year == year:
            yearly_list_id.append(item["id"])
    return yearly_list_id
