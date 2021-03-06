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
    """
        查询操作
        """
    # 查询单条,get返回实例，如果查询结果没有回报错，
    # filter查询返回的结果是多个实例的列表,
    # instance = Student.objects.get(pk=1)
    # instance = Student.objects.filter(pk=1).first()

    # 查询多条,返回queryset类型(多个查询结果实例的列表) 可以被迭代
    # queryset = Student.objects.all() #
    # for stu in queryset:
    # 学生的姓名 学生的年龄 学生的分数
    #     print(stu.name,stu.age,stu.score)

    # 对查询集结果进行切片，取第0个到第4个，和列表的切片一样
    # queryset = Student.objects.filter().all()[:5] # limit 语句
    # print(queryset.query) # 返回执行的sql语句

    # 精准查找 两条语句作用一样，查询姓名位小美的学生，结果返回查询集
    # queryset = Student.objects.filter(name='小美')
    # queryset = Student.objects.filter(name__exact='小美')

    # 忽略大小写
    # queryset = Student.objects.filter(name__iexact='xiaomei')

    # 模糊查询
    # queryset = Student.objects.filter(name__contains='xiao') # 不忽略大小写
    # queryset = Student.objects.filter(name__icontains='xiao') # 忽略大小写

    # 正则匹配法
    # queryset = Student.objects.filter(name__regex='^x')
    # queryset = Student.objects.filter(name__iregex='^x')

    # 大于 小于
    # queryset = Student.objects.filter(age__gt=17, age__lt=19)

    # in 一个集合中的所有
    # queryset = Student.objects.filter(age__in=(18,17,16))

    # queryset = Student.objects.all().order_by('age') 升序
    # queryset = Student.objects.all().order_by('-age') #升序
    # queryset = Student.objects.all().order_by('-age','id') #升序
    # for stu in queryset:
    #     print stu.age,stu.id

    # 指定字段查询
    # 第一种
    # queryset = Student.objects.values('name','age').all()

    # 第二种
    # queryset = Student.objects.values_list('name','age','score').all()

    # 连表查询
    # 第一种
    # queryset = Student.objects.all()
    # for stu in queryset:
    #     print stu.name,stu.cls.id,stu.cls.name

    # 第二种 : 牛逼的双下划线(跨表)，可以用多个双下划线跨多张表
    # 语句功能是查询学生表中所有学生的姓名和学生所在班级的名称
    # cls__name 是cls双下划线name,cls 是Student中的cls字段，name是班级表中的name字段
    # queryset = Student.objects.values('name','cls__name').all()

    # 查询一个班级所有学生，执行两次sql语句
    # cls1 = Class.objects.get(name='1701')
    # queryset = Student.objects.filter(cls=cls1)

    # 查询一个班级所有学生，执行一次sql语句
    # queryset = models.Student.objects.filter(cls__name='1903').all().values('name','cls__name')

    # 查询一个班级所有学生，起始表从班级表开始查询,反向查询
    # stu_cls 是学生表中外键的别名
    # queryset = Class.objects.get(name='1903').stu_cls.all()

    # 按照分数查询 大于90分
    # queryset = Student.objects.filter(score__gt=90).all()

    return HttpResponse('数据库操作成功')


def post_cls(request):
    Class.objects.create(name="1901")
    return HttpResponse('数据库操作成功')


def get_cls(request):
    res = Class.objects.all().values()
    print(res)
    return HttpResponse(res)
