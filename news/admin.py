from django.contrib import admin
from news.models import News, Category

class NewsAdmin(admin.ModelAdmin):
  list_display = ['title', 'description', 'category', 'date']
  search_fields = ['title']
# Register your models here.

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
