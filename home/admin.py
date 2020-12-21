from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.utils.html import format_html

from home.models import Student


class StudentAdmin(ModelAdmin):

    list_display = ('email', 'students', 'birthday', 'is_active')

    def students(self, object):

        if not object.social_url:
            return f'{object.name} {object.surname}'
        else:
            return format_html("<a href='{}' target='_blank'>{} {}</a>", object.social_url, object.name,
                                 object.surname)


admin.site.register(Student, StudentAdmin)
