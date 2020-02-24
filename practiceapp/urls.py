from django.urls import path, include

from practiceapp.views.ArticleView import ArticleView
from practiceapp.views.ProductView import ProductView
from practiceapp.views.MovieVIew import MovieDetailsView
from practiceapp.views.PlaceView import PlaceViews
from practiceapp.views.UserView import UserView

urlpatterns = [
    path('place/', PlaceViews.as_view()),
    path('place/<str:pk>', PlaceViews.as_view()),
    path('movie/', MovieDetailsView.as_view()),
    path('product/', ProductView.as_view()),
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
    path('user/', UserView.as_view())
]