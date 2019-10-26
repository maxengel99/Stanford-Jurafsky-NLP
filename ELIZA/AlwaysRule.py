from Rule import Rule
import re

class AlwaysRule(Rule):
    def apply(self, string):
        return 'test'

    def can_apply(self, string):
        return 'no'
    
    def is_final(self, string):
        return False 