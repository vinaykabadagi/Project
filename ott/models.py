from django.db import models

class AdminMaster(models.Model):
    admin_un= models.AutoField(primary=True,unique=True,maxlength=8)
    admin_pass=models.CharField(maxlength=10)

class User(models.Model):
    user_un = models.AutoField(primary=True, unique=True, maxlength=8)
    user_name=models.CharField(maxlength=25)
    user_email=models.EmailField(max_length=254,unique=True)
    user_pw = models.CharField(maxlength=12)
    user_ChannelName = models.CharField(maxlength=25,unique=True)

class Channel(models.Model):
    Channel_Name = models.CharField(maxlength=25, unique=True)
    Channel_wh = models.DurationField()
    Channel_sub = models.IntegerField()

class Media(models.Model):
    m_id = models.AutoField(primary=True, unique=True, maxlength=8)
    m_title = models.CharField(maxlength=100)
    m_desc = models.TextField(maxlength=350)
    m_genre = models.CharField(maxlength=20)
    m_cat = models.CharField(maxlength=10)
    m_views = models.IntegerField()
    m_likes = models.IntegerField()
    m_actors = models.CharField()
    m_dir = models.CharField()
    m_date = models.DateField()

class videos(models.Model):
    v_id = models.AutoField(primary=True, unique=True, maxlength=8)
    v_title = models.CharField(maxlength=100)
    v_desc = models.TextField(maxlength=350)
    v_tags = models.CharField(maxlength=200)
    v_cat = models.CharField(maxlength=10)
    v_views = models.IntegerField()
    v_likes = models.IntegerField()
    v_wh = models.IntegerField()

#akshhhhhhh!

# Create your models here.

