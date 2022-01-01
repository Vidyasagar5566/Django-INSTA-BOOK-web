from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg_log, name = 'reg_log'),
    path('main_page_L', views.main_page_L, name = 'main_page_L'),
    path('main_page_R', views.main_page_R, name = 'main_page_R'),
    path('register_login', views.reg_log, name = 'reg_log'),
    path('upload', views.upload, name = 'upload'),
    path('main_page_U', views.main_page_U, name = 'main_page_U'),
    path('del_my_details', views.del_my_details, name = 'del_my_details'),
    path('comment', views.comment, name = 'comment'),
    path('post_comments', views.post_comments, name = 'post_comments'),
]








