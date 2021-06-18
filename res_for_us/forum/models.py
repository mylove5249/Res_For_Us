# Create your models here.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls.base import translate_url
from django.utils.text import slugify
from .fields import ThumbnailImageField

class Forum(models.Model):
    message = models.TextField(max_length=5000,null=True)
    subject = models.CharField(max_length=255)
    address = models.TextField(max_length=1000)
    mainphoto = ThumbnailImageField(upload_to='photo/%Y/%m')
    cleaned = models.IntegerField()
    taste = models.IntegerField()
    kindness = models.IntegerField()
    last_updated = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(verbose_name="SLUG", max_length=100, allow_unicode=True, help_text="one word for title alias")
    writter = models.ForeignKey(User, related_name='forums',on_delete=models.CASCADE, null=True)    

    class Meta:
        verbose_name = 'forum'
        verbose_name_plural = 'forumss'
        db_table = 'forum_forum'
        ordering = ('-last_updated',) # modify)dt를 기준으로 기본 오름차순 정렬, ','가 있어야 튜플로 처리, '-' 추가시 내림차순
    
    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("forum:forum_detail", args=(self.slug,)) # /blog/this-is-title

    def get_previous(self): # 이전 글 가져오기
        return self.get_previous_by_last_updated()

    def get_next(self): # 다음 글 가져오기
        return self.get_next_by_last_updated()

    # 상속 받은 메서드 재정의
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject, allow_unicode=True) 
        super().save(*args, **kwargs)

class Reply(models.Model):
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User, null=True, related_name='posts',on_delete=models.CASCADE)
    updated_at = models.DateField(null = True)
    updated_by=  models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)

