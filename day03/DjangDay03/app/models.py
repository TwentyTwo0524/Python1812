from django.db import models
from django.db.models import Manager

# 自定义管理器
class AnimalManager(Manager):
    # 重写
    def all(self):
        return super().all().exclude(is_del=True)

class Animal(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    # 逻辑删除
    is_del = models.BooleanField(default=False)

    # 如果没有自定义，系统默认 objects
    # objects = models.Manager()
    myObjects = AnimalManager()



#### 学习目标s: 明确不同的关系，不同的关系是如何实现的，数据删除时要怎么处理
## 一对一
# 人 和 身份证 【一个人 对应 一个身份证（身份证号）】
# 主表
class Person(models.Model):
    p_name = models.CharField(max_length=40)


# 身份证
# 从表(声明关系)
'''
create table app_idcard
(
  id          int auto_increment
    primary key,
  i_no        varchar(40)  not null,
  i_sex       int          not null,
  i_addr      varchar(100) not null,
  i_person_id int          not null,
  constraint i_person_id
  unique (i_person_id),
  constraint app_idcard_i_person_id_c24e2938_fk_app_person_id
  foreign key (i_person_id) references app_person (id)
);


主表数据删除， 关联的从表数据，默认是会被删除!
'''
class IDCard(models.Model):
    # 身份证号
    i_no = models.CharField(max_length=40)
    # 性别 (1男，2女)
    i_sex = models.IntegerField()
    # 地址
    i_addr = models.CharField(max_length=100)

    # 声明关系 [这个身份证是属于哪个人的]
    i_person = models.OneToOneField(Person)


    # 删除模式
    # 默认 models.CASCADE 模式
    # 主数据删除，有级联数据(从表)，级联数据也会被删除
    # 主数据删除，没有级联数据(从表)，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.CASCADE)

    # models.PROTECT 保护模式
    # 主表数据删除，有级联数据，抛出 'ProtectedError'
    # 主表数据删，没有级联数据，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.PROTECT)

    # models.SET_NULL 置空模式
    # 主表数据删除，有级联数据，将级联数据中关系字段设置为null
    # 主表数据删，没有级联数据，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.SET_NULL, null=True)

    # models.SET_DEFAULT 设置默认值模式
    # 主表数据删除，有级联数据，将级联数据中关系字段设置为 默认值
    # 主表数据删，没有级联数据，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.SET_DEFAULT, default=1)


## 一对多
# 一个班级 对应 多个学生
# 主表
class Grade(models.Model):
    g_name = models.CharField(max_length=40)

# 从表(声明关系)
'''
create table app_student
(
  id         int auto_increment
    primary key,
  s_name     varchar(40) not null,
  s_age      int         not null,
  s_grade_id int         not null,
  constraint app_student_s_grade_id_129e1bc3_fk_app_grade_id
  foreign key (s_grade_id) references app_grade (id)
);
'''
class Student(models.Model):
    s_name = models.CharField(max_length=40)
    s_age = models.IntegerField()

    # 声明关系 (这学生 属于 哪个班)
    s_grade = models.ForeignKey(Grade, models.SET_NULL, null=True)