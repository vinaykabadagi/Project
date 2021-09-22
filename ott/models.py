from django.db import models


class AdminMaster(models.Model):
    admin_un = models.CharField(primary_key=True, unique=True, max_length=8)
    admin_pass = models.CharField(max_length=10)


class User(models.Model):
    user_un = models.AutoField(primary_key=True, unique=True, max_length=8)
    user_name = models.CharField(max_length=25)
    user_email = models.EmailField(max_length=254, unique=True)
    user_pw = models.CharField(max_length=12)
    user_ChannelName = models.CharField(max_length=25, unique=True)


class Channel(models.Model):
    Channel_Name = models.CharField(max_length=25, unique=True)
    Channel_wh = models.DurationField()
    Channel_sub = models.IntegerField()


class Media(models.Model):
    m_id = models.AutoField(primary_key=True, unique=True, max_length=8)
    m_title = models.CharField(max_length=100)
    m_desc = models.TextField(max_length=350)
    m_genre = models.CharField(max_length=20)
    m_cat = models.CharField(max_length=10)
    m_views = models.IntegerField()
    m_likes = models.IntegerField()
    m_actors = models.CharField(max_length=200)
    m_dir = models.CharField(max_length=200)x
    m_date = models.DateField()


class videos(models.Model):
    v_id = models.AutoField(primary_key=True, unique=True, max_length=8)
    v_title = models.CharField(max_length=100)
    v_desc = models.TextField(max_length=350)
    v_tags = models.CharField(max_length=200)
    v_cat = models.CharField(max_length=10)
    v_views = models.IntegerField()
    v_likes = models.IntegerField()
    v_wh = models.IntegerField()

# akshhhhhhh!

# Create your models here.
