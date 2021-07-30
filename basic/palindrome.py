class Palindrome(object):

    def str_to_list(self, payload: str) -> []:
        return [i for i in payload if i.isalnum()]
        """
        strs = []
        for char in payload:
            if char.isalnum():
                strs.append(char.lower())
        return strs
        """

    def isPalindrome(self, ls: []) -> bool:
        '''
        while len(ls) > 1:
            if ls.pop(0) != ls.pop():
                return False
        '''
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}






