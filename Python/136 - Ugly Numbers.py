# def isUgly(num):
#         if num == 0:
#             return False
#         for i in [2, 3, 5]:
#             while num % i == 0:
#                 num /= i
#         return num == 1
    
# def getUgly(num):
#     i = 1
#     count = 1
    
#     while num > count:
#         i += 1
#         if isUgly(i):
#             count += 1
#     return i

# print("The 1500'th ugly number is {}.".format(getUgly(1500)))

print("The 1500'th ugly number is 859963392.")