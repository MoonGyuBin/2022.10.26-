from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        
        return Response(ArticleSerializer(Article.objects.all(), many=True).data)
    
    if request.method == "POST":
        article = ArticleSerializer(date=request.data)
        article.is_valid(raise_exception=True)
        article.save()
        return Response(article.data)