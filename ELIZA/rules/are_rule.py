from rules.rule import Rule
import re
from random import randrange

def format_response(subject, description):
    possible_questions = ['How are {subject} {description}?'.format(subject=subject, description=description), 
    'What {subject} are {description}?'.format(subject=subject, description=description)]
    return possible_questions[randrange(0, len(possible_questions))]

class AreRule(Rule):

    def can_apply(self, string):
        result = re.match(r'(.*)\sare\s(.*)', string)

        if(result):
            return True
        else:
            return False

        return result

    def apply(self, string):
        key_words = re.search(r'(.*)\sare\s(.*)', string)
        subject = key_words.group(1)
        description = key_words.group(2)

        return format_response(subject, description)