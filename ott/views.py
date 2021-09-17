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
