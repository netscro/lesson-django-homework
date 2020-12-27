from app.celery import app


@app.task(bind=True)
def task_test_2(self):
    return 1 + 1

