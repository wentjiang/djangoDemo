from django.contrib import admin
from .models import Question
# Register your models here.

#向管理页面注册Question
admin.site.register(Question)