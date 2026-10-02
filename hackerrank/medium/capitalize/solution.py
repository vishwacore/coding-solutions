

# Complete the solve function below.
def solve(s):
    result=""
    for word in s.split(" "):
        if word and word[0].isalpha():
            word = word[0].upper() + word[1:]
        result += word + " "
    
    return result.strip()

