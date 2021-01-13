import requests
from celery import chain, shared_task

from home.models import Currency


@shared_task
def privatbank_currency():
    currency = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    return currency.json()


@shared_task
def currency_model_save(currency):
    for new_currency in currency:
        currency_model = Currency()
        currency_model.ccy = new_currency['ccy']
        currency_model.base_ccy = new_currency['base_ccy']
        currency_model.buy = new_currency['buy']
        currency_model.sale = new_currency['sale']
        currency_model.save()


@shared_task
def privatbank_task():
    return chain(privatbank_currency.s(), currency_model_save.s())()
