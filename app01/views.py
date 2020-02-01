from django.shortcuts import render, HttpResponse
from app01.models import Class, Student

# Create your views here.

# def index(request, *args, **kwargs):
#     data = request.GET
#     print("data====", data)
#     return HttpResponse("这个是首页--app01")


def index(request):
    # print(request.method)
    # print(request.path)
    # print(request.GET)
    # print(request.POST)
    # print(request.s)

    return render(request, 'app01/index.html')


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


def args(request):
    # 获取url传过来的name和age的值
    name = request.GET.get('name')
    age = request.GET.get('age')
    # 制作一个字典，传递给对应的模板文件
    context = {
        "name": name,
        "age": age
    }
    return render(request, 'app01/args.html', context)


def reg(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print('username====', username)
        print('password====', password)

        return HttpResponse('登录成功')
    elif request.method == 'GET':
        return render(request, 'app01/reg.html')
    else:
        return HttpResponse('fuck off')


class Human:
    h_name = "人类"
    h_age = 100000

    def sayhellow(self):
        return '沙扬娜拉'


def xuanran(request):
    title = "标题"
    ls = ['python', 'java', 'php']
    info = {
        'name': '啦啦啦',
        'age': 20
    }
    h1 = Human()
    context = {
        'title': title,
        'language': ls,
        'info': info,
        'h1': h1
    }
    return render(request, 'app01/xuanran.html', context)


def orm_test(request):
    """
    增加操作
    """
    # 新增一个名字为1901的一个班级,create是新增方法，里面可以接受多个字段参数
    # Class.objects.create(name="1901")
    # 同时新增一个学生和班级操作
    # 新增一个班级名称为1903的班级，返回一个班级实例
    # cls_instance = Class.objects.get(name="1903")
    # stu_info左边的key要和Student模型字段对应上，因为cls是外键，所以要对应一个班级的实例
    # stu_info = {
    #     "name":"XIAOmei",
    #     "age": "24",
    #     "score":"88",
    #     "email": "1333@qq.com",
    #     "introduce": "假如你是xiaomei",
    #     "cls": cls_instance
    # }
    # Student.objects.create(**stu_info)
    """
    修改操作
    """
    # 将名字为1901的班级名称改为1901_xiu，filter为过滤，支持多个参数，update是更新方法，支持多个参数
    # Class.objects.filter(name="1901").update(name="1901_xiu")
    """
    删除操作
    """
    # 将名字为1901_xiu的班级删除掉，delete是删除方法
    # Class.objects.filter(name="1901_xiu").delete()
