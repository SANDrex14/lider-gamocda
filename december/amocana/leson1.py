#  1)


# number =  [1, -4, 7, 12]
# positiv = []

# def problem_1_sum_of_positive(number):
#     for i in number:
#         if i > 0:
#             positiv.append(i)
        

# assert problem_1_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_1_sum_of_positive([-1, -2, -3, -4]) == 0
# assert problem_1_sum_of_positive([]) == 0


# 2) 

# def problem_2_sum_of_positive(numbers):
#     total = 0
#     for num in numbers:
#         if num > 0:
#             total += int(num)  
#     return total


# print(problem_2_sum_of_positive([1, -4, 7, 12]) == 20) 
# print(problem_2_sum_of_positive([-1.5, 2.7, -3.3, 4.8]) == 6)  
# print(problem_2_sum_of_positive([]) == 0)  
# print(problem_2_sum_of_positive([-1, -2, -3]) == 0)  


# 3) 

# def find_missing_numbers(numbers):
#     full_sequence = list(range(1, 11))
    
#     missing_numbers = []
    
#     for num in full_sequence:
#         if num not in numbers:
#             missing_numbers.append(num)
    
#     print("გამორჩენილი რიცხვები:")
#     for missing in missing_numbers:
#         print(missing)

# numbers = [1, 2, 4, 6, 8, 10]
# find_missing_numbers(numbers)


# # 4)

# def longest_unique_substring(s: str) -> int:
#     max_len = 0
#     start = 0
#     seen = {}

#     for end in range(len(s)):
#         if s[end] in seen and seen[s[end]] >= start:
#             start = seen[s[end]] + 1
#         seen[s[end]] = end
#         max_len = max(max_len, end - start + 1)

#     return max_len

# assert longest_unique_substring("abcabcbb") == 3
# assert longest_unique_substring("bbbbb") == 1
# assert longest_unique_substring("") == 0
# assert longest_unique_substring("pwwkew") == 3


# 5)

# def are_anagrams(str1: str, str2: str) -> bool:
#     return sorted(str1) == sorted(str2)

# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True

# 6)

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# def find_intersection(list1, list2):
#     intersection = []
#     for item in list1:
#         if item in list2 and item not in intersection:
#             intersection.append(item)
#     return intersection

# intersection = find_intersection(list1, list2)

# print(intersection)


# 7)






