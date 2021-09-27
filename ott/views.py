from django.http.response import HttpResponse
from django.shortcuts import render
from ott.models import AdminMaster
from ott.models import User
from django.contrib.auth import authenticate, login


# Create your views here.


def openPage(request):
    return render(request, 'web/home.html')


def seriesPage(request):
    return render(request, 'web/series.html')


def songsPage(request):
    return render(request, 'web/songs.html')


def mylistPage(request):
    return render(request, 'web/mylist.html')


def loginPage(request):
    return render(request, 'web/login.html')


def registerPage(request):
    return render(request, 'web/register.html')


def vPage(request):
    return render(request, 'web/vpage.html')


def seemorePage(request):
    return render(request, 'web/seemore.html')


def removeAdsPage(request):
    return render(request, 'web/buy.html')


def videosPage(request):
    return render(request, 'web/videos.html')


def settingsPage(request):
    jsonData = User.objects.filter(
        user_email=request.session["Email"]).values()
    data = (jsonData)
    print(type(data))
    print(data)
    articles_list = list(data)
    print(articles_list)
    print(type(articles_list[0]))

    return render(request, 'web/settings.html', articles_list[0])
    



def view1page(request):
    return render(request, 'web/view1page.html')


def mychannel(request):
    return render(request, 'web/mychannel.html')


def Channel_Content(request):
    return render(request, 'web/Channel_Content.html')


def Channel_settings(request):
    return render(request, 'web/Channel_settings.html')


def Analytics(request):
    return render(request, 'web/Analytics.html')


def myprofilePage(request):
    return render(request, 'web/myprofile.html')


def adminPage(request):
    return render(request, 'admin/dashboard.html')


def uploadPage(request):
    return render(request, 'admin/upload.html')

def subscriptionPage(request):
    return render(request, 'web/subscription.html')


def likedPage(request):
    return render(request, 'web/liked.html')


def userlistPage(request):
    return render(request, 'admin/userlist.html')


def watchhistoryPage(request):
    return render(request, 'web/watchhistory.html')

def channelview(request):
    return render(request,'web/channelview.html')
    
def reported_videos(request):
    return render(request, 'admin/reported_videos.html')


def admin_videos(request):
    return render(request, 'admin/videos.html')



# def userReg(request):
#     lclId = AdminMaster.objects.count()
#     lclId = lclId + 1;
#     AdminMaster.objects.create(
#         admin_id = lclId,
#         admin_un = request.POST[]
#     )


def userReg(request):
    if User.objects.filter(user_un=request.POST['username']).exists():
        return HttpResponse("10")
    else:
        lclId = User.objects.count()
        lclId = lclId + 1
        User.objects.create(
            user_id=lclId,
            user_un=request.POST['username'],
            user_name=request.POST["name"],
            user_email=request.POST['email-id'],
            user_phone=request.POST['phoneno'],
            user_pw=request.POST['password'],
            user_status="0",
            user_ChannelName=""
        )
        return HttpResponse("1")


def userLogin(request):
    if User.objects.filter(user_un=request.POST['name'], user_pw=request.POST['password']).exists():
        jsonData = User.objects.filter(user_un=request.POST['name']).values()
        data = list(jsonData)
        listValue = data[0]
        request.session['Email'] = listValue['user_email']
        print(request.session)
        return HttpResponse("11")

    else:
        return HttpResponse("12")


def Logout(request):
    try:
        del request.session['Email']
    except KeyError:
        pass
    return HttpResponse("29")
