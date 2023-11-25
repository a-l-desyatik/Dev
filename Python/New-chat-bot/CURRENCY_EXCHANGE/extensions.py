import requests
from config import keys

class APIException(Exception):
    pass

class CurrencyExchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        quote = quote.lower()
        base = base.lower()
        
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangerate-api.com/v4/latest/{quote_ticker}')
        if r.status_code != 200:
            raise APIException('Ошибка API сервиса')

        data = r.json()
        if 'error' in data:
            raise APIException(data['error'])

        rate = data['rates'].get(base_ticker)
        if not rate:
            raise APIException(f'Не удалось найти курс для {base_ticker}')

        total_base = rate * amount
        return total_base