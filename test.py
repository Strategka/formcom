import pprint

import requests as req


URL = 'http://localhost:8000/get_form'


def check_supported_type(type, data):
    print(f'Тип "{type}":')
    print(f"Данные формы - {data}")
    print(f'Результат - {req.post(URL, data=data).text}')
    print()

def check_supported_types():
    type_data = {
            'Дата': {
                'right_format_date1': '1799-06-06', 
                'right_format_date2': '23.01.1832',
                'wrong_format_date3': '11/11/11',
            },
            'Номер телефона': {
                'right_format_phone1': '+7 800 333 44 34', 
                'wrong_format_phone2': '8 (000) 00-00-00',
            },
            'Электронная почта': {
                'right_format_email1': 'nevsky@gmail.com', 
                'wrong_format_email2': 'kuritsin@ mail.ru',
            },
            'Текст': {
                'text_f': 'Текст тЕкст теКст текСт тексТ', 
            }
    }

    for type, data in type_data.items():
        check_supported_type(type, data)


if __name__ == '__main__':
    test_data = [
            {
                'user_email': 'nn@leadhit.ru', 
                'user_password': 'MyPassWordHandsOff!',
            },
            {
                'user_name': 'Виталий Цаль', 
                'user_email': 'evilarthas@gmail.com', 
                'birth_date': '1990-11-19',
                'phone_number': '+7 777 777 77 77',
                'user_password': 'Velichaishiy1990',
            },
            {
                'user_login': 'test', 
                'comment_date': '11.11.2011', 
                'comment_text': 'Text', 
            },
            {
                'user_login': 'test', 
                'comment_data': '11.11.2011', 
                'comment_text': 'Text', 
            },
    ]

    pp = pprint.PrettyPrinter(indent=4)

    for data in test_data:
        print('Ищем форму по:')
        pp.pprint(data)
        print('Результат:')
        pp.pprint(req.post(URL, data=data).json())
        print()
