import re

def normalize(phone_number):
    # phone_number = re.sub(r'[^\d()]', '', phone_number)
    if phone_number.startswith('8'):
        phone_number = '+7' + phone_number[1:]
    if not phone_number.startswith('+7'):
        if phone_number.startswith('7'):
            phone_number = '+7' + phone_number[1:]
        else:
            phone_number = '+7495' + phone_number if not phone_number.startswith('495') else '+7' + phone_number[3:]
    phone_number = re.sub(r'\((\d{3})\)', r'\1', phone_number)
    if '- ' in phone_number or '-\n' in phone_number or '-\r' in phone_number or '-\r\n' in phone_number:
        digits = re.findall(r'\d+', phone_number)
        if len(digits[0]) == 1 and '-' in digits[1]:
            return None
    phone_number = phone_number.replace('-', '')
    return phone_number


new_number = input().strip()


phone_book = [input().strip() for _ in range(3)]


for number in phone_book:
    if normalize(number) == normalize(new_number):
        print(normalize(number))
        print("YES")
    else:
       print("NO")
