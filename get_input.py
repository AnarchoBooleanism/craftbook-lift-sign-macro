# Various functions for getting valid inputs.

class InputError(Exception):
    """Exception class for the input functions."""
    pass

def get_value_input(prompt_text:str="Input", convert:callable=(lambda x: x), default=None, is_legal:callable=(lambda x: True), error_message:str="Not a legal value"):
    """
    Get input for a certain value, while checking if it is a valid value.
    Used by other input functions.

    Parameters:
        prompt_text (str): Text to use as prompt (default: "Input").
        convert (callable): Function that converts input into a valid object.
        default: Default value to use. (default: None)
        is_legal (callable): Function for checking the input.
        error_message (str): Error message to use. (default: "Not a legal value")
    Returns:
        value: Object created from user input.
    """

    assert type(prompt_text) is str, "get_value_input: prompt_text must be str"
    assert callable(convert), "get_value_input: convert must be callable"
    assert callable(is_legal), "get_value_input: is_legal must be callable"
    assert type(error_message) is str, "get_value_input: error_message must be str"

    full_prompt_text = "".join([ # Prompt text as one string
        prompt_text,
        f" (default: \"{default}\")" if default is not None else "",
        ": "
    ])

    while True:
        try:
            user_input = input(full_prompt_text)
            
            if user_input == "" and default is not None: # Default for blank strings
                converted_user_input = default
            elif user_input == "":
                raise InputError("No default value, cannot be blank")
            else:
                converted_user_input = convert(user_input) # Convert input into object

            if not is_legal(converted_user_input): # Check if not legal
                raise InputError(error_message)
            
            return converted_user_input # If everything works, then return
        except InputError as e: # For other issues
            print(f"Error, invalid input: {e}")
            print("Please try again.")
        except ValueError: # For conversion issues
            print("Error, invalid input: Could not process/convert input")
            print("Please try again.")

def get_int_input(prompt_text:str="Input an integer value", default:int=None, is_legal:callable=(lambda x: True), error_message:str="Not a legal integer"):
    """
    Get input for an integer, while checking if it is a valid value.

    Parameters:
        prompt_text (str): Text to use as prompt (default: "Input an integer value").
        default (int): Default value to use. (default: None)
        is_legal (callable): Function for checking the input.
        error_message (str): Error message to use. (default: "Not a legal integer")
    Returns:
        value: Object created from user input.
    """
    return get_value_input( # Use existing function, but with extras related to integers
        prompt_text=prompt_text,
        convert=(lambda x: int(x)),
        default=default,
        is_legal=is_legal,
        error_message=error_message
    )

def get_bool_input(prompt_text:str="Input a Boolean value", default:bool=True, is_legal:callable=(lambda x: True), error_message:str="Not a legal Boolean"):
    """
    Get input for an boolean, while checking if it is a valid value.
    True if a variation of "True", else False.

    Parameters:
        prompt_text (str): Text to use as prompt (default: "Input a Boolean value").
        default (bool): Default value to use. (default: True)
        is_legal (callable): Function for checking the input.
        error_message (str): Error message to use. (default: "Not a legal Boolean")
    Returns:
        value: Object created from user input.
    """
    return get_value_input( # Use existing function, but with extras related to Booleans
        prompt_text=prompt_text,
        convert=(lambda x: True if x in ["True", "true", "T", "t"] else False),
        default=default,
        is_legal=is_legal,
        error_message=error_message
    )
