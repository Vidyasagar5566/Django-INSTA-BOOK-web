from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg_log, name = 'reg_log'),
    path('main_page', views.main_page, name = 'main_page'),
    path('main_page_L', views.main_page_L, name = 'main_page_L'),
    path('main_page_R', views.main_page_R, name = 'main_page_R'),
    path('register_login', views.reg_log, name = 'reg_log'),
    path('main_page_U', views.main_page_U, name = 'main_page_U'),
    path('del_my_details', views.del_my_details, name = 'del_my_details'),
    path('post_comments', views.post_comments, name = 'post_comments'),
    path('your_profile', views.your_profile, name = 'your_profile'),
    path('register', views.register, name = 'register'),
    path('view_comments', views.view_comments, name = 'view_comments'),
    path('upload_profile_pic', views.profile_pic, name = 'profile_pic'),
    path('user_name-user_details', views.user_name_user_details, name = 'user_name-user_details'),
    path('post_likes', views.post_likes, name = 'post_likes'),

]



#def filter_users(a,b):
    #a -- user_posts
    #b -- users
#    s1={}
#    q=[]
#    for i in a:
#        if i.u_name[-1] == 'U':
#            q.append(i)
#            str0 = ''
#            for j in i.u_name:
#                if j == ':':
#                    break
#                str0 += j
#            s1[str0] = 0
#    p = []
#    for i in b:
#        if i.username == "VidyaSagar":
#            continue
#        if i.username not in s1:
#            p.append(i)
# p-- not profile picture
#    return q,p
