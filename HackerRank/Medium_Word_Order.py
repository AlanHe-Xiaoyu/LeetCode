# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    all_words = {}
    for _ in range(n):
        word = input()
        all_words[word] = all_words.get(word, 0) + 1
    
    print(len(all_words))
    vals = [item[1] for item in all_words.items()]
    print(*vals, sep=' ')