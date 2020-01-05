from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_article(request, article_id):
    # param article_id:是一个参数名称，在blog\urls.py文件中作为url地址的一部分，如果访问的话，调用该模板中的这个函数，会将这个参数设置为调用的值

    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, 'blog/content.html', {'article': article, 'publish': pub})
# Create your views here.

