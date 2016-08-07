# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

#rotates letter c by int n
def rotate_letter(c, n):
	if c.isupper():
		start = ord('A')
	elif c.islower():
		start = ord('a')
	else:
		#just return the char if its not a letter
		return c
	i = (ord(c) + n - start) % 26 + start
	return chr(i)


#rotates string s by int n
def rotate_word(s, n):
	result = ''
	for letter in s:
		result += rotate_letter(letter, n)
	return result


def main():

    print(rotate_word('Nicolas', 7))
    print(rotate_word('Mon', -10))
    print(rotate_word('sleep', 9))

if __name__ == '__main__':
    main()