from rest_framework import serializers
from .models import Post
from .models import Video

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'video', 'password', 'frame']
    