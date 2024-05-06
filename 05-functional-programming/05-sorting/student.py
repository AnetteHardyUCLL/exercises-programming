from operator import attrgetter


def sort_by_age(people):
    return sorted(people, key=attrgetter("age"))


def sort_by_decreasing_age(people):
    return sorted(people, key=attrgetter("age"), reverse=True)


def sort_by_name(people):
    return sorted(people, key=attrgetter("name"))


def sort_by_name_then_age(people):
    return sorted(people, key=lambda person: (person.name, person.age))


def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=lambda person: (person.name, -person.age))
