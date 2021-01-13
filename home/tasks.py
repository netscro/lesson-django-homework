from celery import chain, shared_task

from app.celery import app


@shared_task
def privatbank_currency(*args):
    return sum(args)


@shared_task
def privatbank_task():
    return chain(privatbank_currency.s(2, 2), privatbank_currency.s(7, 7))()
