from rules.rule import Rule
from random import randrange
import re

possible_responses = ['Are you saying no just to be negative', 'You are being a bit negative', 'Why \'no\'']

class NoRule(Rule):

    def can_apply(self, string):
        result=re.match(r'\bno\b', string)
        if(result):
            return True
        else:
            return False

        return result

    def apply(self, string):
        return '{response}'.format(response=possible_responses[(randrange(len(possible_responses)))])