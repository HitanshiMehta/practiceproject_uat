from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from practiceapp.Serializers.ArticleSerializer import ArticleSerializer
from practiceapp.models.ArticleModel import Article


class ArticleView(APIView):

        def get(self, request):
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            print("serializer",serializer.data)
            return Response({"articles": serializer.data},status=status.HTTP_200_OK)

        def post(self, request):
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                article_saved = serializer.save()
            return Response({"success": "Article '{}' created successfully".format(article_saved.title)},status=status.HTTP_201_CREATED)

        def put(self,request,pk):
            saved_article=get_object_or_404(Article.objects.all(),pk=pk)
            serializer=ArticleSerializer(instance=saved_article,data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                article_saved=serializer.save()
            return Response({"success : Article '{}' updated successfully".format(article_saved.title)},status=status.HTTP_206_PARTIAL_CONTENT)

        def delete(self,request,pk):
            articles=get_object_or_404(Article.objects.all(),pk=pk)
            articles.delete()
            return Response({"Successfully deleted article id {} ".format(pk)},status=status.HTTP_204_NO_CONTENT)
