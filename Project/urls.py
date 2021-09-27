"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ott import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dashboard/', views.adminPage, name="index"),
    path('songs/', views.songsPage, name="songs"),
    path('series/', views.seriesPage, name="movies"),
    path('home/', views.openPage, name="index"),
    path('', views.openPage, name="index"),
    path('mylist/', views.mylistPage, name="mylist"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('vpage/', views.vPage, name="vpage"),
    path('seemore/', views.seemorePage, name="seemore"),
    path('buyplan/', views.buyplanPage, name="buyplan"),
    path('videos/', views.videosPage, name="videos"),
    path('manalytics/', views.manalyticsPage, name="manalytics"),
    path('sanalytics/', views.sanalyticsPage, name="sanalytics"),
    path('songadmin/', views.songadminPage, name="songadmin"),
    path('uploadform/', views.uploadformPage, name="uploadform"),
    path('settings/', views.settingsPage, name="settings"),
    path('view1page/', views.view1page, name="view1page"),
    path('mychannel/', views.mychannel, name="mychannel"),
    path('Analytics/', views.Analytics, name="Analytics"),
    path('Channel_Content/', views.Channel_Content, name="Channel_Content"),
    path('Channel_settings/', views.Channel_settings, name="Channel_settings"),
    path('myprofile/', views.myprofilePage, name="myprofile"),
    path('upload/', views.uploadPage, name="upload"),
    path('subscription/', views.subscriptionPage, name="subscription"),
    path('liked/', views.likedPage, name="liked"),
    path('userlist/', views.userlistPage, name="userlist"),
    path('watchhistory/', views.watchhistoryPage, name="watchhistory"),
    path('admin_videos/', views.admin_videos, name="admin_videos"),
    path('reported_videos/', views.reported_videos, name="reported_videos"),
    path('user_registeration/',views.userReg),
    path('user_login/',views.userLogin),
    path('user_logout/',views.Logout),
    path('channelview/',views.channelview),
    path('user_update/',views.updateView),

    


]
