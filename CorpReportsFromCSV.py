import csv

CORP_SUMMARY_CSV = 'Corp Summary.csv'
OUTPUT_REPORT_CSV = 'Salary report.csv'


def start():
    """
    Функция запускает меню выбора, в котором пользователь может выбирать разные опции, пока не пожелает закончить.
    """
    option = ''
    options = ['1', '2', '3', '4']
    while option != '4':
        while option not in options:
            print(
                '\nВыберите, что вы хотите сделать? \n'
                '1: Вывести иерархию департаментов️(Департамент: отделы)\n'
                '2: Вывести сводный отчёт️(Департамент: число сотрудников, "вилка" зарплат, средняя зарплата)\n'
                '3: Сохранить сводный отчёт из предыдущего пункта в виде csv-файла️\n'
                '4: Выход️\n'
            )
            print('Выберите: {}/ {}/ {}/ {}'.format(*options))
            option = str(input())

            if option == '1':
                output_report(make_hierarchy_report(CORP_SUMMARY_CSV))
                option = ''
            elif option == '2':
                output_report(make_salary_report(CORP_SUMMARY_CSV))
                option = ''
            elif option == '3':
                save_report_in_csv(make_salary_report(CORP_SUMMARY_CSV))
                option = ''
                print(f'Готово, ваш отчет сохранен с именем: {OUTPUT_REPORT_CSV}')
            else:
                print('Досвидания!')


def make_hierarchy_report(csv_file: str) -> dict:
    """
    Функция считывает csv файл и выводит в понятном виде иерархию команд,
    т.е. департамент и все команды, которые входят в него.
    :param csv_file: Строка с названием файла в формате csv, который содержит информацию по корпорации.
    :return departments: Словарь с отчетом.
    """
    departments = {}
    with open(csv_file, newline='') as data:
        reader = csv.DictReader(data, delimiter=';')
        for row in reader:
            if row['Департамент'] not in departments.keys():
                departments[(row['Департамент'])] = []
            departments[(row['Департамент'])].append(row['Отдел'])

    keys = list(departments.keys())
    values = list(departments.values())
    for i in range(len(keys)):
        departments[keys[i]] = list(set(values[i]))

    return departments


def make_salary_report(csv_file: str) -> dict:
    """
    Функция считывает csv файл и выводит сводный отчёт по департаментам в виде словаря:
    Департамент: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату.
    :param csv_file: Строка с названием файла в формате csv, который содержит информацию по корпорации.
    :return report: Словарь с отчетностью
    """
    report = {}

    with open(csv_file, newline='') as data:
        reader = csv.DictReader(data, delimiter=';')
        for row in reader:
            if row['Департамент'] not in report.keys():
                # number_of_workers, salary_min, salary_max, salary_avg
                report[(row['Департамент'])] = [1, int(row['Оклад']), int(row['Оклад']), int(row['Оклад'])]
            else:
                report[(row['Департамент'])][0] += 1
                if int(report[(row['Департамент'])][1]) > int(row['Оклад']):
                    report[(row['Департамент'])][1] = int(row['Оклад'])
                if int(report[(row['Департамент'])][2]) < int(row['Оклад']):
                    report[(row['Департамент'])][2] = int(row['Оклад'])
                report[(row['Департамент'])][3] += int(row['Оклад'])

        for dep in report.keys():
            report[dep][3] = int(report[dep][3]) / int(report[dep][0])

    return report


def output_report(report: dict):
    """
    Красиво распечатывает словарь.
    :param report: Словарь с отчетом
    """
    print('\n')
    print('----------------------------------------------------------')
    for dep, divs in report.items():
        print(f'\n{dep.title()}:', end=' ')
        for div in divs:
            print(div, end=', ')
    print('\n')
    print('----------------------------------------------------------')


def save_report_in_csv(report: dict):
    """
    Функция принимает на входе словарь с финансовым отчетом и записывает его в csv файл.
    :param report: Словарь с данными в формате: {'Департамент': ['Число сотрудников', 'Минимальная зарплата',
    'Максимальная зарплата', 'Средняя зарплата']}
    """
    col_names = ['Департамент', 'Число сотрудников', 'Минимальная зарплата', 'Максимальная зарплата',
                 'Средняя зарплата']
    departments = []
    for key in report.keys():
        departments.append(key)
    dict_data = []
    for i in range(len(departments)):
        dict_data.append(dict([(col_names[0], departments[i]),
                               (col_names[1], report[departments[i]][0]),
                               (col_names[2], report[departments[i]][1]),
                               (col_names[3], report[departments[i]][2]),
                               (col_names[4], report[departments[i]][3])]))

    with open(OUTPUT_REPORT_CSV, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=col_names)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)


if __name__ == '__main__':
    start()
