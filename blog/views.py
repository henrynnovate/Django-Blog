from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'title': 'Post 1',
        'author': 'John Doe',
        'content': 'First post content',
        'date_posted': 'August 15, 2021'
    },
    {
        'title': 'Post 2',
        'author': 'Jane Doe',
        'content': 'Second post content',
        'date_posted': 'August 17, 2021'
    },
    {
        'title': 'Post 3',
        'author': 'Mike Doe',
        'content': 'Third post content',
        'date_posted': 'August 19, 2021'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

