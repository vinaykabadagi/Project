from django.db import models


class AdminMaster(models.Model):
    admin_id = models.AutoField(primary_key=True, unique=True)
    admin_un = models.CharField(unique=True, max_length=8)
    admin_pass = models.CharField(max_length=10)
    admin_status = models.CharField(max_length=8)


class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    user_un = models.CharField(unique=True, max_length=20)
    user_name = models.CharField(max_length=25)
    user_email = models.EmailField(unique=True)
    user_phone = models.IntegerField(unique=True, default=1)
    user_pw = models.TextField(max_length=100)
    user_ChannelName = models.CharField(max_length=25, unique=True)
    user_status = models.CharField(max_length=8)
    user_image=models.ImageField(upload_to="ott/static/media/images_users", default="ott/static/media/myprofile.png")


class Channel(models.Model):
    channel_Name = models.CharField(max_length=25, unique=True)
    channel_wh = models.DurationField()
    channel_sub = models.IntegerField()
    channel_status = models.CharField(max_length=8)


class Media(models.Model):
    m_id = models.AutoField(primary_key=True, unique=True)
    m_title = models.CharField(max_length=100)
    m_desc = models.TextField(max_length=350)
    m_genre = models.CharField(max_length=20)
    m_cat = models.CharField(max_length=10)
    m_views = models.IntegerField()
    m_likes = models.IntegerField()
    m_actors = models.CharField(max_length=200)
    m_dir = models.CharField(max_length=200)
    m_date = models.DateField()
    m_status = models.CharField(max_length=8)
    m_movies = models.ImageField(upload_to="ott/static/media/images_movies")
    m_series = models.ImageField(upload_to="ott/static/media/images_series")


class videos(models.Model):
    v_id = models.AutoField(primary_key=True, unique=True)
    v_title = models.CharField(max_length=100)
    v_desc = models.TextField(max_length=350)
    v_tags = models.CharField(max_length=200)
    v_cat = models.CharField(max_length=10)
    v_views = models.IntegerField()
    v_likes = models.IntegerField()
    v_wh = models.IntegerField()
    v_image = models.ImageField(upload_to="ott/static/media/images_videos")
    v_status = models.CharField(max_length=8)