# ARCHERS

## ASSIGNMENT
Complete the Archer class.

## CONSTRUCTOR
The constructor should take and set as properties the following parameters in order:

- `name`
- `health`
- `num_arrows`

## GET_SHOT METHOD
Finish the method called `get_shot` that doesn't take any parameters.

If the current archer has health left, remove one health from the current archer. Then, if the archer's health is `0`, raise ValueError: `{} is dead` where `{}` is the archer's name.

## SHOOT METHOD
Finish the method called `shoot` that takes an `Archer` instance as the `target` input.

If the shooter has no arrows left, raise ValueError `{} can't shoot` where `{}` is the shooter's name. Otherwise, remove an arrow from the shooter and print {1} shoots `{2}` where `{1}` is the shooter's name and `{2}` is the name of the targeted archer. Next, call the target's `get_shot()` method.