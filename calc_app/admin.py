from django.contrib import admin
from calc_app.models import RequestModel, RowModel, ResponseModel


# @admin.action(description='Mark selected stories as published')
# def edit(modeladmin, request, queryset):
#     queryset.update(s='-')
#
#
class RowModelAdmin(admin.ModelAdmin):
    list_display = ['s', 'v', 't', 'request']
    # ordering = ['request']
    # actions = [edit]


class RequestModelAdmin(admin.ModelAdmin):
    list_display = ['file_name']


class ResponseModelAdmin(admin.ModelAdmin):
    list_display = ['calculation_time', 'calculation_function', 'request']


admin.site.register(RowModel, RowModelAdmin)
admin.site.register(RequestModel, RequestModelAdmin)
admin.site.register(ResponseModel, ResponseModelAdmin)
