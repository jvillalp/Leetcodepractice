"""
Print out each element of the following array on a separate line:

['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

array_list = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]
#iterate through list
for item in array_list:
    #print each item indivudually
    print(item)

def nested_print(nested_list):
    #interate through list (for loop)
    for item in nested_list:
        #conditionals
        if isinstance(item, list):
            nested_print(item)
        #base case
        else:
            print(item)

    # for item in nested_list:
    #     if type(item) == str:
    #         print(item)
    #     elif type(item) == list:
    #         for i in item:
    #             if type(i) == str:
    #                 print(i)
    #             elif type(i) == list:
    #                 for x in i:
    #                     print(x)
    #     elif type(item) == int:
    #         print(item)  

x = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
nested_print(x)
"""
Stretch:
Print out each element of the following array on a separate line, but 
this time the input array can contain arrays nested to an arbitrarily deep level:
['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

For the above input, the expected output is:
Bob
Slack
reddit
89
101
alacritty
(brackets)
5
375
0
{slice, owned}
22



=============================
STRETCH SOLUTION: One Possible Approach
The overarching idea for this problem is that while looping through the elements of the input array, we need to check if the current element is an array. If it is an array, then the contents of the nested array need to be printed. This can be done with a recursive call. In pseudocode, a possible solution might look like this:
function nested_print(arr: Array) {
  for element in arr {
    if type(element) == Array {
      nested_print(element)
    } else {
      print(element)
    }
  }
}
"""