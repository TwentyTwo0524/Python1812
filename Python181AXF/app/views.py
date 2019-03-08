import random

from django.shortcuts import render
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods


# Create your views here.
def home(request):
    # 轮播图数据
    wheels = Wheel.objects.all()

    # 导航
    navs = Nav.objects.all()

    # 每日必购
    mustbuys = Mustbuy.objects.all()

    # 商品部分
    shops = Shop.objects.all()
    shophead = shops[0]
    shoptabs = shops[1:3]
    shopclass_list = shops[3:7]
    shopcommends = shops[7:11]

    # 商品列表
    mainshows = Mainshow.objects.all()

    response_dir = {
        'wheels':wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead,
        'shoptabs': shoptabs,
        'shopclass_list': shopclass_list,
        'shopcommends': shopcommends,
        'mainshows': mainshows
    }

    return render(request, 'home/home.html', context=response_dir)



# def market(request, categoryid=104749):
def market(request):
    # 分类信息
    foodtypes = Foodtype.objects.all()


    # 商品信息
    # goods_list = Goods.objects.all()[0:5]
    # 默认打开页面  热销榜
    # 点击左侧分类，即显示对应分类 商品信息  【传参数categoryid】
    # goods_list = Goods.objects.filter(categoryid=categoryid)

    # 客户端 需要记录 点击的分类下标 【cookies， 会自动携带】
    index = int(request.COOKIES.get('index', '0'))
    # 根据index 获取 对应的 分类ID
    categoryid = foodtypes[index].typeid
    # 根据 分类ID 获取对应分类信息
    goods_list = Goods.objects.filter(categoryid=categoryid)

    # 获取子类信息
    childtypenames = foodtypes[index].childtypenames
    # 存储子类信息 列表
    childtype_list = []
    # 将对应的子类拆分出来
    for item in childtypenames.split('#'):
        # item  >> 全部分类:0
        # item  >> 子类名称: 子类ID
        item_arr = item.split(':')
        temp_dir = {
            'name': item_arr[0],
            'id': item_arr[1]
        }

        childtype_list.append(temp_dir)


    response_dir = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'childtype_list': childtype_list
    }


    return render(request, 'market/market.html', context=response_dir)


def cart(request):
    temp = random.randrange(4,63)
    return render(request, 'cart/cart.html', context={'temp':temp})


def mine(request):
    return render(request, 'mine/mine.html')