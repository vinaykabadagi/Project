from django.db import models

class AdminMaster(models.Model):
    admin_un= models.Autofield(primary=True,unique=True,maxlength=8)
    admin_pass=models.Charfield(maxlength=10)

class User(models.Model):
    user_un = models.Autofield(primary=True, unique=True, maxlength=8)
    user_name=models.Charfield(maxlength=25)
    user_email=models.models.EmailField(max_length=254,unique=True)
    user_pw = models.Charfield(maxlength=12)
    user_ChannelName = models.Charfield(maxlength=25,unique=True)

class Channel(models.Model):
    Channel_Name = models.Charfield(maxlength=25, unique=True)
    Channel_wh = models.DurationField()
    Channel_sub = models.Integerfield()

class Media(models.Model):
    m_id = models.Autofield(primary=True, unique=True, maxlength=8)
    m_title = models.Charfield(maxlength=100)
    m_desc = models.TextField(maxlength=350)
    m_genre = models.Charfield(maxlength=20)
    m_cat = models.Charfield(maxlength=10)
    m_views = models.Integerfield()
    m_likes = models.Integerfield()
    m_actors = models.Charfield()
    m_dir = models.Charfield()
    m_date = models.DateField()

class videos(models.Model):
    v_id = models.Autofield(primary=True, unique=True, maxlength=8)
    v_title = models.Charfield(maxlength=100)
    v_desc = models.TextField(maxlength=350)
    v_tags = models.Charfield(maxlength=200)
    v_cat = models.Charfield(maxlength=10)
    v_views = models.Integerfield()
    v_likes = models.Integerfield()
    v_wh = models.Integerfield()


# Create your models here.

