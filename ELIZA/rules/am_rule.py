from rules.rule import Rule
import re
from random import randrange

possible_questions = ['Do you believe it is normal to be', 'Do you enjoy being', 'Do you know anyone else who is']

class AmRule(Rule):
    def can_apply(self, string):
        result = re.match(r'.*\sam\s(.*)', string)
        if(result):
            return True
        else:
            return False

        return result
    
    def apply(self, string):
        subject = re.search(r'.*\sam\s(.*)', string).group(1)
        return '{question} {subject}?'.format(question=possible_questions[(randrange(len(possible_questions)))], subject=subject)