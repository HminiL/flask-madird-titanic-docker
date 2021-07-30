class ReverseString(object):

    def str_to_list(self, payload: str) -> []:
        return [char for char in payload if char.isalnum()]


    def reverse_list(self, ls: []) -> []:
        return ls[::-1]


    def list_to_str(self, ls: []) -> str:
        return ''.join(ls)


    def reverseString(self, strs: []) -> []:
        return strs[::-1]
