from django.shortcuts import render
from news.models import Category, News
# Create your views here.

# def menu(request):
#     data = {'Categorys': Category.objects.all() }
#     return render(request, 'news/base.html', data)


def xahoi(request):
    data = {'breaking': News.objects.all().filter(breaking='on').filter(category='1').order_by('-date')[:3], 'trending': News.objects.all().filter(
        breaking='on').order_by('-date')[:3], 'Categorys': Category.objects.all(), 'ordernews': News.objects.all().filter(category='1').order_by('-date')[:3]}
    return render(request, 'news/xahoi.html', data)


def thegioi(request):
    data = {'breaking': News.objects.all().filter(breaking='on').filter(category='2').order_by('-date')[:3], 'trending': News.objects.all().filter(
        breaking='on').order_by('-date')[:3], 'Categorys': Category.objects.all(), 'ordernews': News.objects.all().filter(category='2').order_by('-date')[:3]}
    return render(request, 'news/thegioi.html', data)


def thethao(request):
    data = {'breaking': News.objects.all().filter(breaking='on').filter(category='3').order_by('-date')[:3], 'trending': News.objects.all().filter(
        breaking='on').order_by('-date')[:3], 'Categorys': Category.objects.all(), 'ordernews': News.objects.all().filter(category='3').order_by('-date')[:3]}
    return render(request, 'news/thethao.html', data)


def suckhoe(request):
    data = {'breaking': News.objects.all().filter(breaking='on').filter(category='4').order_by('-date')[:3], 'trending': News.objects.all().filter(
        breaking='on').order_by('-date')[:3], 'Categorys': Category.objects.all(), 'ordernews': News.objects.all().filter(category='4').order_by('-date')[:3]}
    return render(request, 'news/suckhoe.html', data)


def kinhdoanh(request):
    data = {'breaking': News.objects.all().filter(breaking='on').filter(category='5').order_by('-date')[:3], 'trending': News.objects.all().filter(
        breaking='on').order_by('-date')[:3], 'Categorys': Category.objects.all(), 'ordernews': News.objects.all().filter(category='5').order_by('-date')[:3]}
    return render(request, 'news/kinhdoanh.html', data)


def giaoduc(request):
    data = {'breaking': News.objects.all().filter(breaking='on').filter(category='6').order_by('-date')[:3], 'trending': News.objects.all().filter(
        breaking='on').order_by('-date')[:3], 'Categorys': Category.objects.all(), 'ordernews': News.objects.all().filter(category='6').order_by('-date')[:3]}
    return render(request, 'news/giaoduc.html', data)


def detailView(request, news_id):
    c = News.objects.get(pk=news_id)
    return render(request, "news/detail_news.html", {"detail": c, 'Categorys': Category.objects.all(), 'News': News.objects.all(), 'ordernews': News.objects.all().order_by('-date')[:3]})


def index(request):
    data = {'breaking': News.objects.all().filter(breaking='on').order_by('-date')[:6], 'Categorys': Category.objects.all(),
            'ordernews': News.objects.all().order_by('-date')[:3], 'featured': News.objects.all().filter(featured='on').order_by('-date')[:1]}
    return render(request, 'news/index.html', data)
