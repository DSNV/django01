from django.contrib import admin

# Register your models here.
from .models import Users, Companies, Founders, Informations, Product, Article, Positions, Positionstwo, Postionsone, \
    Positions, Resumes, ResumeOnline
from django.contrib.auth.models import Group, User
from .models import PModel


# #-*-coding:utf-8 -*-
# from django.contrib import admin
# from .models import *
# from django.http import StreamingHttpResponse
# from django.shortcuts import render,HttpResponse,redirect
# import xlwt
# import os
# from io import BytesIO
#
#
# class testAdmin(admin.ModelAdmin):
#    list_display = ('a_name','b_level','...')
#    actions = ["export_excel",]
#    export_excel.short_description = "导出Excel文件"
# 指令处理函数，参数固定写法
# def make_article_published(modeladmin, request, queryset):
#     # queryset 是从 数据库 查询到的model set
#     # 更新status状态为p，在此处就是Article
#     queryset.update(status='p')
# # 此指令的名称
# make_article_published.short_description = '更改状态为发布'
#
#
# #将Article注册到后台
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     # 后台列表展示的字段
#     list_display = ('title', 'status')
#     # 动作集合
#     actions = [make_article_published]

# def make_article_published(modeladmin, request, queryset):

# admin.site.register(Users)
# class PModelAdmin(admin.ModelAdmin):
    # list_display = ['pic_url']
    # search_fields = ['pic_url']


def Userupdate(modeladmin, request, queryset):
    queryset.update(identity=1)
Userupdate.short_description = '修改为公司用户'


def Userupdate1(modeladmin, request, queryset):
    queryset.update(identity=0)
Userupdate1.short_description = '修改为普通用户'


class UserAdmin(admin.ModelAdmin):
    list_display = ['u_id','username','password','age','sex','phonenum','u_regtime','identity']
    search_fields = ['username']
    list_per_page = 5
    list_filter = ['username']
    actions = [Userupdate,Userupdate1]
    # actions = [Userupdate1]


class ComAdmin(admin.ModelAdmin):
    list_display = ['c_id','c_name','area','founder','contacts','cont_phone']
    search_fields = ['c_name','area','founder','contacts']
    list_per_page = 10


class FounderAdmin(admin.ModelAdmin):
    list_display = ['f_name','f_position','f_photo','f_blog','f_introduction','f_uid']
    search_fields = ['f_name']
    list_per_page = 10


class InforeAdmin(admin.ModelAdmin):
    list_display = ['i_name','company','i_payfor','i_city','posttime']
    search_fields = ['i_name','i_city','company','i_payfor']
    list_per_page = 10

class PositinAdmin1(admin.ModelAdmin):
    list_display = ['pname']
    search_fields = ['pname']
    list_per_page = 10


class PositinAdmin2(admin.ModelAdmin):
    list_display = ['pname']
    search_fields = ['pname']
    list_per_page = 10


class PositinAdmin3(admin.ModelAdmin):
    list_display = ['pname']
    search_fields = ['pname']
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['p_name','p_web','p_intr','company']
    search_fields = ['p_name']


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','owner','resume']
    list_per_page = 10
    list_filter = ['resume','owner']


class ResumeolAdmin(admin.ModelAdmin):
    list_filter = ['owner']
    list_per_page = 10
    list_display = ['owner','myjob','myexp','myobj','myedu','myinfor','display']


admin.site.register(Companies,ComAdmin)
admin.site.register(Users,UserAdmin)
admin.site.register(Founders,FounderAdmin)
# admin.site.register(PModel,PModelAdmin)
admin.site.register(Informations,InforeAdmin)
admin.site.register(Postionsone,PositinAdmin1)
admin.site.register(Positionstwo,PositinAdmin2)
admin.site.register(Positions,PositinAdmin3)
admin.site.register(Product,ProductAdmin)
admin.site.register(Resumes,ResumeAdmin)
admin.site.register(ResumeOnline,ResumeolAdmin)


admin.site.site_url = '/app/'
admin.site.site_title = "拉狗后台管理"
admin.site.site_header = "拉狗后台管理"
admin.site.index_title = "欢迎~"
admin.site.unregister(Group)
# admin.site.unregister(User)
