#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Since the function will always get to a return statement in the first iteration of the for loop,
        the function will only check if the first letter is lowercase instead of every letter.
        for example, the word 'Boom' has lower case letters, but this function will return false
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Instead of using the .islower() function on the variable c, this function uses it on the char value 'c',
        so 'c'.islower() isnt actually checking a letter in the string and will always return True because 'c' 
        is lower case.  Notice any_lowercase2('ALLCAPS') returns 'True'.  Also, instead of this function 
        returning the boolean True, it returns a string 'True'. notice type(any_lowercase2('ALLCAPS')) is str
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """This function uses a flag variable to be set to True if a c.islower() returns True.  However, this flag is
        set to a new boolean value for every letter it checks, so if it catches a lower case before the end of the 
        string, the flag variable will be reassigned after, so this function really only returns the value of the 
        check of the last letter.  Notice how any_lowercase3('GoT') returns False even though it has a lowercase 'o'
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """All good here!  notice how any_lowercase4('ALLCAPS') returns False and any_lowercase4('ONExLOWER')) 
        returns True, both correct
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """This Function will return False after it hits one upper case letter
        notice how any_lowercase5('xxxxxXxxxxx') returns False, even though it
        has all lower case letters except one
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1('Boom'))
    print(any_lowercase2('ALLCAPS'))
    print(type(any_lowercase2('ALLCAPS')))
    print(any_lowercase3('GoT'))
    print(any_lowercase4('ALLCAPS'))
    print(any_lowercase4('ONExLOWER'))
    print(any_lowercase5('xxxxxXxxxxx'))

if __name__ == '__main__':
    main()
