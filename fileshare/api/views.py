from django.contrib.auth.models import User
from .models import Profile, File
from .serializers import UserSerializer, FileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied  

class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication,]

    def perform_create(self, serializer):
        user = self.request.user
        # print("user is",user)
        profile = Profile.objects.get(user=user)
        if profile.user_type == 'ops':
            serializer.save(uploader=user)
        else:
            raise PermissionDenied("You do not have permission to upload files.")

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FileListView(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication,]

    def get_queryset(self):
        user = self.request.user
        print(user)
        profile = Profile.objects.get(user=user)
        if profile.user_type == 'client':
            return File.objects.all()
        else:
            raise PermissionDenied("You do not have permission to view these files.")

class FileDownloadView(APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication,]

    def get(self, request, pk):
        try:
            file = File.objects.get(pk=pk)
        except File.DoesNotExist:
            return Response({"message":"file not found"},status=404)
        profile = Profile.objects.get(user=request.user)
        if profile.user_type == 'client':
            # serializer = FileSerializer(file, context={'request': request})
            # print(serializer.get_file_url)
            # return Response(serializer.data, status=200)
            # file_serializer = FileSerializer(file)
            # download_link = f"/download/{file.file}/secure-link"
            download_link = f"http://127.0.0.1:8000/media/{file.file}"
            return Response({"download-link": download_link, "message": "success"}, status=200)
        else:
            return Response({"message": "You do not have permission to download this files."}, status=403)