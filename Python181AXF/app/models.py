from django.db import models


# 基础类
class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

# 轮播图　模型类
# insert into axf_wheel(img,name,trackid)
class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'


# 导航　模型类
class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'


# 每日必购
class Mustbuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'


# 部分商品
class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'
