import math

from django.shortcuts import render
from app.models import Goods



def index(request, num=1):
    goods_list = Goods.objects.all()

    # 总页数
    total_page = math.ceil(goods_list.count() / 12)

    # [0:12]    第1页   0*12 : 1*12
    # [12:24]   第2页   1*12 : 2*12
    # [24:36]   第3页   2*12 : 3*12

    # num第几页
    num = int(num)
    goods_list = Goods.objects.all()[(num-1)*12:num*12]



    return render(request, 'index.html', context={'goods_list':goods_list, 'total_page': range(total_page)})