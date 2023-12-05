from typing import Any
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        for review in Review.object.filter():
            reviews.append(review.review_text)
        return Response({'reviews': 'success'})
        
class CreateAppDevClubReview(APIView):
    def post(self, request):
        review = request.data('review')
        if review == "":
            return Response({'message': 'failure'})
        else:
            new_database_entry = Review(review)
            return Response({'message' : 'Review added'})
        

    


        