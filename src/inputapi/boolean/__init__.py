from ..otherFunc.clearScreen import auto as clearScreen
from ..strings import sameLineStr


def yesNo(
    request: str = "",
    allowNumeric: bool = True,
    clearOnLoad: bool = False,
    clearWhenDone: bool = False,
) -> bool:
    """yesNo asks a Yes or No question

    For Boolean input you ask a request and get a Boolean representing the users response while repeating if the user gives an invalid response

    Args:
        request (str): The question to be written in the terminal for the user to answer. Defaults to empty string.
        allowNumeric (bool, optional): Allows the user to input a number along with the Y/n (Great for programs with a lot of numeric inputs). Defaults to True.
        clearOnLoad (bool, optional): Clears the terminal when running the function. Defaults to False.
        clearWhenDone (bool, optional): When the user gives the input it will clear the terminal. Defaults to False.

    Returns:
        response: True means the user said Yes, False for No
    """

    if clearOnLoad:
        clearScreen()

    if str != "":
        print(request)

    allowedInput = ["y", "n"]
    if allowNumeric:
        print("Numeric response allowed (Y=1, n=2)")
        allowedInput.append("1")
        allowedInput.append("2")

    query = sameLineStr("[Y/n]:", 1, 1, allowedInput)

    print()

    if clearWhenDone:
        clearScreen()

    return query.lower() in {"y", "1"}


__all__ = ["yesNo"]
