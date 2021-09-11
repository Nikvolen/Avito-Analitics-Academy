import requests
from bs4 import BeautifulSoup


def get_html(url):
    """
    Функция получает на вход ссылку на страницу и возвращает ее html
    :param url: Ссылка на нужную страницу
    :return: Возвращает html
    """
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


def get_actual_weather(in_city):
    """
    Функция получает на вход город, в котором нужно узнать погоду.
    Выводит актуальную погоду и краткую сводку.
    :param in_city: город
    :return:
    """
    url = f'https://sinoptik.com.ru/погода-{in_city.lower()}'
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        temp = soup.find('div', class_='weather__article_main_temp').get_text(strip=True)
        description = soup.find('div', class_='weather__article_description-text').get_text(strip=True)
        summary = f'Температура воздуха сейчас {temp}\n' + description
        return summary
    except:
        print(f'Город "{in_city}" не найден. ')


def step2_umbrella():
    print('Выйдя на улицу, уточка решила посмотреть прогноз погоды...\n')
    print('Прогноз погоды на сегодня: \n', get_actual_weather(actual_city), '\n')
    if 'дождь' in get_actual_weather(actual_city):
        print('Кажется, сегодня будет дождь, так что уточка сделала правильный выбор! '
              'С зонтом гулять будет поспокойнее =)')
    else:
        print('По прогнозу погоды дождя не ожидается, но все мы знаем, что им доверять нельзя! '
              'Так что хорошо, что уточка взяла зонтик =)')


def step2_no_umbrella():
    if 'дождь' in get_actual_weather(actual_city):
        print('Что-то на улице дождливо... Похоже лучше вернуться за зонтиком.')
    else:
        print('Погода вроде хорошая, хорошо что не взяли зонтик. В баре он будет только мешать!')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    actual_city = 'Москва'
    step1()
