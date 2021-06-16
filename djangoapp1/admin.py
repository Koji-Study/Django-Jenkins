from django.contrib import admin
#uesername:wanghao
#Fendou2021###
# Register your models here.
from .models import Article #导入文章的模块

admin.site.register(Article) #将Article模块注册到admin模块里