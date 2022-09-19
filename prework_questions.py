#CODING TEMPLE prework questions

# QUESTION 1
## Write a function to print "hello_USERNAME!"
### USERNAME is the input of the function

def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name('USERNAME')

# QUESTION 2
## Write a python function, first_odds that prints the odds numbers from
### 1-100 and returns nothing

def first_odds():
    for odd in range(1,100,2):
        print(odd)
    

first_odds()
print(first_odds())

# QUESTION 3
## Write a python function, max_num_in_list to return the max number
### of a given list

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

ages = [25, 42, 85, 21, 15, 55, 61, 77, 88, 92, 4, 12]

answer = max_num_in_list(ages)
print(answer)

# QUESTION 4 
## Write a function to return if the given year is a leap year. A leap year
### is divisible by 4, but not divisible by 100, unless it is also divisble
#### by 400. The return should be boolean Type

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
    
verdict = is_leap_year(2022)
print(verdict)

# QUESTION 5
## Write a function to check to see if all numbers in a list are consecutive
### numbers. The return should be boolean Type.

list = [1, 2, 4, 5]
list_2 = [2, 3, 4, 5, 6, 7]
august_temps = [91, 92, 99, 101, 88, 96, 105, 85, 89]

def is_consecutive(a_list):
    if a_list[len(a_list) -1] - a_list[0] == len(a_list) - 1:
        return True
    else:
        return False

print(is_consecutive(list))
print(is_consecutive(list_2))

