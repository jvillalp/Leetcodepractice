"""
Given a string and a non-negative int n, 
we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. 
Return n copies of the front;
"""
def front_times(str, n):
    front_len = 3
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]
  
    result= ""
    for i in range(n):
        result = result + front
    return result
    
print(front_times('Chocolate', 2))

"""
Given a string, return a new string made of every other char starting with the first, 
so "Hello" yields "Hlo".
"""

def string_bits(str):
    #string that skips chars
    new_string = ""
    for i in range(len(str)):
        if i%2==0:
            new_string = new_string + str[i]
    #return str[::2]
    return new_string

print(string_bits('Hello'))


