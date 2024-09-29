from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
a = list(map(lambda x,y : x == y, first, second))
print(a)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='UTF-8') as file:
            for line in data_set:
                file.write(str(line))
                file.write('\n')
    return write_everything

class MysticBall:
    def __init__(self, *word):
        self.words = word
    def __call__(self):
        word = choice(self.words)
        return word


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())