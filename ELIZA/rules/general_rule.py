from rules.rule import Rule
from random import randrange
import re

possible_responses = ['Tell me more', 'That is interesting', 'I understand']

class GeneralRule(Rule):

    def apply(self):
        return possible_responses[randrange(len(possible_responses))]