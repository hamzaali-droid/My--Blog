from django.db import models

class Post(models.Model):
    post_id = models.AutoField(auto_created=True, primary_key=True)
    post_tag = models.CharField(max_length=40, default="")
    post_title = models.CharField(max_length=200, default="")
    post_thumbnail = models.ImageField(upload_to="Images", default="")
    post_content = models.TextField(max_length=10000, default="")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Post-{self.post_id}:{self.post_title}"

class Subscriber(models.Model):
    subscriber_id = models.AutoField(auto_created=True, primary_key=True)
    subscriber_email = models.CharField(max_length=30, default="example@gmail.com")

    def __str__(self):
        return f"{self.subscriber_email}: Subscribe your website"

        
