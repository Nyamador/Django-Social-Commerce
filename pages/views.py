from django.shortcuts import render
from django.views.generic import TemplateView
from feed.models import Activity


class HomePageView(TemplateView):
    template_name = 'pages/index.html'


def feed(request):
    feed = Activity.objects.get_user_timeline(request.user.id)
    context = {
        'feed' : feed,
    }
    return render(request, 'pages/feed.html', context)