from Rule import Rule
import re

class RememberRule(Rule):
    def can_apply(self, string):
        result = re.match(r'.*\sremember\s(.*)', string)
        if(result):
            return True
        else:
            return False

        return result

    def apply(self, string):
        subject = re.search(r'.*\sremember\s(.*)', string).group(1)
        subject = subject.replace('I ', 'you ')
        subject = subject.replace('i ', 'you ')
        return 'What made you think of {subject}?'.format(subject=subject)