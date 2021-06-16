from django.urls import path, include #引入路由配置相关的包
import djangoapp1.views #引入视图文件

urlpatterns = [
    path('hello_world', djangoapp1.views.hello_world),  #有相关的路径就调用对应的函数
    path('articleinfor', djangoapp1.views.get_article_infor),
    path('index', djangoapp1.views.get_index_page),
    path('details/<int:article_id>', djangoapp1.views.get_details_page)

]

