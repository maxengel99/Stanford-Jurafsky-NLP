from rules.rule import Rule
import re
from random import randrange

def format_response(question_word):
    possible_responses = ['I don\'t know. {question_word} do you think?'.format(question_word=question_word),
    'Interesting question. Do you have any idea {question_word}?'.format(question_word=question_word)]
    return possible_responses[randrange(0, len(possible_responses))]

class QuestionRule(Rule):

    def can_apply(self, string):
        result = re.match(r'^what\s(.*)|^where\s(.*)|^who\s(.*)|^why\s(.*)|^when\s(.*)', string)

        if(result):
            return True
        else:
            return False

        return result

    def apply(self, string):
        question_word = re.search(r'([a-zA-Z]*)\s', string).group(1)

        return format_response(question_word)