from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    blogimage = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:50]


    def pub_date_display(self):
        return self.pub_date.strftime('%b %e %Y')