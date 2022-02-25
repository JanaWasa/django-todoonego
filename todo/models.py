from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    # blank means that this field is optional, don't need to be filled in
    memo = models.TextField(blank=True)
    # This is at specifica time this was created, in contrast to DateField()
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    # one to many relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
