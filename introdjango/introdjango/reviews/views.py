from typing import Any
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AppDevClubReviewsView(APIView):
    def __init__(self):
        self.reviews = [
            'join appdev',
            'app dev is fun'
        ]
        

    def get(self, request):
        return Response({'reviews': self.reviews})
    
    def post(self, request):
        data = request.data.get('review')

        if data:
            self.reviews.append(data)
            return Response({'message': 'success'})
        else:
            return Response({'message': 'No review'}, status=400)

    


        