
iban ="DE29100100100987654321"

first_letter = iban[0]
second_letter = iban[1]

first_letter = str(ord(first_letter) - ord("A")+10)
second_letter = str(ord(second_letter) - ord("A")+10)

print(first_letter)
print(second_letter)

country_code = iban[:2]
check_digit = iban[2:4]
bank_code = iban[4:12]
account_number = iban[12:]

iban_part = bank_code + account_number + first_letter + second_letter + "00"
print(iban_part)

iban_mod = int(iban_part)
iban_mod = 98 - (iban_mod % 97)
print(iban_mod)

if check_digit == str(iban_mod):
    is_check_true = True
else:
    is_check_true = False
print(is_check_true)


#iban1 = input("type iban that want to check")

def iban_verification(iban):
    first_letter = iban[0]
    second_letter = iban[1]

    first_letter = str(ord(first_letter) - ord("A")+10)
    second_letter = str(ord(second_letter) - ord("A")+10)
    
    #country_code = iban[:2]
    check_digit = iban[2:4]
    bank_code = iban[4:12]
    account_number = iban[12:]

    iban_part = bank_code + account_number + first_letter + second_letter + "00"
    
    iban_mod = int(iban_part)
    iban_mod = 98 - (iban_mod % 97)
    
    if check_digit == str(iban_mod):
        return  True
    else:
        return  False

print(iban_verification("DE29100100100987654324"))