from django.shortcuts import render
from hack.models import Article

# Create your views here.
def index(request):
    context = {
        "articles": Article.objects.all()
        
    }
    
    return render(request, 'hack/index.html', context)

def detail(request,article_id):
    context ={
        "article_id" : article_id
    }
    return render(request,"hack/page2.html",context)
