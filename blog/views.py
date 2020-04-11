from django.shortcuts import render, get_object_or_404
from .models import blog_Project

# Create your views here.
def all_blogs(request):
    blog_Projects = blog_Project.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blog_Projects':blog_Projects})

def detail(request, blog_id):
    one_Blog = get_object_or_404(blog_Project, pk=blog_id)
    print (one_Blog)
    return render(request, 'blog/detail.html', {'one_Blog':one_Blog})
    #return render(request, 'blog/detail.html', {'id':blog_id})
