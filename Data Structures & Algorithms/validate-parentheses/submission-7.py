class Solution:
    def isValid(self, s: str) -> bool:
        openParen = "[{("
        closingParen = "]})"
        myStack = []
        matchingPairs = {"{": "}", "[": "]", "(": ")"}
    
        for bracket in s:
            #adding in the closing bracket
            if bracket in openParen:
                myStack.append(matchingPairs[bracket])
            
            if bracket in closingParen:
                #making sure there is something to compare to, i.e stack is not empty
                if myStack and bracket == myStack[-1]:
                    myStack.pop()
                else:
                    return False
                        
        return True if len(myStack) == 0 else False