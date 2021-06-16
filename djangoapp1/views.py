from django.shortcuts import render
from django.http import HttpResponse
from djangoapp1.models import Article
from django.core.paginator import Paginator #引入分页的模块
# Create your views here.

def hello_world(request):
    return HttpResponse ("Hello World") #将字符串封装成HttpResponse返回


def get_article_infor(request):
    all_article = Article.objects.all()
    title = ["title"]
    for article in all_article:
        title.append(article.article_title)
    return HttpResponse(title)  # 将字符串封装成HttpResponse返回


def get_index_page(request):
    page = request.GET.get("page")  #获取名为page的参数
    if page:
        page = int(page)
    else:     #如果没有这个参数的话，就默认为1
        page = 1
    all_article = Article.objects.all() #把所有的文章都取出来
    top5_article_list = Article.objects.order_by('-publish_date')[:5]#按照发表的时间倒序

    paginator = Paginator(all_article,6) #将所有的文章按每页6个进行分页
    page_num = paginator.num_pages #分页之后的页数
    page_article_list= paginator.page(page) #取得相应页的内容
    if page_article_list.has_next(): #如果该页有下一页，则下一页的页数就是当前的页数加一，如果没有，则当前页就是下一页
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():  #如果该页有上一页，则上一页的页数就是当前的页数减一，如果没有，则当前页就是上一页
        previous_page = page - 1
    else:
        previous_page = page
    #模板系统和参数进行渲染并返回
    return render(request, 'blog/index.html',
                  {
                      'article_list': page_article_list,  #当前分页的文章
                      'page_num': range(1, page_num + 1), #文章的数量
                      'current_page': page, #当前页
                      'previous_page':previous_page, #上一页
                      'next_page': next_page, #下一页
                      'top5_article_list': top5_article_list
                  }
                  )

def get_details_page(request, article_id):
    all_article = Article.objects.all()
    current_article = None
    previous_article = None
    next_article = None
    previous_index = 0  #上一篇文章的索引
    next_index = 0 #下一篇文章的索引
    for index,article in enumerate(all_article): #如果文章存在
        if index ==0:  #表示是第一篇文章
            previous_index = index    # 没有上一篇文章，索引就是第一篇文章
            next_index = index + 1    # 下一篇文章的索引就为该篇文章的索引加1
        elif index == len(all_article) - 1:  #如果是最后一篇文章
            next_index = index  #没有下一篇文章，索引就是最后一篇文章
            previous_index = index - 1  #上一篇文章的索引就是该篇文章的索引减1
        else:                       # 正常情况下就是正常的索引加减
            previous_index = index - 1
            next_index = index + 1

        if article.article_id == article_id:   #取出所有的文章，根据文章ID的不同来匹配，实现文章详情页的跳转
            current_article = article
            previous_article = all_article[previous_index]  #根据索引得到上一篇文章
            next_article = all_article[next_index]          #根据索引得到下一篇文章
            break
    section_list = current_article.article_content.split("\n")
    return render(request, 'blog/details.html',
                  {
                      'current_article': current_article,
                      'section_list':section_list,
                      'previous_article': previous_article,  #上一篇文章
                      'next_article': next_article     #下一篇文章
                  }
                  )

