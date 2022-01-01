from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from . models import user_uploads

def filter_users(a,b):
    #a -- user_uploads
    #b -- users
    s1={}
    for i in a:
        s1[i.u_name] = 0
    p = []
    for i in b:
        if i.username in s1 or i.username == "VidyaSagar":
            continue
        p.append(i)
    return p

def comments(comment_str):
    lst = []
    str0 = ""
    for i in comment_str:
        if i == "$":
            lst.append(str0)
            str0 = "@"
            continue
        str0 = str0 + i
    lst.reverse()
    lst.append(str0)
    return lst, "NO OF COMMENTS: " + str(len(lst)-1)




# Create your views here.
def reg_log(request):
    return render(request, 'login,register.html')

def comment(request):
    return render(request, 'comments.html')

def main_page_L(request):
    if request.method == 'POST':
        username = request.POST["input1"]
        password = request.POST["input2"]
        user = auth.authenticate(username= username, password = password)
        if user:
            lst0 = user_uploads.objects.all()
            lst1 = User.objects.all()
            dests, count = [], -1
            user_details0, user_details1 = 0, 0
            for i in lst0:
                if i.u_name == username:
                    i.comments, no_of_comms = comments(i.comments)
                    i.comments.insert(0,no_of_comms)
                    user_details0 = i
                    continue
                i.comments, no_of_comms = comments(i.comments)
                i.comments.insert(0,no_of_comms)
                dests.append(i)

            for i in lst1:
                if i.username == username:
                    user_details1 = i
                count += 1
            un_upload_users = filter_users(lst0,lst1)
            dests.reverse()
            return render(request, 'main_page_L.html',
                              {'dests':dests,'user_details0':user_details0,'user_details1':user_details1,'count':count,'un_upload_users':un_upload_users})

        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login,register.html')
    else:
        return render(request, 'login,register.html')


def main_page_R(request):

    if request.method == 'POST':
        username = request.POST["input0"]
        first_name = request.POST["input1"]
        last_name = request.POST["input2"]
        password1 = request.POST["input3"]
        password2 = request.POST["input4"]
        email = request.POST["input5"]

        if username and first_name and last_name and password1 and password2 and email:
            if password1 != password2:
                messages.info(request, "password1 and password2 aren't matching")
                return render(request, 'login,register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "UserName was already taken, please register with another user name")
                return render(request, 'login,register.html')
            elif password1 == password2:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                lst = user_uploads.objects.all()
                lst0 = User.objects.all()
                dests = []
                for i in lst:
                    if i.u_name == user.username:
                        continue
                    i.comments, no_of_comms = comments(i.comments)
                    i.comments.insert(0, no_of_comms)
                    dests.append(i)
                dests.reverse()
                un_upload_users = filter_users(lst, lst0)
                return render(request, 'main_page_R.html', {'user':user, 'dests' : dests,'un_upload_users':un_upload_users})
            else:
                return render(request, 'login,register.html')
        else:
            messages.info(request, "Fill All The Details While Registering")
            return render(request, 'login,register.html')
    else:
        return render(request, 'login,register.html')
def upload(request):
    return render(request, 'upload.html')

def main_page_U(request):
    if request.method == 'POST':
        table = user_uploads()
        table.u_name = request.POST["input1"]
        try:
            table.U_profile_pic = request.FILES["input2"]
            table.U_main_pic = request.FILES["input3"]
            table.caption = request.POST["input4"]
        except:
            messages.info(request, "upload all the details")
            return render(request, 'upload.html')
        lst = user_uploads.objects.all()
        lst0 = User.objects.all()
        dests, count = [], 0
        user1 = 0
        for i in lst0:
            if i.username == table.u_name:
                user1 = i
                break
        if user1 == 0:
            messages.info(request, "UserName wasn't matched")
            return render(request, 'upload.html')

        # searching if user details already existed
        for i in lst:
            if i.u_name == table.u_name:
                messages.info(request, "some thing went wrong user details already existed")
                return render(request, 'upload.html')
        # _________

        table.save()
        lst = user_uploads.objects.all()
        user = 0
        for i in lst:
            if i.u_name == table.u_name:
                i.comments, no_of_comms = comments(i.comments)
                i.comments.insert(0, no_of_comms)
                user = i
                continue
            i.comments, no_of_comms = comments(i.comments)
            i.comments.insert(0, no_of_comms)
            dests.append(i)
            count+=1
        if user == 0:
            messages.info(request, "uploaded details doesn't saved upload again")
            return render(request, 'upload.html')
        dests.reverse()
        un_upload_users = filter_users(lst, lst0)
        return render(request, 'main_page_U.html',{'dests':dests,'user1':user1,'user':user,'count':count,'un_upload_users':un_upload_users} )
    return render(request, 'upload.html')

def del_my_details(request):
    if request.method == 'POST':
        username = request.POST["input1"]
        lst1 = user_uploads.objects.all()
        dests ,exist= [],0
        for i in lst1:
            if i.u_name == username:
                exist=1
                continue
            i.comments, no_of_comms = comments(i.comments)
            i.comments.insert(0, no_of_comms)
            dests.append(i)
        if exist == 0:
            messages.info(request, "UserName wasn't matched")
            return render(request, 'del_my_details.html')
        dests.reverse()
        del_my_details = user_uploads.objects.get(u_name = username)
        del_my_details.delete()
        lst0 = User.objects.all()
        user = 0
        for i in lst0:
            if i.username == username:
                user = i
        if user == 0:
            messages.info(request, "UserName wasn't matched")
            return render(request, 'del_my_details.html')
        un_upload_users = filter_users(dests, lst0)
        return render(request, 'main_page_R.html', {'user':user, 'dests' : dests,'un_upload_users':un_upload_users})
    else:
        return render(request, 'del_my_details.html')

def post_comments(request):
    if request.method == 'POST':
        #username1 = user
        #username2 = user_uploads
        username1 = request.POST["input1"]
        password = request.POST["input2"]
        username2 = request.POST["input3"]
        comment = request.POST["input4"]
        user = auth.authenticate(username = username1, password = password)
        lst1 = user_uploads.objects.all()
        if not user:
            messages.info(request, "ReEnter Your Password!! it's Wrong")
            return render(request, 'comments.html')
        for i in lst1:
            if i.u_name == username2:
                break
        else:
            messages.info(request, "correctly mention Commenter User Name ")
            return render(request, 'comments.html')

        user = user_uploads.objects.get(u_name = username2)
        p=username1.upper()
        user.comments = user.comments + p + " : " + comment + "$"
        user.save()

# from login function

        lst0 = user_uploads.objects.all()
        lst1 = User.objects.all()
        dests, count = [], -1
        user_details0, user_details1 = 0, 0
        for i in lst0:
            if i.u_name == username1:
                i.comments, no_of_comms = comments(i.comments)
                i.comments.insert(0, no_of_comms)
                user_details0 = i
                continue
            i.comments, no_of_comms = comments(i.comments)
            i.comments.insert(0, no_of_comms)
            dests.append(i)

        for i in lst1:
            if i.username == username1:
                user_details1 = i
            count += 1
        un_upload_users = filter_users(lst0, lst1)
        dests.reverse()
        return render(request, 'main_page_L.html',
                      {'dests': dests, 'user_details0': user_details0, 'user_details1': user_details1, 'count': count, 'un_upload_users': un_upload_users})

    return render(request, 'comments.html')


