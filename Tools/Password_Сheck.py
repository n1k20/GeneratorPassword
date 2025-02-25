def password_check(password: str) -> bool:
    data = {'Upper': 0, 'Lower': 0, 'Numbers': 0, 'Symbols': 0}
    Upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']
    Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Symbols = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
               '[', ']', '^', '_`', '{', '|', '}', '~', '(']
    for letter in password:
        if letter in Upper: data['Upper'] += 1
        if letter in Lower: data['Lower'] += 1
        if letter in Numbers: data['Numbers'] += 1
        if letter in Symbols: data['Symbols'] += 1
    if (data['Upper'] >= 2 and data['Lower'] >= 2 and data['Numbers'] >= 2 and data['Symbols'] >= 2) == True:
        return True
    return False


def Check(data):
    count = 0
    print("----------------------------------------")
    print("PASSWORD GENERATOR")
    print("________________________________________")
    while count != 20:
        password = ""
        while password_check(password=password) == False:
            password = random_password(data=data)
        print(password)
        count += 1
    print("----------------------------------------")