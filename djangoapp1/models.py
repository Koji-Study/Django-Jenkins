from django.db import models

# Create your models here.
class Article(models.Model):  #模型层字段的定义
    #文章的唯一ID
    article_id = models.AutoField(primary_key = True) #主键，自动的
    #文章的标题
    article_title = models.TextField() #标题文本类型
    #文章的摘要
    article_brief = models.TextField() #摘要文本类型
    #文章的主要内容
    article_content = models.TextField()# 主要内容是文本类型
    #文章的发布日期
    publish_date = models.DateTimeField(auto_now = True) #默认为当前的时间,auto_now = True默认以当前时间为发布日期

    def __str__(self):
        return self.article_title   #在后台管理界面admin中的文章列表显示文章的标题