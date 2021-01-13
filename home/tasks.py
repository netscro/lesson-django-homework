import requests
from celery import chain, shared_task

from home.models import Currency


@shared_task
def privatbank_currency():
    currency = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    return currency.json()


@shared_task
def currency_model_save(currency):
    currency_model = Currency()
    for new_currency in currency:
        for save_currency in new_currency:
            currency_model.ccy = save_currency['ccy']
            currency_model.base_ccy = save_currency['base_ccy']
            currency_model.buy = save_currency['buy']
            currency_model.sale = save_currency['sale']
        currency_model.save()


@shared_task
def privatbank_task():
    return chain(privatbank_currency.s(), currency_model_save.s())()
