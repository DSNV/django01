from django.conf.urls import url

from App import views

urlpatterns=[
    #主页
    url(r'^$',views.index,name='index'),
    #更多职位
    url(r'^list/$',views.list,name='list'),
    # #筛选职位表
    url(r'^shailist/(?P<payfor>\d{0,})/(?P<exp>\d{0,})/(?P<degree>\d{0,})/(?P<worktype>\d{0,})/(?P<area>\d{0,})/$',views.shailist,name='shailist'),
    #搜索职位表
    url(r'^seeklist/(?P<spid>\d+)/$',views.seeklist,name='seeklist'),
    # 公司列表
    # url(r'^companylist/$',views.companylist,name='companylist'),
    #点击职位后详情，未登录状态
    url(r'^postdetail/$',views.postdetail,name='postdetail'),
    #公司详情
    url(r'^myhome/$',views.myhome,name='myhome'),
    #账号设置
    url(r'^accountbind/$',views.accountbind,name='accountbind'),
    #修改密码
    url(r'updatepwd/$',views.updatepwd,name='updatepwd'),
    #职位订阅
    url(r'^subscribe/$',views.subscribe,name='subscribe'),
    #我的简历
    url(r'^jianli/$',views.jianli,name='jianli'),
    #简历投递状态
    url(r'^delivery/$',views.delivery,name='delivery'),
    #简历推荐岗位
    url(r'^mylist/$',views.mylist,name='mylist'),
    #联系我们
    url(r'^about/$',views.about,name='about'),
    #用户登录
    url(r'^login/$',views.login,name='login'),
    #用户注册
    url(r'^register/$',views.register,name='register'),
    #用户退出登录
    url(r'^logout/$',views.logout,name='logout'),
    #公司申请第一步11111111111111111111111111
    url(r'^companyapplyfirst/$',views.companyapplyfirst,name='comfirst'),
    #公司申请第二部22222222222222222222222222
    url(r'^companyapplysecond/$',views.companyapplysecond,name='comsecond'),
    #公司申请第三部33333333333333333333333333
    url(r'^companyapplythird/$',views.companyapplythird,name='comthird'),
    #公司申请第四部44444444444444444444444444
    url(r'^companyapplyfourth/$', views.companyapplyfourth, name='comfourth'),
    #公司申请第五部55555555555555555555555555
    url(r'^companyapplyfifth/$', views.companyapplyfifth, name='comfifth'),
    #公司申请提交中66666666666666666666666666
    url(r'^authsuccess/$',views.authsuccess,name='authsuccess'),
    #公司岗位申请第一部1111111111111111111111
    # url(r'^bindstepfirst/$',views.bindstepfirst,name='bindstepfirst'),
    #公司岗位申请第二部2222222222222222222222
    # url(r'^bindstepsecond/$',views.bindstepsecond,name='bindstepsecond'),
    #公司岗位申请第三部3333333333333333333333
    # url(r'^bindstepthird/$',views.bindstepthird,name='bindstepthird'),
    #岗位收藏页面
    url(r'^collections/(?P<u_id>\d+)/',views.collections,name='collections'),
    url(r'^collections1/(?P<u_id>\d+)/', views.collections1, name='collections1'),
    url(r'^collections/(?P<u_id>\d+)/', views.collections2, name='collections2'),

    #简历查看情况等一系列页面，招收新职位除外
    url(r'^canInter/$',views.canInter,name='caninter'),
    #公司发布新的岗位
    url(r'^jobnewapply/$',views.createnewjob,name='createnewjob'),
    #公司协议
    url(r'^protocol/$',views.protocol,name='protocol'),
    # url(r'')
    url(r'^refuse/$',views.haveRefuseResumes,name='refuse'),
    url(r'^notice/$',views.haveNoticeResumes,name='notice'),
    url(r'^interview/$',views.canInter,name='interview')

]