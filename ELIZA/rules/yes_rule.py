from rules.rule import Rule
from random import randrange
import re

possible_responses = ['You seem to be quite positive.', 'You are sure.', 'I understand']

class YesRule(Rule):

    def can_apply(self, string):
        result=re.match(r'\byes\b', string)
        if(result):
            return True
        else:
            return False

        return result

    def apply(self, string):
        return '{response}'.format(response=possible_responses[(randrange(len(possible_responses)))])