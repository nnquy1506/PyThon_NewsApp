from . import views
from django.urls import path

urlpatterns = [
    path('xahoi/', views.xahoi, name = "xahoi"),
    path('thegioi/', views.thegioi, name = "thegioi"),
    path('thethao/', views.thethao, name = "thethao"),
    path('suckhoe/', views.suckhoe, name = "suckhoe"),
    path('kinhdoanh/', views.kinhdoanh, name = "kinhdoanh"),
    path('giaoduc/', views.giaoduc, name = "giaoduc"),
    path('detail/<int:news_id>', views.detailView , name = "detail"),
    path('',views.index, name = "home")
]