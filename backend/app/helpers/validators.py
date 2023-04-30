def check_string_not_empty(cls, value) -> str:
    assert value != "", "Empty strings are not allowed."
    return value
