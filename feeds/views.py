from django.shortcuts import get_object_or_404, render, redirect

from insta.settings import AUTH_USER_MODEL
from .models import Feed, Comment, Hashtag
from accounts.models import User
from .forms import FeedForm, CommentForm

# Create your views here.
def index(request):
    feeds = Feed.objects.all().order_by('-pk')
    context = {
        'feeds': feeds,
    }
    return render(request,'feeds/index.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FeedForm(request.POST, request.FILES)
            if form.is_valid():
                new_feed = form.save(commit = False)
                new_feed.user = request.user
                words = new_feed.content.split()
                new_feed.save()
                # 해시태그 구현
                hashtag = [word[1:] for word in words if word[0] == '#']
                for hash in hashtag:
                    if Hashtag.objects.filter(content=hash).exists():
                        new_hash = Hashtag.objects.get(content=hash)
                        new_feed.hashtag.add(new_hash)
                    else:
                        new_hash = Hashtag(content=hash)
                        new_hash.save()
                        new_feed.hashtag.add(new_hash)
                # 인물태그 구현
                usertag = [word[1:] for word in words if word[0] == '@']
                for tag in usertag:
                    user = User.objects.get(username=tag)
                    new_feed.tag_users.add(user)
                return redirect('feeds:index')
        elif request.method == 'GET':
            form = FeedForm()
            context = {
                'form': form,
            }
            return render(request, 'feeds/new.html', context)
    return redirect('accounts:login')

def detail(request, feed_pk):
    if request.method == 'GET':
        feed = get_object_or_404(Feed, pk=feed_pk)
        user = get_object_or_404(User,pk=feed.user_id)
        comments = feed.feed_comments.all()
        form = CommentForm()
        context = {
            'feed': feed,
            'comments': comments,
            'form': form,
            'user':user,
        }
        return render(request, 'feeds/detail.html', context)


def update(request, feed_pk):
    feed = get_object_or_404(Feed, pk=feed_pk)
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FeedForm(request.POST, request.FILES, instance=feed)
            if form.is_valid():
                form.save()
                return redirect('feeds:detail', feed.pk)
            
        else:
            form = FeedForm(instance=feed)
        context = {
            'form': form,
            'feed': feed,
        }
        return render(request, 'feeds/update.html', context)
    return redirect('accounts:login')


def delete(request, feed_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            feed = get_object_or_404(Feed, pk=feed_pk)
            feed.delete()
            return redirect('feeds:index')
    return redirect('accounts:login')

def like(request, feed_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            feed = get_object_or_404(Feed,pk=feed_pk)
            user = request.user

            if feed.like_users.filter(pk=user.pk).exists():
                feed.like_users.remove(user)
            
            else:
                feed.like_users.add(user)
            
            return redirect('feeds:index')
    return redirect('accounts:login')

def comment_create(request, feed_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            feed = get_object_or_404(Feed, pk=feed_pk)
            form = CommentForm(data=request.POST)
            comments = Comment.objects.filter(user=request.user)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.feed = feed
                comment.save()
                return redirect('feeds:detail', feed_pk)
            context = {
                'feed': feed,
                'comments': comments,
                'form': form,
            }
            return render(request, 'feeds/detail.html', context)
    return redirect('accounts:login')

def comment_update(request, feed_pk, comment_pk):
    if request.user.is_authenticated:
        feed = get_object_or_404(Feed, pk=feed_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.method == 'POST':
            form = CommentForm(instance=comment,data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('feeds:detail', feed_pk)
            context = {
                'feed': feed,
                'comment': comment,
                'form': form
            }
            return render(request, 'feeds/update_comment.html', context)
        
        elif request.method == 'GET':
            form = CommentForm(instance=comment)
            context = {
                'feed': feed,
                'comment': comment,
                'form': form,
            }
            return render(request, 'feeds/update_comment.html', context)
    return redirect('accounts:login')

def comment_delete(request, feed_pk, comment_pk):
    if request.user.is_authenticated:
        if request.method=='POST':
            comment = get_object_or_404(Comment, pk = comment_pk)
            comment.delete()
            return redirect('feeds:detail', feed_pk)
    return redirect('accounts:login')

def bookmark(request, feed_pk):
    if request.user.is_authenticated:
        if request.method=='POST':
            feed = get_object_or_404(Feed, pk=feed_pk)
            user = request.user
            if feed.bookmark_user.filter(pk=user.pk).exists():
                feed.bookmark_user.remove(user)
            else:
                feed.bookmark_user.add(user)

            return redirect('feeds:index')
    return redirect('accounts:login')