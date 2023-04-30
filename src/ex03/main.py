# def remove(number: str) -> str:
#     result = number.replace("-", "")
#     result = result.replace("8", "", 1) if result[0] == '8' and len(result) >= 11 else result.replace("+7", "")
#     result = result.replace("(", "")
#     result = result.replace(")", "")
#     result = result[3:] if len(result) == 10 else result
#     return result
#
#
# def equal(number_1: str, number_2: str) -> None:
#     if number_1 == number_2:
#         print("YES")
#     else:
#         print("NO")
#
#
# number_add = input()
# number_one = input()
# number_two = input()
# number_three = input()
#
# if __name__ == "__main__":
#     number_add = remove(number_add)
#     number_one = remove(number_one)
#     number_two = remove(number_two)
#     number_three = remove(number_three)
#
#     equal(number_add, number_one)
#     equal(number_add, number_two)
#     equal(number_add, number_three)


import re

def normalize(phone_number):
    phone_number = re.sub(r'[^\d()]', '', phone_number)
    if phone_number[0] == '8':
        phone_number = '+7' + phone_number[1:4] + phone_number[4:].replace("-", '')
    if not phone_number.startswith('+7'):
        if phone_number.startswith('7'):
            phone_number = '+7495' + phone_number if phone_number[:4] != '7495' else '+' + phone_number
        else:
            phone_number = '+7495' + phone_number if phone_number[:3] != '495' else '+7' + phone_number
    phone_number = re.sub(r'\((\d{3})\)', r'\1', phone_number)
    return phone_number


new_number = input().strip()


phone_book = [input().strip() for _ in range(3)]


for number in phone_book:
    if normalize(number) == normalize(new_number):
        print("YES")
    else:
       print("NO")

# print(test_str[3:])
# if len(number_one) == 7 or len(number_two) == 7 or len(number_three) == 7:
#     if test_str[3:] in (number_one, number_two, number_three):
#         print("YES")
