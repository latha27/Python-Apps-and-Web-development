user_input = input("Enter the string/word to check palindrome or not:").lower()

reverse_input = user_input[::-1]

result = ''
for i in range(len(user_input)):
    if user_input[i] == reverse_input[i]:
        result = result + user_input[i]

if result == user_input:
    print("String/word is palindrome")
else:
    print("String/word Not a palindrome")

