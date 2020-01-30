from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request, *args, **kwargs):
    data = request.GET
    print("data====", data)
    return HttpResponse("这个是首页--app01")


def article(request, aid):
    return HttpResponse('这是第{}篇文章'.format(aid))


def students(request):
    # get_data = request.GET
    # get_list = request.GET.getlist("id")
    post_data = request.POST
    method = request.method
    # print("get_data===", get_data)
    # print("get_list====", get_list)
    print("post_data====", post_data)
    print("method===", method)

    return HttpResponse('学生列表----app01')


def student(request, stu_id):
    import json
    body_data = request.body
    json_data = ""
    if body_data:
        json_data = json.loads(body_data)
    method = request.method
    print("stu_id====", stu_id)
    print("body_data====", body_data)
    print("json_data====", json_data)
    print("method===", method)
    return HttpResponse('这是id为{}的学生'.format(stu_id))


def test_url(request):
    return HttpResponse('url测试--app01')
