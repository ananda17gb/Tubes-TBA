class ANA:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "A":    "q2",
                "n":    "q5",
                "a":    "q5",
                "other":"q5",
                "EOS":  "error"     
            },
            "q2": {
                "A":    "q5",
                "n":    "q3",
                "a":    "q5",
                "other":"q5",
                "EOS":  "error"     
            },
            "q3": {
                "A":    "q5",
                "n":    "q5",
                "a":    "q4",
                "other":"q5",
                "EOS":  "error"     
            },
            "q4": {
                "A":    "q5",
                "n":    "q5",
                "a":    "q5",
                "other":"q5",
                "EOS":  "accept"     
            },
            "q5": {
                "A":    "q5",
                "n":    "q5",
                "a":    "q5",
                "other":"q5",
                "EOS":  "error"     
            }
        }

    def valid(self, word):
        word += "#"
        state = "q1"

        for char in word:
            if char == "A":
                state = self.TABLE[state]["A"]
            elif char == "n":
                state = self.TABLE[state]["n"]
            elif char == "a":
                state = self.TABLE[state]["a"]
            elif char == "#":
                state = self.TABLE[state]["EOS"]
            else:
                 state = self.TABLE[state]["other"]
            
            if state == "error":
                return False
            elif state == "accept":
                return True
        return False