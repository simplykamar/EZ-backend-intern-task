from django.contrib.auth.models import User
from .models import Profile, File
from rest_framework import serializers
import os

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'uploader', 'file', 'uploaded_at']
        read_only_fields = ['uploader']

    def validate_file(self, value):
        import os
        ext = os.path.splitext(value.name)[1]  
        valid_extensions = ['.pptx', '.docx', '.xlsx']
        if not ext.lower() in valid_extensions:
            raise serializers.ValidationError('Unsupported file extension. Allowed extensions are: .pptx, .docx, .xlsx')
        return value
    
    def get_file_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return request.build_absolute_uri(obj.file.url)

