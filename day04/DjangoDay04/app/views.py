from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def basedemo(request):

    context = { # key:value
        'name': 'Hello World!',
        'age': 18,
        'score': [70,89,90],
        'username': 'root',   # root 超级管理员,
        'scoredir': [
            {'语文': 90},
            {'数学': 98},
            {'英语': 78}
        ],
        'names': ['张三', '李四', '王五', '赵柳']
    }

    return render(request, 'basedemo.html', context=context)


def includedemo(request):

    goods_list = ['ipad', 'iphone', 'mac', 'ipod']

    return render(request, 'includedemo.html', context={'goods_list':goods_list})


def home(request):
    return render(request, 'home.html')


def cart(request):
    return render(request, 'cart.html')


def mine(request):

    return render(request, 'mine.html')