from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Manager)
# admin.site.register(User)
admin.site.register(Manage)

admin.site.register(User)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         'nickname',
#         'email',
#         'date_joined'
#     )

#     list_display_links = (
#         'nickname',
#         'email',
#     )