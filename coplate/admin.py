from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review
# Register your models here.

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)   # 추가 필드는 어드민에 따로 지정 해줘야 함
admin.site.register(Review)