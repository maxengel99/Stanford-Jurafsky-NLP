from rules.rule import Rule
from random import randrange
import re

possible_responses = ['How do you do. Please state your problem', 'Hi. What seems to be your problem?']

class HiRule(Rule):

    def can_apply(self, string):
        result=re.match(r'\bhi\b|\bHi\b|\bhello\b', string)
        if(result):
            return True
        else:
            return False

        return result
        
    def apply(self, input_string=''):
        return possible_responses[randrange(len(possible_responses))]