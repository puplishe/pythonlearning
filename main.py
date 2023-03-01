# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
def first_func(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)


def animal_crackers(some_text):
    some_text.split()
    if some_text[0] == some_text[1]:
        print(some_text[0][0])


def makes_twenty(num1, num2):
    if num1 + num2 == 20:
        return True
    if num1 == 20 or num2 == 20:
        return True
    else:
        return False
def old_mcdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()


def master_yoda(text):

    return  ''.join(text.split()[::-1])

def almost_there(n):

    return abs(100 - n) <= 10 or abs(200 - n) <= 10

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def papper_doll(text):
    list = []
    for x in text:
        list.append(x*3)
    return  ''.join(list)

def blackjack(a, b, c):
    sum = a + b + c
    if sum <= 21:
        return sum
    else:
        if a == 11 or b == 11 or c == 11:
            if sum - 10 <= 21:
                return sum - 10
            else:
                return 'Bust'
        return 'Bust'


def summer_69(arr):
    sum = 0
    add = True
    for x in arr:
        while add:
            if x != 6:
                sum += x
                break
            else:
                add = False
        while not add:
            if x == 9:
                break
            else:
                add = False
                break
    return sum



print(summer_69([4, 5, 6, 7, 8, 9]))