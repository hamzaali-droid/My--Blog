from django.contrib import admin
from .models import Post, Subscriber

admin.site.register(Subscriber)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('javascript/tiny.js',)