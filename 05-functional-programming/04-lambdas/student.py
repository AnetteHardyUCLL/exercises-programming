from util import *


def group_by_suit(cards):
    return group_by(cards, lambda card: card.suit)


def group_by_value(cards):
    return group_by(cards, lambda card: card.value)


def partition_by_color(cards):
    return partition(cards, lambda card: card.suit in ["clubs", "spades"])
