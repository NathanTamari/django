from django.urls import path
from .views import AppDevClubReviewsView, CreateAppDevClubReview

urlpatterns = [
    path('reviews/', AppDevClubReviewsView.as_view()),
    path('add_review/', CreateAppDevClubReview.as_view())
]
