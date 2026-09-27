class Solution:
    def isValid(self, s: str) -> bool:
        openParens = "[{("
        closingParens = "]})"

        myStack = []

        matchingPairs = {"{": "}", "[": "]", "(": ")"}

        for bracket in s:
            # If we get an opening bracket
            if bracket in openParens:
                myStack.append(matchingPairs[bracket])

            # If we get a closing bracket
            if bracket in closingParens:
                # Stack is empty → nothing to compare against
                if len(myStack) == 0:
                    return False

                # Closing bracket doesn't match the top of stack
                if bracket != myStack[-1]:
                    return False

                # Match → remove from stack
                myStack.pop()

        return len(myStack) == 0
