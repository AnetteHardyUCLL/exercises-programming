# Task

Create a class `Account`.

* It should have a publically accessible attribute `login`.
* It should have a private attribute `password`.
* Both these attributes must be initialized by constructor parameters.
* Provide a method `is_correct_password(self, pw)` that checks if `pw` is equal to the password.

## Important

We have to admit that the `Account` class is actually a _really_ bad example.
We only used it because it is very intuitive to want to hide a password, which gives us an easy to explain reason for as why we would want to hide members.

In reality, "hidden" members are still very easily accessible in Python, so the password is still very much exposed.
Python's method of hiding attributes is not meant as a safety feature, but simply as a way to convey intent.
It protects against Murphy, but not against Machiavelli.

Also, as a general rule, passwords are *never* stored, regardless of the technology used, i.e., this is not a Python-specific rule.
For example, websites such as Google, Amazon, Reddit, etc. never store your password as it would be incredibly unsafe to do so.
If you're wondering how a website can check whether your password is correct without having access to it, feel free to ask your lecturer.
