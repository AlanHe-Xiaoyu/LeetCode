'''
Intuition : use math
'''

# class Solution:
#     def intLength(num):
#         length = 0
#         while num:
#             length += 1
#             num = num // 10
        
#         return length
        
#     def closestDown(num):
#         if num % 10 == 0:
#             num -= 1

#         copy = num
#         length = Solution.intLength(num)
#         # print(length)
#         halfLen = length // 2

#         secondHalf = 0
#         multiplier = 1
#         for i in range(halfLen):
#             multiplier *= 10
#             # secondHalf = secondHalf * 10 + copy % 10
#             copy = copy // 10
        
#         anotherCopy = copy
#         # if copy % 10 == 0:
#         #     anotherCopy = copy - 1
#         #     copy -= 1
#         #     multiplier = multiplier // 10

#         if length % 2 == 1:
#             copy = copy // 10

#         # print(copy)
#         for i in range(halfLen):
#             secondHalf = secondHalf * 10 + copy % 10
#             copy = copy // 10
        
#         return anotherCopy * multiplier + secondHalf
        
#     def nearestPalindromic(self, n: str) -> str:
#         orig = int(n)

#         if orig == 1:
#             return '0'

#         down = Solution.closestDown(orig - 1)

#         up = Solution.closestDown(orig + orig - down)

#         if up == orig:
#             return str(down)

#         return str(min([down, up], key=lambda p : abs(orig - p)))

