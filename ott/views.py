from django.shortcuts import render

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
    return render(request, 'web/settings.html')
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
def likedPage(request):
    return render(request, 'web/liked.html')
def userlistPage(request):
    return render(request, 'admin/userlist.html')
def watchhistoryPage(request):
    return render(request, 'web/watchhistory.html')
def reported_videos(request):
    return render(request, 'admin/reported_videos.html')
def admin_videos(request):
    return render(request, 'admin/videos.html')
