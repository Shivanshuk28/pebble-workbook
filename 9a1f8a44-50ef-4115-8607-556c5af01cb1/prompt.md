```py
from typing import List

def traitDecider(fathers_trait,mothers_trait):
    """
    Calculate inherited traits for children based on the number of capital letters in parent trait values

    The trait with more capital letters is considered dominant and will be passed to the child.
    If both parents have the same number of capital letters for a trait, then fathers trait is selected.

    Args:
        fathers_trait (dict): Fathers traits dictionary containing traits and their values
        mothers_trait (dict): Mothers traits dictionary containing traits and their values

    Returns:
        dict : Dictionary containing the inherites traits for the child

    Examples:
        fathers_trait={"hair_color":"Blue","eye_color":"BlAck"}
        mothers_trait={"hair_color":"BlACk","eye_color":"bRoWN"}
        result=traitDecider(fathers_trait,mothers_trait)
        #Returns: {"hair_color":"BlAck","eye_color":"bRoWN"}

    Raises:
        ExceptionType: description
    """
    pass
```
