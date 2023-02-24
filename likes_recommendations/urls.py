from django.urls import path
from likes_recommendations import views

urlpatterns = [
    path('likes_recommendations/', views.LikeRecommendationList.as_view()),
    path('likes_recommendations/<int:pk>', views.LikeRecommendationDetail.as_view()),
]