# import sys

def minion_game(string):
    # your code goes here
    # print(string[:-1])
    # line = sys.stdin[0]
    total = len(string)

    vowels = ["A", "E", "I", "O", "U"]
    stuart, kevin = 0, 0

    for i in range(total):
        if string[i] in vowels:
            kevin += total - i
        else:
            stuart += total - i

    if stuart == kevin:
        print("Draw")
    elif stuart > kevin:
        print("Stuart " + str(stuart))
    else:
        print("Kevin " + str(kevin))


if __name__ == '__main__':
    s = input()
    minion_game(s)