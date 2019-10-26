class Rule:
    def apply(self, string):
        return string

    def can_apply(self, string):
        return False
    
    def is_final(self, string):
        return False 