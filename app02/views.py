from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    print(request.method)
    print(request.POST)
    return HttpResponse("这个是首页--app02")


def article(request, aid):
    return HttpResponse('文章页ok--app02')


def test_url(request):
    return HttpResponse('url测试--app02')


def caijing(request):
    return render(request, 'app02/caijing.html')


def yule(request):
    return render(request, 'app02/yule.html')
