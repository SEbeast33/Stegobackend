from django.shortcuts import render
from .serializers import PostSerializer,VideoSerializer
from .models import Post,Video
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .Steganography import *
# from .VideoStego import *
# from .NewVideoStego import *
from django.conf import settings
from django.http import HttpResponse
import random


# class PostView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         posts_serializer = PostSerializer(data=request.data)
#         if posts_serializer.is_valid():
#             posts_serializer.save()
#             data=posts_serializer.data['title']
#             img=posts_serializer.data['image']
           
#             print(data)
#             path=hide_message_in_image(img,data)
           
#             print(path)
#             # print(text)
#             return Response({"filename": path}, status=status.HTTP_201_CREATED)
           
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def generate_random_key(self):
        # Generate a random key of length 4 with numbers between 100 and 999
        return [random.randint(100, 999) for _ in range(4)]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            data = posts_serializer.data['title']
            img = posts_serializer.data['image']
            
            # Generate a random key
            key = self.generate_random_key()
            print(key)
            # Pass the random key to the hide_message_in_image function
            path = hide_message_in_image(img, data, key)
           
            print(path)
            return Response({"filename": path,'key':key}, status=status.HTTP_201_CREATED)
           
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class VideoView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         posts = Video.objects.all()
#         serializer = VideoSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
        
            
#         posts_serializer = VideoSerializer(data=request.data)
#         if posts_serializer.is_valid():
#             posts_serializer.save()
#             data=posts_serializer.data['title']
#             video=posts_serializer.data['video']
#             frame_no=posts_serializer.data['frame']
#             password=posts_serializer.data['password']
#             frame=encode_vid_data(video,data,frame_no,password)
#             print(frame)
            
#             return Response({"filename": video}, status=status.HTTP_201_CREATED)
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



class PostDecodeView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            
            img=posts_serializer.data['image']
            img_url='https://res.cloudinary.com/dkzbn6s7o/image/upload/v1714160279/hidden_image.png'
            text=extract_message_from_image(img_url)
            print(text)
            # print(text)
            return Response({"decodedtext": text}, status=status.HTTP_201_CREATED)
            
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DecryptWithLinkView(APIView):
    def post(self, request):
        # Get the link and key array from the request data
        link = request.data.get('link')
        key_array = request.data.get('key_array')
        key = [int(x) for x in key_array.split(',')]
        print(key)
        


        # Validate the input
        if not all([link, key_array]):
            return Response({'error': 'Missing required data'}, status=status.HTTP_400_BAD_REQUEST)

        # Process the input data (e.g., save to database, perform operations)
        # In this example, we'll just return the received data

        text=extract_message_from_image(link,key)
        return Response({
            'decodedtext': text,
            
        }, status=status.HTTP_201_CREATED)