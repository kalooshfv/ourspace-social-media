from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.authentication import *
from rest_framework.permissions import *
from .forms import *
from rest_framework import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse

user = get_user_model()

class PostItemViews(APIView):
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        content = request.POST.get('content')
        if not content:
            return JsonResponse({'error': 'Content field is required'}, status=400)
        post = Post.objects.create(content=content, creator=request.user)
        
        return JsonResponse({})


    def get(self, request, id=None):
        if id:
            item = Post.objects.select_related('creator').filter(creator = id)
            serializer = PostSerializer(item, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        items = Post.objects.select_related('creator').all()
        serializer = PostSerializer(items, many=True)

        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Post.objects.get(id=id)
        new_content = request.data["content"]
        serializer = PostSerializer(item, data={"content": new_content}, partial=True)
        if serializer.is_valid():
            serializer.save(partial=True)
            return Response({"data": serializer.data})
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id=None):
        item = get_object_or_404(Post, id=id)
        item.delete()
        return Response({"data": "Item Deleted"})

class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

class CustomLoginView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            response = Response({'message': 'Logged in successfully!'})
            return response

        else:
            return Response({'message': 'Invalid username or password'}, status=401)

class CustomUserPatchView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










    
