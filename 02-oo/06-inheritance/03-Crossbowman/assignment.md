# INHERITANCE HIERARCHY
There is no limit to how deeply we can nest an inheritance tree. For example, a `Cat` can inherit from an `Animal` that inherits from `LivingThing`. That said, we should always be careful that each time we inherit from a base class the child is a strict subset of the parent. You should never think to yourself "my child's class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

## ASSIGNMENT
The game designers have decided to add a new unit to the game: `Crossbowman`. A crossbowman is always an archer, but not all archers are crossbowmen. Crossbowmen have several arrows, but they have an additional method: `triple_shot()`.

1. Add a `use_arrows(self, num)` method to the `Archer` class. It should remove `num` arrows. If there aren't enough arrows to remove, it should raise a `not enough arrows` exception.
2. The `Crossbowman` class's constructor should call its parent's constructor.
3. The crossbowman's `triple_shot` method should use `3` arrows.
4. The crossbowman's `triple_shot` method takes a `target` as a parameter and returns `{} was shot by 3 crossbow bolts` where `{}` is the name of the `Human` that was shot.