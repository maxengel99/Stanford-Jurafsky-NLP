
from rules.question_rule import QuestionRule
from rules.am_rule import AmRule
from rules.remember_rule import RememberRule
from rules.no_rule import NoRule
from rules.yes_rule import YesRule
from rules.are_rule import AreRule
from rules.hi_rule import HiRule
from rules.was_rule import WasRule
from rules.general_rule import GeneralRule

class Eliza:

    def __init__(self):
        self.rules = [QuestionRule(), RememberRule(), AmRule(), NoRule(), YesRule(), AreRule(), HiRule(), WasRule()]
        self.general_response = GeneralRule()
    
    def hold_conversation(self):
        user_input = input("Hi, how are you?\n")
        while True:
            response = self.get_response(user_input)
            user_input = input('{response}\n'.format(response=response))
    
    def get_response(self, user_input):
        for rule in self.rules:
            check_rule = rule.can_apply(user_input)
            if(check_rule):
                return rule.apply(user_input)
        
        return self.general_response.apply()

if __name__ == '__main__':
    Eliza().hold_conversation()
