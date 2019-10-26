
from rules.am_rule import AmRule
from rules.remember_rule import RememberRule

class Eliza:

    def __init__(self):
        self.rules = [RememberRule(), AmRule()]
    
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

if __name__ == '__main__':
    Eliza().hold_conversation()
