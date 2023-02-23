from django.shortcuts import render, redirect, reverse
from tweets.models import Tweet
from django.contrib.auth.models import User

# Create your views here.

def new_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    context = {
        "tweets" : tweets,
    }
    return render(request, 'tweet.html', context=context)
def add_tweet(request):
    if request.method == "POST":
        content  = request.POST['content']
        data = Tweet(content=content)
        data.save()
        return redirect(reverse("tweets"))
    return render(request, '404.html')

def view_author(request, author_id):
    tweets = Tweet.objects.filter(author_id=author_id)
    context = {
        "tweets" : tweets
    }
    return render(request, "view_author.html", context=context)







