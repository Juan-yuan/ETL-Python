def check_null(data):
    if not data:
        return True
    data = data.lower()
    if data == "none" or data == "" or data == "null" or data == "undefined":
        return True
    return False