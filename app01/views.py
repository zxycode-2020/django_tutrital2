from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("这个是首页--app01")


def article(request, aid):
    return HttpResponse('这是第{}篇文章'.format(aid))


def test_url(request):
    return HttpResponse('url测试--app01')
