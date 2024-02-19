# WHEN SHOULD I USE INHERITANCE?
Inheritance is a powerful tool, but it is a really bad idea to try to overuse it. Inheritance should only be used when every instance of the child class can also be considered the same type as the parent class.

When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance probably is not the best answer. In that case, you would probably just want to share some functions, or maybe make a new parent class that both classes inherit from.

 `ALL CATS ARE ANIMALS BUT NOT ALL ANIMALS ARE CATS`