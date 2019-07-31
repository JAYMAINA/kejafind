from django.shortcuts import render, get_object_or_404
from .models import Posts

def home(request):
    io = Posts.objects
    return render(request, 'home.html',{'io': io})
def detail(request, blog_id):
    nu = get_object_or_404(Posts, pk=blog_id)
    return render(request, 'detail.html', {'blog':nu})
