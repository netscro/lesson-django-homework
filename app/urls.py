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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from home.views import MainPage, StudentUpdate, \
    StudentUpdateMain, StudentsInfo, home, ReportCardInfo, ReportCardDelete, SubjectInfo, \
    SubjectDelete, TeacherInfo, SubjectUpdate, TeacherUpdate, TeacherDelete, JsonStudentsView, CSVView, \
    SendEmail, Students, StudentDelete, LoginUser, SignUpUser, ActivateUser, LogOutUser, StudentsViewAPI, \
    SubjectViewAPI, TeacherViewAPI, ReportCardViewAPI  # noqa
  # noqa

# url адреса для Django Rest Framework
router = routers.DefaultRouter()
router.register(r'students/api_view', StudentsViewAPI, basename='students_api')
router.register(r'subject/api_view', SubjectViewAPI, basename='subject_api')
router.register(r'teacher/api_view', TeacherViewAPI, basename='teacher_api')
router.register(r'report_card/api_view', ReportCardViewAPI, basename='report_card_api')

urlpatterns = [

    path('drf/', include(router.urls)),

    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', MainPage.as_view(), name='main_page'),

    path('students/', Students.as_view(), name='students'),

    # path('student-update/<id>/', StudentUpdate.as_view(),
    #      name='student_update'),
    path('student-update/<pk>/', StudentUpdate.as_view(),
         name='student_update'),
    path('student-delete/<pk>/', StudentDelete.as_view(),
         name='student_delete'),


    path('student-update/', StudentUpdateMain.as_view(),
         name='student_update_main'),
    path('students-info/', StudentsInfo.as_view(),
         name='students_info'),

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

    path('students-json/', JsonStudentsView.as_view(),
         name='students_json'),
    path('students-csv/', CSVView.as_view(),
         name='students_csv'),

    path('send-email/', SendEmail.as_view(),
         name='send_email'),

    path('login/', LoginUser.as_view(),
         name='login'),
    path('logout/', LogOutUser.as_view(),
         name='logout'),
    path('sign-up/', SignUpUser.as_view(),
         name='sign_up'),
    path('activate/<uid>/<token>/', ActivateUser.as_view(),
         name='activate_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
