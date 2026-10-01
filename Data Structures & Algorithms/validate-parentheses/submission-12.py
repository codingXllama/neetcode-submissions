class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        myStack = [] 
        openBrackets = "([{"
        closingBracket= ")]}"

        for bracket in s:
            #opening bracket
            if bracket in openBrackets:
                myStack.append(bracket)
            
            #closing bracket
            else:   
                if myStack and pairs[bracket] == myStack[-1]:
                    myStack.pop()
                else:
                    return False
                
        return len(myStack)==0