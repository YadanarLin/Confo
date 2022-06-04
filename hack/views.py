from django.shortcuts import render,redirect
from hack.models import Article,Comment
from django.http import Http404

# Create your views here.
def index(request):
    if request.method=="POST":
        article=Article(title=request.POST["title"], body=request.POST["text"])
        article.save()
        return redirect(detail,article.id)
    context = {
        "articles": Article.objects.all()
        
    }
    return render(request, 'hack/index.html', context)

def detail(request, article_id):
    try:
        article=Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Review does not exist")
    if request.method=='POST':
        comment=Comment(article=article, text=request.POST['text'])
        comment.save()

    context ={
        "article" : article, #red article represents the one seen in html. blue one represents its value
        "comments":article.comments.order_by('-posted_at')
    }
    
    return render(request,'hack/page2.html',context)