"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import MainPage, StudentUpdate, \
    StudentUpdateMain, StudentsInfo, home, students, ReportCardInfo, ReportCardDelete, SubjectInfo, \
    SubjectDelete, TeacherInfo, SubjectUpdate, TeacherUpdate, TeacherDelete  # noqa
  # noqa
urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', MainPage.as_view(), name='main_page'),
    path('students/', students, name='students'),
    path('student-update/<id>/', StudentUpdate.as_view(),
         name='student_update'),
    path('student-update/', StudentUpdateMain.as_view(),
         name='student_update_main'),
    path('students-info/', StudentsInfo.as_view(), name='students_info'),

    path('report-card-info/', ReportCardInfo.as_view(),
         name='report_card_info'),
    path('report-card-delete/<id>/', ReportCardDelete.as_view(),
         name='report_card_delete'),

    path('subject-info/', SubjectInfo.as_view(),
         name='subject_info'),
    path('subject-delete/<id>/', SubjectDelete.as_view(),
         name='subject_delete'),

    path('subject-update/<id>/', SubjectUpdate.as_view(),
         name='subject_update'),

    path('teacher-info/', TeacherInfo.as_view(),
         name='teacher_info'),
    path('teacher-delete/<id>/', TeacherDelete.as_view(),
         name='teacher_delete'),
    path('teacher-update/<id>/', TeacherUpdate.as_view(),
         name='teacher_update'),
]
