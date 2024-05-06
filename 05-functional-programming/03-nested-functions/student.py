from util import *


def count_older_than(people, min_age):
    def older_than_min_age(person):
        return person.age >= min_age

    return count(people, older_than_min_age)


def indices_of_cards_with_suit(cards, suit):
    def has_suit(card):
        return card.suit == suit

    return indices_of(cards, has_suit)
