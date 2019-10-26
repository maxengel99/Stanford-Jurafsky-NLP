from rules.rule import Rule
import re
from random import randrange

def format_response(subject, description):
    possible_responses = ['Why was {subject} {description}?'.format(subject=subject, description=description),
    'That\'s interesting. What makes you think {subject} {description}?'.format(subject=subject, description=description)]
    return possible_responses[randrange(len(possible_responses))]

class WasRule(Rule):
    def can_apply(self, string):
        result = re.match(r'.*\swas\s.*', string)
        if(result):
            return True
        else:
            return False

        return result
    
    def apply(self, string):
        key_words = re.search(r'(.*)\swas\s(.*)', string)
        subject = key_words.group(1)
        description = key_words.group(2)
        return format_response(subject, description)