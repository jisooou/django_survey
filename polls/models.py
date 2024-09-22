from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.
class Question(models.Model): #설문조사 주제 table 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    was_published_recently.boolean = True
    # 정렬이 될 수 있도록 설정함.
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model): #설문조사 선택지 table
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

