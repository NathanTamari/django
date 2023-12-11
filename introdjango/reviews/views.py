from typing import Any
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        for review in Review.objects.all():
            reviews.append(review.review_text)
        return Response({'reviews': reviews})
        
class CreateAppDevClubReview(APIView):
    def post(self, request):
        reviews = request.data.getlist('review', [])
        if not reviews:
            return Response({'message': 'failure'})
        
        for text in reviews:
            if text != "":
                new_database_entry = Review.objects.create(review_text=text)
        
        return Response({'message' : 'Review added'})
