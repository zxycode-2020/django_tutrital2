from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    print(request.method)
    print(request.POST)
    return HttpResponse("这个是首页--app01")


def article(request, aid):
    return HttpResponse('文章页ok--app01')


def test_url(request):
    return HttpResponse('url测试--app01')
