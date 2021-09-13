#figure out
def is_palindrome(s):
    
    #makes all of s lowercase and puts into a list (split would not work)
    arr = list(s.lower())
    #reverses list
    arr2 = list(reversed(arr))
    #makes a new string which is the arr2 joined
    s2 = "".join(arr2)
    #checks if the reverse is the same as the original word but all lowercase
    return s.lower() == s2

print(is_palindrome("abba"))
print(is_palindrome("Abba"))
print(is_palindrome("micheal"))