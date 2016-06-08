from celery import shared_task

@shared_task
def task():
    print 1+1
    return "Done"