# Generator for sign text.

def get_floor_number(num:int) -> str:
    """
    Returns the floor number for a given integer.
    Examples: Ground, 2nd, 3rd, 4th, etc.
    
    Parameters:
        num (int): Integer to analyze.
    Returns:
        floor_number (str): String representation of floor for the given integer.
    """
    assert type(num) is int, "get_ordinal_indicator: num must be an int"
    assert num > 0, "get_ordinal_indicator: num must be a positive integer (starting from 1)"

    if num == 1: # If ground floor (floor 1)
        return "Ground"

    match ending := num % 10: # Special cases
        case 1:
            return f"{num}st"
        case 2:
            return f"{num}nd"
        case 3:
            return f"{num}rd"

    return f"{num}th" # If not returned already, return "-th"

def generate_sign(count:int, has_basement:bool=False, has_rooftop:bool=False) -> list[str]:
    """
    Generator function for sign text. Returns a list of strings, representing lines.

    Parameters:
        count (int): Number of floors to create signs for, in between the basement and rooftop floors.
        has_basement (bool): Whether to include a basement floor in the signs. (default: False)
        has_rooftop (bool): Whether to include a rooftop in the signs. (default: False)
    """
    assert type(has_basement) is bool, f"generate_sign: has_basement must be a bool"
    assert type(has_rooftop) is bool, f"generate_sign: has_rooftop must be a bool"

    if has_basement: # Yield for basement
        yield ["Basement", "[Lift Up]"]
    
    for floor in range(1, count + 1): # Yield per floor
        floor_text = f"{get_floor_number(floor)} Floor"
        
        if has_basement or floor != 1: # If not bottom floor or basement
            yield [floor_text, "[Lift Down]"]
        if has_rooftop or floor != count: # If not rooftop or top floor
            yield [floor_text, "[Lift Up]"]
    
    if has_rooftop: # Yield for rooftop
        yield ["Rooftop", "[Lift Down]"]


if __name__ == "__main__":
    # For testing

    count = int(input("Number of floors: "))
    has_basement = bool(input("Include basement (blank if not): "))
    has_rooftop = bool(input("Include rooftop (blank if not): "))
    generator = generate_sign(count, has_basement=has_basement, has_rooftop=has_rooftop)

    while True:
        print(next(generator))