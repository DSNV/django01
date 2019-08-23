import hashlib
from django.db import models
# Create your models here.
from django.utils import timezone


#1普通用户表
class Users(models.Model):
    u_id = models.AutoField(primary_key=True,verbose_name='编号')#编号
    username = models.CharField(max_length=100,unique=True,verbose_name='用户名')#用户姓名
    password = models.CharField(max_length=128,verbose_name='用户密码')#用户密码
    sex_type = ((0,'男'),(1,'女'))#性别枚举栏
    sex = models.BooleanField(default=0,choices=sex_type,verbose_name='性别')#性别
    age = models.IntegerField(default=0,verbose_name='年龄')#年龄
    u_address = models.CharField(max_length=500,null=True,verbose_name='用户地址')#用户地址
    email = models.EmailField(verbose_name='用户邮箱')#用户邮箱
    phonenum = models.CharField(max_length=11,null=True,verbose_name='手机号码')#用户手机号码
    degree = models.CharField(max_length=20,null=True,verbose_name='学历')#学历
    collage = models.CharField(max_length=50,null=True,verbose_name='毕业学校')#毕业学校
    u_exper = ((0,'没有经验'),(3,'1-3年'),(5,'3-5年'),(6,'五年以上'))
    exper = models.IntegerField(default=0,choices=u_exper,verbose_name='工作经验')#工作经验
    # wantedjob = models.ForeignKey()
    u_job = models.CharField(max_length=50,null=True,verbose_name='意向工作')#意向工作
    u_regtime = models.DateTimeField(default=timezone.now,verbose_name='注册时间')#注册时间
    STATUS_CHOICES = ((0, '普通用户'),(1, '公司用户'),)
    identity = models.IntegerField(default=0,verbose_name='身份类型',choices=STATUS_CHOICES)#用户类型，默认普通用户为0

    class Meta:
        db_table = 'user'
        verbose_name_plural = '[01]用户列表'

    def __str__(self):
        return self.username

    # @property
    # def password(self):
    #     return self.password
    # @password.setter
    # def password(self,value):
    #     self.password = hashlib.sha1(value.encode('utf8')).hexdigest()


#2创始人表
class Founders(models.Model):
    f_name = models.CharField(max_length=20,verbose_name='姓名')#姓名
    f_position = models.CharField(max_length=20,null=True,verbose_name='现任职位')#职位
    f_photo = models.ImageField(null=True,verbose_name='照片')#照片
    f_blog = models.CharField(max_length=50, null=True,verbose_name='微博')#微博
    f_introduction = models.CharField(max_length=500, null=True,verbose_name="个人简介")#简介
    f_uid = models.IntegerField(default=1,verbose_name='身份编号')
    # company = models.ForeignKey(Companies,on_delete=models.CASCADE,db_column='company',verbose_name='公司名称')

    def __str__(self):
        return self.f_name

    class Meta:
        db_table = 'founders'
        verbose_name_plural = '[05]创始人'


#3公司表
class Companies(models.Model):
    c_id = models.AutoField(primary_key=True,verbose_name='公司编号')                                                   #公司编号
    c_name = models.CharField(max_length=100,null=True,verbose_name='公司名称')                                         #公司名称
    logo = models.ImageField(null=True,verbose_name='LOGO')                                                             #公司logo
    slogan = models.CharField(max_length=50,null=True,verbose_name='SLOGAN')                                            #口号，宣传语
    c_infor = models.CharField(max_length=1000,null=True,verbose_name='详细信息')                                       #公司详细信息
    c_address = models.CharField(max_length=100,null=True,verbose_name='公司地址')                                      #公司地址
    founder = models.ForeignKey(Founders,on_delete=models.CASCADE,db_column='f_name',null=True,verbose_name='创始人')   #创始人
    # product = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product')                                 #公司产品
    area = models.CharField(max_length=50,null=True,verbose_name='所属领域')                                            #所属领域
    contacts = models.CharField(max_length=20,null=True,verbose_name='联系人')                                          #联系人
    cont_phone = models.CharField(max_length=20,null=True,verbose_name='联系人电话')                                    #联系人电话
    cont_mail = models.EmailField(null=True,verbose_name='联系人邮箱')                                                  #联系人邮箱
    c_phone = models.CharField(max_length=20,null=True,verbose_name='公司电话')                                         #公司电话
    c_email = models.EmailField(null=True,verbose_name='公司邮箱')                                                      #公司邮箱
    web = models.CharField(max_length=50,null=True,verbose_name='公司官网')                                             #公司官网
    s_type = ((0,'无信息'),(1,'10人以下'),(2,'10-50人'),(3,'50-100人'),(4,('100人以上')))
    size = models.IntegerField(default=0,choices=s_type,verbose_name='公司规模')                                        #公司规模
    dev_type = ((0,'未融资'),(1,'天使轮'),(2,'Pre_A轮'),(3,'A轮'),(4,'B轮'),(5,'C轮'),(6,'D轮及以上'),(7,'已上市'))
    develop = models.IntegerField(default=0,choices=dev_type,verbose_name='发展阶段')                                   #发展阶段
    invest = models.CharField(max_length=100,null=True,verbose_name='投资机构')                                         #投资机构
    identity = models.IntegerField(default=1,verbose_name='身份类型')                                                   #用户类型，公司默认为1
    userid = models.IntegerField(default=0,null=True,verbose_name='用户编号')
    comintroduce = models.CharField(max_length=10000,null=True,verbose_name='公司介绍')                                 #公司介绍

    def __str__(self):
        return self.c_name

    class Meta:
        db_table = 'companies'
        verbose_name_plural = '[03]公司列表'


#4公司产品表
class Product(models.Model):
    p_name = models.CharField(max_length=50,null=True,verbose_name='产品名称')
    p_web = models.CharField(max_length=30,null=True,verbose_name='产品网址')
    p_intr = models.CharField(max_length=500,null=True,verbose_name='产品介绍')
    company = models.ForeignKey(Companies,on_delete= models.CASCADE,db_column='p_id',verbose_name='所属公司')

    def __str__(self):
        return self.p_name

    class Meta:
        db_table = 'product'
        verbose_name_plural = '[04]公司产品'


#5简历表
class Resumes(models.Model):
    resume = models.FileField(null=True,verbose_name='简历文件')#简历文件
    owner = models.ForeignKey(Users,on_delete=models.CASCADE,db_column='u_id',verbose_name='用户')

    def __str__(self):
        return self.owner.username

    class Meta:
        db_table = 'resumes'
        verbose_name_plural = '[10]简历文件'


#6在线简历表
class ResumeOnline(models.Model):
    myjob= models.CharField(max_length=500,null=True,verbose_name='期望工作')                                       #期望工作
    myexp = models.CharField(max_length=500,null=True,verbose_name='工作经验')                                      #工作经历
    myobj = models.CharField(max_length=500,null=True,verbose_name='项目经验')                                      #项目经验
    myedu = models.CharField(max_length=500,null=True,verbose_name='教育背景')                                      #教育背景
    myinfor = models.CharField(max_length=500,null=True,verbose_name='自我描述')                                    #自我描述
    display = models.CharField(max_length=500,null=True,verbose_name='作品展示')                                    #作品展示
    owner = models.ForeignKey(Users,on_delete=models.CASCADE,db_column='owner',verbose_name='用户')             #外键关联Users

    def __str__(self):
        return self.owner.username

    class Meta:
        db_table = 'resume_ol'
        verbose_name_plural = '[09]在线简历'


#14收到的简历
class GetResume(models.Model):
    # company = models.ForeignKey(Companies,on_delete=models.CASCADE,verbose_name='接收公司')
    resume = models.ForeignKey(ResumeOnline,on_delete=models.CASCADE,verbose_name='简历详情')
    owner = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='简历拥有着')
    s_type = ((0,'待处理的简历'),(1,'已通知面试简历'),(2,'不合适的简历'))
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.owner.username

    class Meta:
        db_table='getresumes'
#7一级信息表
class Postionsone(models.Model):
    o_pid = models.AutoField(primary_key=True,verbose_name='编号') #一级编号
    pname = models.CharField(max_length=50,verbose_name='领域名称') # 领域名称
    shang = models.IntegerField(default=0,verbose_name='上级领域')  #是否有上一级
    xia = models.IntegerField(default=1,verbose_name='下级领域') #是否有下一级

    def __str__(self):
        return self.pname

    class Meta:
        db_table = 'postionsone'
        verbose_name_plural = '[06]一级职业领域'


#8二级信息表
class Positionstwo(models.Model):
    t_pid = models.AutoField(primary_key=True,verbose_name='编号')  # 一级编号
    pname = models.CharField(max_length=50,verbose_name='领域名称')  # 领域名称
    shang = models.IntegerField(default=1,verbose_name='上级标签')  # 是否有上一级
    xia = models.IntegerField(default=1,verbose_name='下级领域')  # 是否有下一级
    twoid = models.ForeignKey(Postionsone,db_column='o_pid',verbose_name='所属领域')

    def __str__(self):
        return self.pname

    class Meta:
        db_table = 'positionstwo'
        verbose_name_plural= '[07]二级职位领域'


#9三级职位表
class Positions(models.Model):
    # 领域细分fid=1一级，
    s_pid = models.AutoField(primary_key=True,verbose_name='编号')  # 一级标题编号，
    pname = models.CharField(max_length=50,verbose_name='职位名称')  # 领域名称
    shang = models.IntegerField(default=1) #是否有上一级
    xia = models.IntegerField(default=0) #是否有下一级
    count = models.IntegerField(default=0,verbose_name='访问次数') #请求次数
    threeaid = models.ForeignKey(Postionsone,db_column='ta_pid',verbose_name='所属领域1') #对应的一级标题id
    threeid = models.ForeignKey(Positionstwo,db_column='t_pid',verbose_name='所属领域2')  #对应的二级标题id

    def __str__(self):
        return self.pname

    class Meta:
        db_table = 'positions'
        verbose_name_plural = '[08]工作职位'


#10招聘信息表
class Informations(models.Model):
    i_id = models.AutoField(primary_key=True,verbose_name='编号')#编号
    i_type = models.CharField(max_length=50,null=True,verbose_name='工作类型')#工作类型
    i_name = models.CharField(max_length=20,null=True,verbose_name='职位名称')#职位名称
    apart = models.CharField(max_length=50,null=True,verbose_name='所属部门')#所属部门
    t_type = ((0,'不限'),(1,'兼职'),(2,'实习'))
    infor_type = models.IntegerField(default=0,choices=t_type,verbose_name='工作性质')#工作性质
    i_payfor = models.CharField(max_length=20,null=True,verbose_name='月薪范围')#月薪范围
    min_payfor = models.IntegerField(default=0,verbose_name='最低月薪')#最低月薪
    max_payfor = models.IntegerField(default=0,verbose_name='最高月薪')#最高月薪
    i_city = models.CharField(max_length=10,null=True,verbose_name='工作城市')#工作城市
    i_exp = models.CharField(max_length=100,null=True,verbose_name='要求工作经验')#要求工作经验
    min_exp = models.IntegerField(default=0,verbose_name='最低工作经验')#最低工作经验
    max_exp = models.IntegerField(default=0,verbose_name='最高工作经验')#最高工作经验
    i_degree = models.CharField(max_length=50,null=True,verbose_name='要求最低学历')#要求最低学历
    payarea = ((0,'2k以下'),(1,'2k-5k'),(2,'5k-10k'),(3,'10k-15k'),(4,'15k-25k'),(5,'25k-50k'),(6,'50k以上')) #薪资
    payshai = models.IntegerField(default=0,choices=payarea,verbose_name='薪资范围')
    exparea = ((0,'不限'),(1,'应届毕业生'),(2,'1年以下'),(3,'1-3年'),(4,'3-5年'),(5,'5-10年'),(6,'10年以上'))#工作经验
    expshai = models.IntegerField(default=0,choices=exparea,verbose_name='工作经验')
    degreearea = ((0,'不限'),(1,'大专'),(2,'本科'),(3,'硕士'),(4,'博士'))
    degreeshai = models.IntegerField(default=0,choices=degreearea,verbose_name='学历')
    areaarea = ((0,'全国'),(1,'北京'),(2,'上海'),(3,'广州'),(4,'深圳'),(5,'成都'),(6,'杭州'),(7,'武汉'),(8,'南京'),(9,'长春'),(10,'重庆'),(11,'长沙'),(12,'常州'),(13,'东莞'),(14,'大连'),(15,'佛山'),(16,'福州'),(17,'贵阳'),(18,'哈尔滨'),(19,'合肥'),(20,'海口'),(21,'惠州'),(22,'金华'),(23,'济南'),(24,'嘉兴'),(25,'昆明'),(26,'廊坊'),(27,'宁波'),(28,'南昌'),(29,'南宁'),(30,'南通'),(31,'青岛'),(32,'泉州'),(33,'石家庄'),(34,'绍兴'),(35,'沈阳'),(36,'苏州'),(37,'天津'),(38,''),(39,'太原'),(40,'台州'),(41,'无锡'),(42,'温州'),(43,'西安'),(44,'厦门'),(45,'烟台'),(46,'珠海'),(47,''),(48,'中山'),(49,'郑州'))
    areashai = models.IntegerField(default=0,choices=areaarea,verbose_name='工作地点')
    i_wealth = models.CharField(max_length=20,null=True,verbose_name='职位诱惑')#职位诱惑
    i_address = models.CharField(max_length=200,null=True,verbose_name='详细工作地址')#工作地址
    i_introduce = models.CharField(max_length=500,null=True,verbose_name='职位描述介绍')#职位描述
    posttime = models.DateTimeField(default=timezone.now,verbose_name='发布时间')#发布时间
    company = models.ForeignKey(Companies,on_delete=models.CASCADE,db_column='c_id',verbose_name='发表公司')#关联发布公司
    type = models.ForeignKey(Positions,db_column='s_pid',verbose_name='职位类型')

    def __str__(self):
        return self.i_name

    class Meta:
        db_table = 'information'
        verbose_name_plural = '[02]招聘信息'


#11标签表
class Tags(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=20) #标签内容
    # p_type = ((0,'其他'))
    c_id = models.ForeignKey(Companies,on_delete=models.CASCADE,db_column='c_cid')

    def __str__(self):
        return self.t_name

    class Meta:
        db_table = 'tags'


#12我收藏/订阅的职位
class InfoStatus(models.Model):
    information = models.ForeignKey(Informations,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    s_type = ((0,'无状态'),(1,'已收藏'),(2,'订阅'))
    status = models.IntegerField(default=0,choices=s_type)
    # def UpdateInfor(self,status):
    #     ifu
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'status'
        verbose_name_plural = '职位选择状态表'


#13图片存储
class PModel(models.Model):
    pic_url = models.ImageField(upload_to='upload/%Y/%m',verbose_name='photos')

    def __str__(self):
        return self.pic_url.name

    class Meta:
        db_table = 'pic'
        verbose_name_plural = '照片'


#添加action联系
class Article(models.Model):
    # 文章状态，类似枚举
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发布'),
    )
    # 标题
    title = models.CharField(max_length=30)
    # 内容
    body = models.TextField()
    # 状态
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    def __str__(self):
        return self.title