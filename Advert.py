import json
import keyword


class AdvertAttributes:
    def __init__(self, attributes: dict):
        self.attributes = attributes
        for key, value in self.attributes.items():
            if keyword.iskeyword(key):
                key = f'{key}_'
            if key == 'price':
                self.price = value
            if isinstance(value, dict):
                value = AdvertAttributes(value)
            self.__dict__[key] = value


class ColorizeMixin:
    def __repr__(self):
        text = super().__repr__()
        return f'\033[0;{self.repr_color_code}m{text} \033[0;0m'


class BaseAdvert:
    def __repr__(self):
        return f'{self.title} || {self.price} ₽'


class Advert(ColorizeMixin, AdvertAttributes, BaseAdvert):
    repr_color_code = 33  # Yellow

    def __init__(self, attributes):
        super().__init__(attributes)
        self.price
        if not hasattr(self, 'title'):
            raise ValueError('Tittle not setted')


    @property
    def price(self):
        if not hasattr(self, 'price_'):
            setattr(self, 'price_', 0)
        return self.price_

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Price must be int or float')
        elif value < 0:
            raise ValueError('Price must be >= 0')
        self.price_ = value


if __name__ == '__main__':
    ex1 = """{ 
        "title": "Drag X", 
        "location": { 
            "address": "город Москва, Лесная, 7", 
            "metro_stations": ["Белорусская"] 
            } 
        }"""

    ex2 = """{   
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

    ad1 = Advert(json.loads(ex3))
    print(ad1.title)
    print(ad1.price)
    print(ad1.class_)
    print(ad1.location.address)
    print(ad1)

