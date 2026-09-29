class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "{":"}",
            "(":")",
            "[":"]",
        }
        myStack = []
        openBrackets = "[{("

        for bracket in s:
            #appending closing bracket for the opening
            if bracket in openBrackets:
                myStack.append(pairs[bracket])
            else:
                # dealing with closing brackets
                if myStack and bracket == myStack[-1]:
                    myStack.pop()
                else:
                    return False
        return len(myStack)==0