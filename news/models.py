from django.db import models

# Create your models here.

class News(models.Model):
    info_url = models.CharField(max_length=100)
    info_time = models.TimeField()
    info_text = models.TextField()
    get_time = models.DateField()
    data_source = models.CharField(max_length=20)

    #
    # def __str__(self):
    #     return self.data_source

    class Meta:
        app_label = 'news'


class Comment(models.Model):
    comment_text = models.TextField()
    comment_time = models.DateTimeField()
    commenter = models.CharField(max_length=30)
    # comment_article = models.ForeignKey()