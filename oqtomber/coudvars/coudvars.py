#  1)შექმენით პროგრამა, რომელიც იღებს ორობითი ნომერს და გარდაქმნის მას ათობითი.

def binary_to_decimal(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value

binary_input = input("შეიყვანეთ ოობითი რიცხვი: ")
decimal_output = binary_to_decimal(binary_input)

print(f"{binary_input} --> {decimal_output}")

# 2) შექმენით პროგრამა, რომელიც იღებს ათობითი ნომერს და გარდაქმნის მას ორობითი.

def decimal_to_binary(decimal_num):
    binary_value = bin(decimal_num)[2:]
    return binary_value

decimal_input = int(input("შეიყვანეთ ათობით რიცხვი: "))
binary_output = decimal_to_binary(decimal_input)

print(f"{decimal_input} --> {binary_output}")

# 3) შექმენით პროგრამა, რომელიც იღებს სიას და შლის დუბლიკატ ელემენტებს ორიგინალური წესრიგის შენარჩუნებისას.

def remove_duplicates(input_list):
    unique_list = []  
    for item in input_list:
        if item not in unique_list:  
            unique_list.append(item) 
    return unique_list

user_input = input("შეიყვანეთ ელემენტების ჩამონათვალი (ყოჲღას ',' უნდა იყოს): ")

input_list = user_input.split(',')

for i in range(len(input_list)):
    input_list[i] = input_list[i].strip()

output_list = remove_duplicates(input_list)

print(f"{input_list} --> {output_list}")

# 4)შექმენით პროგრამა, რომელიც იღებს არაუარაციულ მთელი რიცხვით 
# და უბრუნებს თავის ფაქტობრიალს. რიცხვი n ფაქტორია ყველა დადებითი 
# მთელი რიცხვის პროდუქტი 1-დან n-მდე. განმარტებით, 0 ფაქტორია 1.

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


try:
    user_input = int(input("შეიყვანეთ არა უარყოფითი მთელი რიცხვი: "))
    if user_input < 0:
        print("გთხოვთ, შეიყვანეთ არა უარყოფითი რიცხვი.")
    else:
        output = factorial(user_input)
        print(f"{user_input}  {output}")
except ValueError:
    print("გთხოვთ, შეიყვანეთ ვალიდური მთელი რიცხვი.")


# 5)შექმენით პროგრამა, რომელიც ამოწმებს, თუ მოცემული სტრიქონი არის პალინდრომი 
# (კითხულობს იგივე წინ და უკან). ფუნქცია უნდა უგულებელყოს სივრცეები, პუნქტუაცია და კაპიტალიზაცია.

import string

def is_palindrome(input_string):
    cleaned_string = ""
    
    for char in input_string:
        if char.isalnum(): 
            cleaned_string += char.lower()  
    
    reversed_string = ""
    
    for char in cleaned_string:
        reversed_string = char + reversed_string  
    
    return cleaned_string == reversed_string

user_input = input("შეიყვანეთ სტრიქონი: ")

result = is_palindrome(user_input)

print(f'"{user_input}" --> {result}')



# 6) თქვენ მიიღებთ სტრიქონს, რომელიც შეიცავს სიტყვებს PascalCase- ში, თქვენი საქმეა მათი გადაკეთება snake_case.

def pascal_to_snake_manual(s):
    result = []
    
    for char in s:
        if char.isupper() and result: 
            result.append('_')
        result.append(char.lower())
    
    return ''.join(result).replace(' ', '_') 


print(pascal_to_snake_manual("TestController")) 
print(pascal_to_snake_manual("MoviesAndBooks"))
print(pascal_to_snake_manual("App7 Test"))      
print(pascal_to_snake_manual("1"))                

# 7) შექმენით პროგრამა, რომელიც იღებს მთელი რიცხვი n და აბრუნებს პირველ n ნომრებს ფიბონაჩის თანმიმდევრობით.
#  თანმიმდევრობა იწყება 0 და 1 და ყოველი მომდევნო რიცხვი არის წინა ორის ჯამი.

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence


print(fibonacci_sequence(5))  
print(fibonacci_sequence(7)) 


# 8) თქვენი ამოცანაა მოცემული სტრიქონის დალაგება. სტრიქონში თითოეული სიტყვა შეიცავს ერთ ნომერს.
#  ეს რიცხვი არის პოზიცია, რომელიც სიტყვას უნდა ჰქონდეს შედეგში.
# შენიშვნა: რიცხვები შეიძლება იყოს 1-დან 9-მდე. ასე რომ, 1 იქნება პირველი სიტყვა (არა 0).
# თუ შეყვანის სტრიქონი ცარიელია, დააბრუნეთ ცარიელი სტრიქონი. შეყვანის სტრიქონში მოცემული
#  სიტყვები შეიცავს მხოლოდ ზედიზედ მოქმედ ნომრებს.

def order(sentence):
    if not sentence:
        return ""
    
    words = sentence.split()
    
    sorted_words = sorted(words, key=lambda x: int(''.join(filter(str.isdigit, x))))
    
    return ' '.join(sorted_words)

print(order("is2 Thi1s T4est 3a"))  
print(order("4of Fo1r pe6ople g3ood th5e the2")) 
print(order("")) 











# 9) დაწერეთ ფუნქცია, რომელიც იღებს მაქსიმალურ bound და
#  აბრუნებს ყველა პრაიმს და მათ შორის მაქსიმალურ bound.

#                       ?






# 10 Eureka ნომრები ასეთი რიცხვებია: 135 = 1^1 + 3^2 + 5^3. რაც ნიშნავს,
#  რომ ჩვენ უნდა ავიღოთ რიცხვი და შევაჯამოთ მისი ციფრები ზედიზედ ძალებზე.
# პირველი ციფრი 1-ზე, მეორე ძალა 2-ზე და ა.შ. თუ ამ თანხის შედეგი იგივეა, რაც თავად რიცხვი,
#  რაც ნიშნავს, რომ რიცხვი არის ევრეკა.
# შექმენით ფუნქცია, რომელიც იღებს დიაპაზონს, როგორიცაა (a, b) და გამოიმუშავებს მასში ყველა ევრეკას ნომერს.
# შენიშვნა: ყველა რიცხვი, რომელსაც ერთი ციფრი აქვს, არის ევრეკა, რადგან მაგალითად 5 = 5^1...

#                                            ?
