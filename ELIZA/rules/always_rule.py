from rules.rule import Rule
import re

class AlwaysRule(Rule):
    def can_apply(self, string):
        return 'no'

    def apply(self, string):
        return 'test'