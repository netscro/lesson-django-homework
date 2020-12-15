from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.utils.html import format_html

from home.models import Student


class StudentAdmin(ModelAdmin):

    list_display = ('email', 'students', 'birthday')

    def students(self, object):

        field_name = format_html("<a href='{}'>{} {}</a>", object.social_url, object.name,
                                 object.surname)

        if not object.social_url:
            return f'{object.name} {object.surname}'
        else:
            return field_name


admin.site.register(Student, StudentAdmin)
