def is_valid_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()