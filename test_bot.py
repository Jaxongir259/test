from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index_course(request):
    # return render(request, 'index.html')
    return HttpResponse('Page with courses')

print('hi')
