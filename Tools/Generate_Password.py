def GeneratePassword():
    length = input("Введите длину пароля: ")
    DATA = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
            '[', ']', '^', '_`', '{', '|', '}', '~', '(', '"']
    if length.isdigit() == False and int(length) >= 8:
        while length.isdigit() == False and int(length) >= 8:
            length = input("Введите корректную длину пароля (в числах и больше 8, а желательно больше 15): ")
    symbols = input("Будут ли различные символы по типу . , ? * (No/Yes или введите кастомные знаки): ").lower()
    if all([letter in DATA for letter in symbols]) or symbols == "'":
        print("OKey")
    if symbols not in ["no", "yes"]:
        while symbols not in ["no", "yes"] or symbols in DATA:
            symbols = input(
                "Ответьте на вопрос (No/Yes или ваши символы в списке: ").lower()

    return [int(length), DATA]