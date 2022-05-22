from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class SavePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.URLField(default='https://google.com/')
    pwd = models.CharField(max_length=1000)
    hide_pwd = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
