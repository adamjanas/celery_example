from django.shortcuts import render
from .tasks import go_to_sleep


def msg(request):
    task = go_to_sleep.delay(1)
    return render(request, 'base.html', {'task_id': task.task_id})

