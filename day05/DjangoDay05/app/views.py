from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# HttpRequest
# request对象，是Django在客户端发起请求后，根据请求信息创建 request
from django.views.decorators.csrf import csrf_exempt


def index(request):
    # 请求方法
    print(request.method)

    # 请求路径
    print(request.path)

    # print(request.META)

    # get请求参数
    print(request.GET)

    # post请求参数
    print(request.POST)

    # 文件参数
    print(request.FILES)

    # cookie
    print(request.COOKIES)

    # session
    print(request.session)

    return render(request, 'index.html')


# 路径参数
# 127.0.0.1:8000/goods/4/
# 视图函数中，第一个参数必须是request，后续即路径参数(一一对应)
def goods(request, haha=1):
    temp = '第{}页 商品'.format(haha)

    return HttpResponse(temp)

def sum(request, a, b, c):
    temp = ' a:{} ,b:{} , c:{}'.format(a,b,c)
    return HttpResponse(temp)

def detail(request, name):
    temp = '{} 详情信息'.format(name)
    return HttpResponse(temp)


# get请求参数
def gettest(request):
    # QueryDict 类 字典
    # 使用这种方式，假如书写的key不存在，会抛出异常 【不建议使用】
    # name = request.GET['name']
    # age = request.GET['age']

    # 通过get方法获取 【推荐】
    name = request.GET.get('name')
    age = request.GET.get('age')
    score = request.GET.get('score')

    temp = '名字:{}, 年龄:{}, 成绩:{}'.format(name, age, score)

    return HttpResponse(temp)


# post请求参数
def postview(request):
    return render(request, 'postview.html')


@csrf_exempt
def posttet(request):
    username = request.POST.get('username')
    temp = '用户名:{}'.format(username)

    return HttpResponse(temp)



# 重定向
# 2xx 成功
# 3xx 重定向
# 4xx 客户端错误
# 5xx 服务端错误
def urltest(request):
    # return redirect('/')
    # return redirect('app:index')
    # return redirect('app:goodslist', 3)

    return HttpResponseRedirect('/')




####### 响应
# HttpResponse()
# render()
# HttpResponseRedirect()
# redirect()
# JsonResponse()

def jsontest(request):

    student = {
        'name': '张三',
        'age': 20
    }

    return JsonResponse(student)