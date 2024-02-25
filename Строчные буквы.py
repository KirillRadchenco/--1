# Исходная строка
input_string = "аоыгСпДЕыйччЛавывсАаЛ ДвыотЕпотоЛмучфО - ГпайУтонЛвеселЯЙ СыйМявапкЕиудывЛО"

# Удаление строчных букв из строки
result_string = ''.join(char for char in input_string if not char.islower())

# Вывод результата
print(result_string)
