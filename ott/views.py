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