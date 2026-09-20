class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        paren_dict = {'(':')', '[': ']', '{': '}'}
        if not s:
            return False

        for c in s:
            if c in paren_dict:
                stk.append(c)
            elif not stk:
                return False
            else:
                buttom = stk.pop()
                if paren_dict[buttom] != c:
                    return False
        if not stk:
            return True
        else:
            return False