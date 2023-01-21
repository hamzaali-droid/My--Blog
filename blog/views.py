from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from .models import Post, Subscriber
import random
import json

def index(request):
    allPosts = Post.objects.all()
    postLength = len(allPosts)
    try:
        randomPosts = random.sample(list(allPosts), 3)
        post1 = Post.objects.filter(post_id=randomPosts[0].post_id)[0]
        post2 = Post.objects.filter(post_id=randomPosts[1].post_id)[0]
        post3 = Post.objects.filter(post_id=randomPosts[2].post_id)[0]
    except Exception as err:
        randomPosts = random.sample(list(allPosts), postLength)
        post1 = Post.objects.filter(post_id=randomPosts[0].post_id)[0] if (postLength > 0) else None
        post2 = Post.objects.filter(post_id=randomPosts[1].post_id)[0] if (postLength > 1) else None
        post3 = Post.objects.filter(post_id=randomPosts[2].post_id)[0] if (postLength > 2) else None

    if len(Post.objects.all()) > 2:
        topRated = Post.objects.all()[:3]
    else:
        topRated = Post.objects.all()

    params = {
        "post1": post1,
        "post2": post2,
        "post3": post3,
        "topRated": topRated
    }

    return render(request, "index.html", params)

def about(request):
    if len(Post.objects.all()) > 2:
        topRated = Post.objects.all()[:3]
    else:
        topRated = Post.objects.all()
    params = {
        "topRated": topRated
    }

    return render(request, "about.html", params)

def blog(request):
    if len(Post.objects.all()) > 2:
        topRated = Post.objects.all()[:3]
    else:
        topRated = Post.objects.all()
    params = {
        "topRated": topRated
    }

    return render(request, "blog.html", params)

def blogPosts(request):
    posts = []
    for i in Post.objects.all():
        obj = {
            "post_id": i.post_id, "post_tag": i.post_tag,
            "post_thumbnail": json.dumps(str(i.post_thumbnail)), "post_title": i.post_title,
            "post_content": i.post_content, "timestamp": i.timestamp
        }
        posts.append(obj)
    blog_posts = {"posts": posts} 

    return JsonResponse(blog_posts)

def post(request, id):
    if len(Post.objects.all()) > 2:
        topRated = Post.objects.all()[:3]
    else:
        topRated = Post.objects.all()
    post = Post.objects.filter(post_id=id)
    params = {"post": post, "topRated": topRated}

    return render(request, "post.html", params)

def subscribe(request):
    if request.method == "POST":
        subscriber_email = request.POST.get("subscriber-email")
        if (len(Subscriber.objects.filter(subscriber_email=subscriber_email)) > 0 or subscriber_email == ""):
            return JsonResponse({"status": 200, "subscribed": True})
        else:
            subscriber = Subscriber(subscriber_email=subscriber_email)
            subscriber.save()

            try:
                send_mail(
                    "Someone subscribe your website",
                    f"{subscriber_email} subscribe your website",
                    subscriber_email,
                    ["tahatariq1727@gmail.com"]
                )
            except Exception as err:
                pass

            return JsonResponse({"status": 200, "subscribed": False})
        return JsonResponse({})