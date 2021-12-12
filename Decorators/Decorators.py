import sys
import datetime

# Задача 1
# Для начала, давайте подменим метод write у объекта sys.stdin на такую функцию, которая перед каждым вызовом
# оригинальной функции записи данных в stdout допечатывает к тексту текущую метку времени.
original_write = sys.stdout.write


def my_write_1(string_text):
    now = datetime.datetime.now()
    if string_text == '\n':
        return original_write('\n')
    return original_write(f'[{now.strftime("%d-%m-%Y %H:%M:%S")}]: {string_text}')


print('Задача 1:')
sys.stdout.write = my_write_1
print('1, 2, 3')
print('\n')
sys.stdout.write = original_write


# Задача 2
# Упакуйте только что написанный код в декторатор.
# Весь вывод фукнции должен быть помечен временными метками так, как видно выше.
def time_output(function):
    def wrapper(*args, **kwargs):
        def my_write_2(string_text):
            now = datetime.datetime.now()
            if string_text == '\n':
                return original_write('\n')
            return original_write(f'[{now.strftime("%d-%m-%Y %H:%M:%S")}]: {string_text}')

        sys.stdout.write = my_write_2
        function(*args, **kwargs)
        sys.stdout.write = original_write

    return wrapper


@time_output
def print_greeting(name):
    print(f'Hello, {name}!')


print('Задача 2:')
print_greeting('Alexander')
print('\n')


# Задача 3
# Напишите декторатор, который будет перенаправлять вывод фукнции в файл.
# Подсказка: вы можете заменить объект sys.stdout каким-нибудь другим объектом.
def redirect_output(filepath):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            tmp_object = sys.stdout
            output = open(filepath, 'w')
            sys.stdout = output
            function(*args, **kwargs)
            output.close()
            sys.stdout = tmp_object

        return inner_wrapper
    return outer_wrapper


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


print('Задача 3:')
print('Результат выполнения находится в файле: function_output.txt')
calculate()
