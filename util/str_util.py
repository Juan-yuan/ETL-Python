def check_null(data):
    if not data:
        return True
    data = data.lower()
    if data == "none" or data == "" or data == "null" or data == "undefined":
        return True
    return False


def check_str_null_and_transform_to_sql_null(data):
    if check_null(data):
        return "NULL"
    else:
        return f"'{data}'"


def check_number_null_and_transform_to_sql_null(data):
    if data and not check_null(str(data)):
        return data
    else:
        return "NULL"
