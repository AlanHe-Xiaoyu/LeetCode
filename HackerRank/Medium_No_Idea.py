def score_it(arr, A, B):
    happiness = 0
    # for i in arr:
    #     if i in A:
    #         happiness += 1
    #     elif i in B:
    #         happiness -= 1
    happiness = sum((i in A) - (i in B) for i in arr)
    
    print(happiness)


if __name__ == '__main__':
    lengths = input().split(' ')
    arr, A, B = input().split(' '), set(input().split(' ')), set(input().split(' '))
    score_it(arr, A, B)