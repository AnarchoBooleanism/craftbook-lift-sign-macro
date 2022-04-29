# Main program.

from sign_generator import generate_sign
from get_input import get_bool_input, get_int_input
import keyboard

HOTKEY = "F4"

while __name__ == "__main__":
    print("Welcome to the CraftBook Lift Sign Macro program!")

    floor_count = get_int_input( # Get various arguments
        prompt_text="Enter a number of floors",
        is_legal=(lambda x: x > 0),
        error_message="Not a legal integer (above 0)"
    )
    has_basement = get_bool_input(prompt_text="Enter whether to include the basement as a floor", default=False)
    has_rooftop = get_bool_input(prompt_text="Enter whether to include the rooftop as a floor", default=False)

    print(f"To write a sign, press \"{HOTKEY}\".")

    for text in generate_sign(floor_count, has_basement, has_rooftop): # Get generator, and iterate over each list
        keyboard.wait(HOTKEY) # Wait for hotkey, then type text and escape
        print(f"Writing \"{text[0]}\" - \"{text[1]}\"...")
        for line in text:
            keyboard.write(line)
            keyboard.send("enter")
        keyboard.send("esc")

    if not get_bool_input(prompt_text="Would you like to create another elevator?"): # Confirm whether to loop again
        break
