import json
import keyword


class AdvertAttributes:
    def __init__(self, attributes: dict):
        self.attributes = attributes
        for key, value in self.attributes.items():
            if keyword.iskeyword(key):
                key = f'{key}_'
            if isinstance(value, dict):
                self.__setattr__(key, AdvertAttributes(value))
            else:
                self.__setattr__(key, value)

        if not self.attributes.get('price', 0):
            self.__dict__['price'] = 0
        elif self.attributes['price'] < 0:
            raise ValueError('Price must be >= 0')

    def __setattr__(self, key, value):
        self.__dict__[key] = value


class JsonData:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def get_python_object(self) -> dict:
        return json.loads(self.raw_data)


class ColorizeMixin:
    def __repr__(self):
        return f'\033[0;{self.repr_color_code}m{self.title} | {self.price} ₽\033[0;0m'


class Advert(ColorizeMixin, AdvertAttributes):
    repr_color_code = 33  # Yellow

    def __init__(self, attributes):
        super().__init__(attributes)

    def __repr__(self):
        return f'\033[0;{self.repr_color_code}m{self.title} | {self.price} ₽\033[0;0m'


if __name__ == '__main__':
    ex1 = """{ 
        "title": "Drag X", 
        "price": 3490, 
        "location": { 
            "address": "город Москва, Лесная, 7", 
            "metro_stations": ["Белорусская"] 
            } 
        }"""

    ex2 = """{ 
        "title": "python",  
        "location": { 
            "address": "город Москва, Лесная, 7", 
            "metro_stations": ["Белорусская"] 
            } 
        }"""

    ex3 = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs", 
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            } 
        }"""

    ad1 = Advert(JsonData(ex3).get_python_object())
    print(ad1.title)
    print(ad1.price)
    print(ad1.class_)
    print(ad1.location.address)
    print(ad1)
