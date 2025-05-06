def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Formats a string by applying an optional prefix, suffix, capitalization, and maximum length.

    Parameters
    """
    # validation of input types
    if not isinstance(text, str):
        raise TypeError("Parameter 'text' must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("Parameter 'prefix' must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("Parameter 'suffix' must be a string.")
    if not isinstance(capitalize, bool):
        raise TypeError("Parameter 'capitalize' must be a boolean.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("Parameter 'max_length' must be an integer or None.")
        if max_length < 0:
            raise ValueError("Parameter 'max_length' must be non-negative.")

    # Applying a transformations
    if capitalize:
        text = text.capitalize()

    result = f"{prefix}{text}{suffix}"

    if max_length is not None:
        result = result[:max_length]

    return result
