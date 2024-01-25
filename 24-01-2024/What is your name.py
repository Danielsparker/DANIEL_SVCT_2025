'''
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello firstname lastname! You just delved into python' where firstname  and lastname  are replaced with first and last .
Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last names are each ≤ 10 .

Sample Input 0

Faf
duplessis
Sample Output 0

Hello Faf duplessis! You just delved into python.
Explanation 0

The input read by the program is stored as a string data type. A string is a collection of characters.

code
---------------------
'''

def print_full_name(first, last):
    print("Hello " + first, last + "! You just delved into python.")
