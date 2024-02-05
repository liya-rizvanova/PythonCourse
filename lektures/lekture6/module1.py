def tri(a, h):
    return 0.5 * a * h

def circle(r):
    return 3.14 * r**2

def rect(a, b):
    return a * b

def main():
    print('Начало модуля 1: ')
    print('Начинаем считать площадь сложной фигуры: ')
    area = rect(20, 30) + tri(20, 15) - circle(5)
    print(f'{area=}')
    print('Конец модуля 1')


# if __name__ == '__main__':
# main()

if __name__ == '__main__':
    print('Начало модуля 1: ')
    print('Начинаем считать площадь сложной фигуры: ')
    area = rect(20, 30) + tri(20, 15) - circle(5)
    print(f'{area=}')
    print('Конец модуля 1')