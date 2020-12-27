from app.celery import app


@app.task()
def task_test_2():
    return 1 + 1
