import hashlib
import os

from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
#首页
from django.urls import reverse

from App.models import Users, Informations, Companies, Founders, Tags, Positions, Postionsone, Positionstwo, Product, \
    Resumes, InfoStatus, GetResume

#首页
from Lagouwh import settings


def index(request):
    # 全部职位
    informations = Informations.objects.filter()
    companies = Companies.objects.filter()
    founders = Founders.objects.filter()
    tags = Tags.objects.filter()
    informationsnew = Informations.objects.order_by('-posttime')[0:11]
    poone = Postionsone.objects.filter()
    potwo = Positionstwo.objects.filter()
    pothreeline = Positions.objects.order_by('-count')[0:8]
    pothreehot = Positions.objects.order_by('-count')[0:11]
    pothree = Positions.objects.filter()
    return render(request,'index.html',locals())
#职位列表
def jobstate(request):
    return render(request,'jobstate.html',locals())
    #
#更多职位
def list(request):
    if request.method =='POST':
        value = request.POST.getlist('work')
        print(value)
        kd = request.POST.get('kd')
        informations = Informations.objects.filter()
        companies = Companies.objects.filter()
        tags = Tags.objects.filter()
        poaa = Positions.objects.filter(pname__icontains=kd)
        if not poaa:
            poaa = Positionstwo.objects.filter(pname__icontains=kd)
            for i in poaa:
                poaa = i.t_pid
            poaa = Positions.objects.filter(threeid=poaa)
            if not poaa:
                poaa = Postionsone.objects.filter(pname__icontains=kd)
                for i in poaa:
                    poaa = i.o_pid
                poaa = Positions.objects.filter(threeaid=poaa)
        pothreehot = Positions.objects.order_by('-count')[0:11]
    else:
        informations = Informations.objects.filter()
        companies = Companies.objects.filter()
        tags = Tags.objects.filter()
        poaa = Positions.objects.filter()
        pothreehot = Positions.objects.order_by('-count')[0:11]
    payf = Informations.objects.values('payshai').distinct()
    expf = Informations.objects.values('expshai').distinct()
    degreef = Informations.objects.values('degreeshai').distinct()
    typef = Informations.objects.values('infor_type').distinct()
    info = Informations.objects.filter()
    listpay = []
    listexp = []
    listdegree = []
    listtype = []
    for i in payf:
        listpay.append(i['payshai'])
    for i in expf:
        listexp.append(i['expshai'])
    for i in degreef:
        listdegree.append(i['degreeshai'])
    for i in typef:
        listtype.append(i['infor_type'])
    return render(request,'list.html',locals())

#搜索职位表
def seeklist(request,spid=1):
    poaa = Positions.objects.filter(s_pid=spid)
    informations = Informations.objects.filter()
    companies = Companies.objects.filter()
    tags = Tags.objects.filter()
    info = Informations.objects.filter()
    pothreehot = Positions.objects.order_by('-count')[0:11]
    payf = Informations.objects.values('payshai').distinct()
    expf = Informations.objects.values('expshai').distinct()
    degreef = Informations.objects.values('degreeshai').distinct()
    typef = Informations.objects.values('infor_type').distinct()
    info = Informations.objects.filter()
    listpay = []
    listexp = []
    listdegree = []
    listtype = []
    for i in payf:
        listpay.append(i['payshai'])
    for i in expf:
        listexp.append(i['expshai'])
    for i in degreef:
        listdegree.append(i['degreeshai'])
    for i in typef:
        listtype.append(i['infor_type'])
    return render(request,'list.html',locals())

#筛选职位表
def shailist(request,payfor,exp,degree,worktype,area):
    if request.method == 'GET':
        # informations = Informations.objects.filter()
        # companies = Companies.objects.filter()
        # tags = Tags.objects.filter()
        # # if payfor == '0' or exp == '0' or degree == '0' or worktype == '0' or area == '0':
        info = Informations.objects.filter()
        infoa = Informations.objects.filter()
        companies = Companies.objects.filter()
        tags = Tags.objects.filter()
        areaa = Informations.objects.filter(areashai=area)
        for i in area:
            print(i)
        pothreehot = Positions.objects.order_by('-count')[0:11]
        payf = Informations.objects.values('payshai').distinct()
        expf = Informations.objects.values('expshai').distinct()
        degreef = Informations.objects.values('degreeshai').distinct()
        typef = Informations.objects.values('infor_type').distinct()
        listpay = []
        listexp = []
        listdegree = []
        listtype = []
        for i in payf:
            listpay.append(i['payshai'])
        for i in expf:
            listexp.append(i['expshai'])
        for i in degreef:
            listdegree.append(i['degreeshai'])
        for i in typef:
            listtype.append(i['infor_type'])
        payfor = int(payfor)
        exp = int(exp)
        degree = int(degree)
        worktype = int(worktype)
        area = int(area)
        # if payfor == 0 and exp == 0 and degree == 0 and worktype == 0 and area == 0:
        #     print('---------------------')
        #     info = Informations.objects.filter()
        #     print(info)
        #     companies = Companies.objects.filter()
        #     tags = Tags.objects.filter()
        #     return redirect(reverse('app:list'))
        if payfor != 0:
            infoa = infoa.filter(payshai=payfor).all()
            companies = Companies.objects.filter()
            tags = Tags.objects.filter()
            if not info:
                info = Informations.objects.filter()
        if exp != 0:
            infoa = infoa.filter(expshai=exp).all()
            companies = Companies.objects.filter()
            tags = Tags.objects.filter()
            if not info:
                info = Informations.objects.filter()
        if degree != 0:
            infoa = infoa.filter(degreeshai=degree).all()
            companies = Companies.objects.filter()
            tags = Tags.objects.filter()
            if info == None:
                info = Informations.objects.filter()
        if worktype != 0:
            infoa = infoa.filter(infor_type=worktype).all()
            companies = Companies.objects.filter()
            tags = Tags.objects.filter()
            if info == None:
                info = Informations.objects.filter()
        if area != 0:
            infoa = infoa.filter(areashai=area).all()
            companies = Companies.objects.filter()
            tags = Tags.objects.filter()
            if info == None:
                info = Informations.objects.filter()
        return render(request,'shailist.html',locals())
        # return redirect(reverse('app:shailist',{
        #     'payfor':payfor,
        #     'exp':exp,
        #     'degree':degree,
        #     'worktype':worktype,
        #     'area':area
        # }))
        # print(payfor,exp,degree,worktype,area)
        # return HttpResponse('nihc')
    print(payfor,exp,degree,worktype,area)
    return HttpResponse('aaaaaaaa')

#职位详情未登录页面
def postdetail(request):
    return render(request,'postdetail.html',locals())

#公司详情
def myhome(request):
    return render(request,'myhome.html',locals())


#账号设置
def accountbind(request):
    return render(request,'accountBind.html',locals())

#修改密码
def updatepwd(request):
    return render(request,'updatePwd.html',locals())

#职位订阅
def subscribe(request):
    return render(request,'subscribe.html',locals())

#我的简历
def jianli(request,u_id=1):
    user = Users.objects.filter(u_id=u_id)
    return render(request,'jianli.html',locals())

#简历投递状态
def delivery(request):
    return render(request,'delivery.html',locals())

#简历推荐岗位
def mylist(request):
    return render(request,'mList.html',locals())

#联系我们
def about(request):
    return render(request,'about.html',locals())

#用户登录
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # passold = hashlib.sha1().hexdigest()
        if Users.objects.filter(email=email,password=password).exists():
            ident = Users.objects.filter(email=email).first()
            identity = ident.identity
            print(identity, type(identity))
            request.session['email'] = email
            request.session['identity'] = identity
            return redirect(reverse('app:index'),locals())
        else:
            return render(request,'login.html',locals())
    return render(request,'login.html',locals())
#用户注册

def register(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Users()
        emailold = Users.objects.filter(email=email).exists()
        if emailold:
            return render(request,'register.html',locals())
        else:
            user = Users(email=email,username=email,password=password,identity=type)
            user.save()
            return redirect(reverse('app:login'),locals())
    return render(request,'register.html',locals())

#用户退出登录
def logout(request):
    request.session.clear()
    return redirect(reverse('app:index'))

#公司申请第一部1111111111111111111111111111111111
def companyapplyfirst(request):
    lista = ((0,'全国'),(1,'北京'),(2,'上海'),(3,'广州'),(4,'深圳'),(5,'成都'),(6,'杭州'),(7,'武汉'),(8,'南京'),(9,'长春'),(10,'重庆'),(11,'长沙'),(12,'常州'),(13,'东莞'),(14,'大连'),(15,'佛山'),(16,'福州'),(17,'贵阳'),(18,'哈尔滨'),(19,'合肥'),(20,'海口'),(21,'惠州'),(22,'金华'),(23,'济南'),(24,'嘉兴'),(25,'昆明'),(26,'廊坊'),(27,'宁波'),(28,'南昌'),(29,'南宁'),(30,'南通'),(31,'青岛'),(32,'泉州'),(33,'石家庄'),(34,'绍兴'),(35,'沈阳'),(36,'苏州'),(37,'天津'),(39,'太原'),(40,'台州'),(41,'无锡'),(42,'温州'),(43,'西安'),(44,'厦门'),(45,'烟台'),(46,'珠海'),(48,'中山'),(49,'郑州'))
    listb=[]
    for i in lista:
        listb.append(i[1])
    email = request.session.get('email')
    userid = Users.objects.filter(email=email)
    for i in userid:
        ccid = i.u_id
    caid = Companies.objects.filter(userid=ccid)
    if caid:
        return render(request,'create.html',locals())
    return render(request,'companyapplyfirst.html',locals())

#公司申请第二部2222222222222222222222222222222222
def companyapplysecond(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        logo = request.FILES.get('logo')
        # print(logo.__dict__)
        if logo:
            savePath = os.path.join(settings.MDEIA_ROOT,logo.name)
            with open(savePath,'wb') as f:
                f.write(logo.read())
            web = request.POST.get('web')
            c_address = request.POST.get('c_address')
            # print(c_address)
            area = request.POST.get('area')
            size = request.POST.get('size')
            develop = request.POST.get('develop')
            c_infor = request.POST.get('c_infor')
            sizea = ['无信息','10人以下','10-50人','50-100人','100人以上']
            developa = ['未融资','天使轮','Pre_A轮','A轮','B轮','C轮','D轮及以上','已上市']
            for i in sizea:
                if size in sizea:
                    size = sizea.index(size)
                    print(type(size))
            for a in developa:
                if develop in developa:
                    develop = developa.index(develop)
                    print(type(develop))
            savePath = savePath.replace("/","\\")
            print(c_name,savePath,web,c_address,area,size,develop,c_infor)
            # if not(c_name == None and savePath == None and web == None and c_address == None and area == None and size == None and develop == None or c_infor == None):
            #     # company = Companies(c_name=c_name,logo=savePath,web=web,c_address=c_address,area=area,size=size,develop=develop,c_infor=c_infor)
            company = Companies()
            company.c_name = c_name
            company.logo = savePath
            company.web = web
            company.c_address = c_address
            company.area = area
            company.size = size
            # company.develop = develop
            company.c_infor = c_infor
            aid = request.session.get('email')
            ccid = Users.objects.filter(email=aid)
            for i in ccid:
                userid = i.u_id
            print('-------------------------------------------------------------------------------------------')
            company.userid = userid
            company.save()
            return render(request, 'companyapplysecond.html', locals())
            # return render(request,'companyapplyfirst.html',locals())
    return redirect(reverse('app:comfirst'))

#公司申请第三部3333333333333333333333333333333333
def companyapplythird(request):
    if request.method == 'GET':
        list = request.GET.getlist('list')
        print(list)
    return render(request,'companyapplythird.html',locals())

#公司申请第四部4444444444444444444444444444444444
def companyapplyfourth(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        f_position = request.POST.get('f_position')
        f_introduction = request.POST.get('f_introduction')
        email = request.session.get('email')
        ccid = Users.objects.filter(email=email)
        for i in ccid:
            ccid = i.u_id
        founders = Founders()
        founders.f_name = f_name
        founders.f_position = f_position
        founders.f_introduction = f_introduction
        founders.f_uid = ccid
        founders.save()
        found = Founders.objects.filter(f_uid=ccid)
        for i in found:
            uid = i.id
        comp = Companies.objects.filter(userid=ccid)
        for a in comp:
            aid = a.c_id
            comp = Companies.objects.get(pk=aid)
            print(comp.area)
            print(comp.founder)
            print(comp)
            print(aid)
            print(uid)
            comp.founder_id = uid
            comp.save()
        # comp.founder.f_name =
    return render(request,'companyapplyfourth.html',locals())

#公司申请第五部5555555555555555555555555555555555
def companyapplyfifth(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_web = request.POST.get('p_web')
        p_intr = request.POST.get('p_infr')
        email = request.session.get('email')
        userid = Users.objects.filter(email=email)
        for i in userid:
            ccid = i.u_id
            comid = Companies.objects.filter(userid=ccid)
        for i in comid:
            coid = i.c_id
            product = Product()
            product.p_name = p_name
            product.p_web = p_web
            product.p_intr = p_intr
            product.company_id = coid
            product.save()
    return render(request,'companyapplyfifth.html',locals())

#公司申请审核中6666666666666666666666666666666666
def authsuccess(request):
    if request.method == 'POST':
        comintroduce = request.POST.get('comintroduce')
        email = request.session.get('email')
        userid = Users.objects.filter(email=email)
        for i in userid:
            ccid = i.u_id
            coid = Companies.objects.filter(userid=ccid)
            for i in coid:
                aid = i.c_id
                caid = Companies.objects.get(pk=aid)
                caid.comintroduce = comintroduce
                caid.save()
    return render(request,'authSuccess.html',locals())

# #公司岗位申请第一步111111111111111111111111111111
# def bindstepfirst(request):
#     return render(request,'bindstep1.html',locals())
#
# #公司岗位申请第二步222222222222222222222222222222
# def bindstepsecond(request):
#     return render(request,'bindStep2.html',locals())
# #公司岗位申请第三步333333333333333333333333333333
# def bindstepthird(request):
#     return render(request,'bindStep3.html',locals())


#职位收藏
def collections(request,u_id=1):
    # users = Users.objects.filter()
    # print(users)
    # for user in users:
    #     status = InfoStatus.objects.get(user=user.u_id)
    #     if status.user.u_id == user.u_id and status.status == 1:
    #         print(status.information)
    #         return render(request,'collections.html',locals())
    # users = Users.objects.filter(u_id=u_id)
    info = InfoStatus.objects.filter(user=u_id)
    users = Users.objects.get(u_id=u_id)
    if users and info:
        status = InfoStatus.objects.filter(status=1)
        print(11,status)
        for i in status:
            if i.user.u_id == users.u_id:
                print(i.user.u_id,users.u_id,12334)
                return render(request,'collections.html',locals())
    return render(request,'collections.html',locals())


def collections1(request, u_id=1):
    print(123)
    user = Users.objects.filter(u_id=u_id)
    status = InfoStatus.objects.filter(user=u_id)
    print(status)
    for s in status:
        s.status = 0
        print(s.status)
        s.save()
        return render(request,'collections.html',locals())
    return render(request,'collections.html',locals())


def collections2(request, u_id=1):
    status = InfoStatus.objects.filter(user=u_id)
    print(status)
    print(1111)
    for s in status:
        print(s.status)
        print(1111)
        s.status = 1
        print(s)
        s.save()
    return render(request,'collections.html',locals())


#简历查看情况等一系列页面，招收新职位除外


#公司发布新的岗位
def createnewjob(request):
    if request.method == 'POST':
        i_type = request.POST.get('i_type')
        print(i_type)
    return render(request,'create.html')

#公司协议
def protocol(request):
    return render(request,'protocol.html',locals())


def userlist(request, page=1):
    users = Users.objects.all()# 实例化分⻚对象，⼀⻚两条记录
    pagination = Paginator(users, 2)
    page = pagination.page(page)  # 某⼀⻚的分⻚对象
    return render(request, 'userlist.html', context={
        'data': page.object_list,  # 当前⻚的数据(列表)
        'page_range': pagination.page_range,  # ⻚码范围
        'page': page
})


def haveRefuseResumes(request):
    resume = GetResume.objects.filter(status=2)
    # for i in resume:
    #     print(i.owner.username)
        # resume = GetResume.resume.owner.objects.filter(u_id=)
    return render(request,'haveRefuseResumes.html',locals())


def haveNoticeResumes(request):
    resume = GetResume.objects.filter(status=1)
    return render(request,'haveNoticeResumes.html',locals())


def canInter(request,c_id=1):
    reseme =GetResume.objects.filter(status=0)
    for i in reseme:
        company = Companies.objects.filter(c_id=c_id)

    return render(request,'canInterviewResumes.html',locals())