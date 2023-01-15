from django.db import models
# Create your models here.


class Card(models.Model):
    question = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    answer_code = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.question
