import jwt
import pdfkit
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Files, AuthToken
from .serializer import ArchiveSerializer, UserSerializer


class ArchiveAPIFile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user

        a = request.FILES['file']
        file = a.name
        path=r"C:\Users\lucaa\PycharmProjects\drf\drfsite\media\\"+a.name
        Files(user_id_id=user.pk, path=path, my_file=a, name=a.name).save()
        return Response(file)
        # token = request.headers['Authorization']
        #
        # data = jwt.decode(token, key, algorithms="HS256")
        # username = data.get("username")
        #
        # if Users.objects.get(username=username):
        #     UserID = Users.objects.get(username=username).pk
        #
        # a=request.FILES['file']
        # file=a.name
        # Files(user_id_id=UserID,path='',my_file=a,name=a.name).save()
        #
        # # handle_uploaded_file(a)
        # return Response(file)


# class RegistrationAPI(APIView):
#     def post(self,request):
#         name=request.data['username']
#         code=request.data['password']
#
#         User(password=code,username=name).save()
#         return Response({"u":name,"p":code})
#
# class LoginAPI(APIView):
#     def post(self,request):
#         if Users.objects.filter(username=request.data['username'],password=request.data['password']):
#             user = Users.objects.filter(username=request.data['username'], password=request.data['password'])
#
#
#             data = {
#                 "username": user[0].username,
#                 "password": user[0].password,
#             }
#             encoded = jwt.encode(data, key, algorithm="HS256")
#             return Response({"token":encoded})
#         else:
#             return Response({"eror": "Incorrect data"})


class GetFile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        # data = dict()
        # data["name"] = "ThePythonDjango.Com"
        # data["DOB"] = "Jan 10, 2015"
        #
        # template = get_template('C:\Python\\test.html')
        # html = template.render(data)
        # pdf = pdfkit.from_string(html, False)
        #
        # filename = "sample_pdf.pdf"
        #
        # response = HttpResponse(pdf, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        # return response
        # user = request.user
        # user=request.user
        fileName=request.GET.get('file')
        AllFilesUser = Files.objects.get(name=fileName,user_id_id=2)
        # path=r"C:\Users\lucaa\PycharmProjects\drf\drfsite\media\\"+AllFilesUser.name
        path=AllFilesUser.path
        zip_file = open(path,'rb')
        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % AllFilesUser.name
        return response


class ArchiveAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        AllFilesUser = Files.objects.filter(user_id_id=user.pk).values("name","created_at")
        return Response({"files":AllFilesUser})
        # return Response({'files': ArchiveSerializer(AllFilesUser, many=True).data})
        # return Response("succses")
        # jwt.decode(encoded, key, algorithms="HS256")
        # a=request.META.get('HTTP_AUTHORIZATION')
        # if request.headers['Authorization'] is not None:
        #     token=request.headers['Authorization']
        #
        #     data=jwt.decode(token, key, algorithms="HS256")
        #     username=data.get("username")
        #
        #     if Users.objects.get(username=username):
        #         UserID = Users.objects.get(username=username).pk
        #     # return Response(UserID)
        #         AllFilesUser = Files.objects.filter(user_id_id=UserID)
        #         return Response({'files': ArchiveSerializer(AllFilesUser, many=True).data})
        #     else:
        #         return Response("Incorrect token")
        # else:
        #     return Response("Incorrect token")
        # userID=request.GET.get('user')
        # AllFiles=Files.objects.filter(user_id=userID)

# def handle_uploaded_file(f):
#     with open('C:\Python\\'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
