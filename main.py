# Main program.

from sign_generator import generate_sign
from get_input import get_bool_input, get_int_input
import keyboard

while __name__ == "__main__":
    floor_count = get_int_input( # Get various arguments
        prompt_text="Enter a number of floors",
        is_legal=(lambda x: x > 0),
        error_message="Not a legal integer (above 0)"
    )
    has_basement = get_bool_input(prompt_text="Enter whether to include the basement as a floor", default=False)
    has_rooftop = get_bool_input(prompt_text="Enter whether to include the rooftop as a floor", default=False)

    if not get_bool_input(prompt_text="Would you like to create another elevator?"): # Confirm whether to loop again
        break
