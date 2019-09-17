def merge_the_tools(string, k):
    total = len(string)
    for i in range(int(total / k)):
        cur_line = []
        for j in range(i * k, (i + 1) * k):
            letter = string[j]
            if letter not in cur_line:
                cur_line.append(letter)

        print(''.join(cur_line))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)