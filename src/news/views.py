from django.shortcuts import render
from django.http import JsonResponse
from .tasks import log_message, add
from .models import News


def task_status(request):
    result = log_message.delay()
    return JsonResponse({'status': 'Task has been triggered', 'task_id': result.id})


def task_view(request):
    x, y = 10, 20  
    res = add.delay(x, y)
    context = {'res': res}
    return render(request, 'tasks/tasks.html', context)


def news_home(request):
    articles_list = News.objects.all()
    context = {
        "articles": articles_list
    }
    return render(request, "news/articles.html", context)
