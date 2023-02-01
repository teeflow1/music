from django.shortcuts import render

# Create your views here.
def music_app (request):
    return render(request, 'index.html', {})
