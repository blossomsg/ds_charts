"""This Project gives info of Probability from Chapter 5 in Math 1, 10th Std SSC
Jargon's to remember

- Random Experiment
The experiment in which all possible results are known in advance but none of
them can be predicted with certainty and there is equal possibility for each result is
known as a ‘Random experiment’.

-Outcome
Result of a random experiment is known as an "Outcome"

-Sample
The set of all possible outcomes of a random experiment is called the sample space.
It is denoted by ‘S’ or ‘Ω’ (A greek letter 'Omega'). Each element of sample
space is called a ‘sample point’. The number of elements in the set ‘S’ is denoted by
n(S). If n(S) is finite, then the sample space is said to be a finite sample space.

-Event
The outcomes satisfying particular condition are called favourable outcomes.
A set of favourable outcomes of a given sample space is an ‘event’. Event is a
subset of the sample space.
Events are generally denoted by capital letteres A, B, C, D etc. For example, if
two coins are tossed and A is the event of getting at least one tail, then the favourable
outcomes are as follows.
H = Heads, T = Tails
A = {TT, TH, HT}

-Probability of an event
In Mathematical language, when possibility of an expected event is expressed
in number, it is called ‘Probability’ . It is expressed as a fraction or percentage
using the following formula.
For a random experiment, if sample space is ‘S’and ‘A’ is an expected event
then probability of ‘A’ is P(A). It is given by following formula


Ex
For example, Tossing a coin, throwing a die, picking a card from a set of cards
bearing numbers from 1 to 50, picking a card from a pack of well shuffled playing
cards, etc.

Math 1 std 12th Probability
9.1.5 Elementary Properties of Probability

"""

import enum, random
import math
import matplotlib.pyplot as plt

from scatterplots_chart_01 import label


class Kid(enum.Enum):
    BOY = 0
    GIRL = 1


def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

print(("P(both | older:", both_girls / older_girl))
print(("P(both | either:", both_girls / either_girl))

"""Read about uniform PDF, CDF, and Normal distribution from Math 2 Sci 12th HSC Probability Distributions"""

SQRT_TWO_PI = math.sqrt(2 * math.pi)







