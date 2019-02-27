import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Animal, Person, IDCard, Grade, Student


def index(request):
    return render(request, 'index.html')


def animal(request):
    return render(request, 'animal.html')


def addanimal(request):
    animal = Animal()
    animal.name = '阿猫阿狗' + str(random.randrange(1,10000))
    animal.age = random.randrange(1,10)
    animal.save()

    return HttpResponse('添加数据成功')


def selectanimal(request):
    # 获取所有数据(没有被逻辑删除的)
    # animals = Animal.objects.all()

    # 逻辑删除的要去除掉
    # animals = Animal.objects.exclude(is_del=True)

    animals = Animal.myObjects.all()

    animal_str = ''
    for item in animals:
        animal_str += '<p> {}-{}-{} </p>'.format(item.id,item.name,item.age)

    return HttpResponse(animal_str)


def deleteanimal(request):
    animal = Animal.myObjects.last()
    animal.delete()

    return HttpResponse('删除数据成功')


def updateanimal(request):
    animal = Animal.myObjects.last()
    animal.name = '大花猫'
    animal.save()

    return HttpResponse('更新数据成功')


def onetoone(request):
    return render(request, 'onetoone.html')


def addperson(request):
    person = Person()
    person.p_name = 'Atom-' + str(random.randrange(1,100))
    person.save()

    return render(request, 'addperson.html')


def bindcard(request):
    card = IDCard()
    card.i_no = '441622{}{}{}{}'.format(random.randrange(1900,2020), random.randrange(1,13), random.randrange(1,30), random.randrange(1000,10000))
    card.i_sex = random.randrange(1,3)
    card.i_addr = '大学城创客小镇3楼 Python1812 座位号:' + str(random.randrange(1,70))

    # 谁的身份证？
    person = Person.objects.last()
    card.i_person = person

    card.save()

    return HttpResponse('身份证绑定成功')


def deleteperson(request):
    person = Person.objects.last()
    person.delete()

    return HttpResponse('删除人成功')


def deletecard(request):
    card = IDCard.objects.last()
    card.delete()

    return HttpResponse('身份证删除成功')


def getpersoncard(request):
    person = Person.objects.last()

    # 主表 获取 从表信息 (模型类没有对应的属性，隐式访问，模型类小写)
    card = person.idcard

    if card.i_sex == 1:
        temp = '男'
    else:
        temp = '女'

    response_str = '姓名:{}, 性别:{}, 身份证号:{}, 家庭住址:{}'.format(person.p_name, temp, card.i_no, card.i_addr)

    return HttpResponse(response_str)


def getcardperson(request):
    card = IDCard.objects.last()

    # 从表 获取 主表信息 (模型类有对应的属性，显式访问)
    person = card.i_person

    if card.i_sex == 1:
        temp = '男'
    else:
        temp = '女'

    response_str = '姓名:{}, 性别:{}, 身份证号:{}, 家庭住址:{}'.format(person.p_name, temp, card.i_no, card.i_addr)

    return HttpResponse(response_str)


def foreignkey(request):
    return render(request, 'foreignkey.html')


#############################################
def addgrade(request):
    grade = Grade()

    arr = ['Python', 'iOS', '测试', 'UI', 'Android']
    temp = random.randrange(0, len(arr))

    grade.g_name = arr[temp] + '-19' + str(random.randrange(10,100))

    grade.save()

    return render(request, 'addgrade.html')


def addstudent(request):
    stu = Student()
    arr = ['张三', '李四', '王五', '赵柳', '田七']
    temp = random.randrange(0, len(arr))
    stu.s_name = arr[temp] + '-' + str(random.randrange(10, 100))
    stu.s_age = random.randrange(18,38)

    # 班级
    grade = Grade.objects.last()
    stu.s_grade = grade

    stu.save()

    return HttpResponse('添加学生成功')


def delgrade(request):
    grade = Grade.objects.last()
    grade.delete()

    return HttpResponse('删除班级成功')