from django.shortcuts import render

# Create your views here.
# Genericview API

from .models import Student, Employee
from .serializers import StudentSerializers, EmployeeSerializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin


class StudentListMixins(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
    

class StudentCreateMixins(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentUpdateMixins(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class Student_P_UpdateMixins(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

class StudentRetriveMixins(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)
    

class StudentDeleteMixins(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def delete(self, request, *args, **kwargs):    
        instance = self.get_object()
        # instance.delete()      # hard delete
        instance.is_active=False  # soft delete
        instance.save()     
        return Response({"msg": "data deleted sucessfully"})
    


   
 #########################################################################################################   


# Combined Mixins

class StudentListCreatMixins(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class StudentRetriewUpdateDestroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
    
###########################################################################################################

# Concrete View = In concere view we combine genericview + mixins + http handler (get, post, delete)

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework import status

class StudentConcreateList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentConcreateCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentConcreateRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentConcreateUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentConcreateDelete(DestroyAPIView):  # overridden method              # need to ask saviita
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # instance.delete()
        instance.is_active = False
        return Response({"data deleted sucessfully"})
    

# Mixed Concreate view

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

# Try this



###########################################################################################################

# Viewset

from rest_framework.viewsets import ViewSet


class StudentviewsetList(ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        ser = StudentSerializers(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors)
    
    def update(self, request , pk=None):
        data = request.data
        print(type(data))
        stud_obj = Student.objects.get(id=pk)
        ser = StudentSerializers(instance=stud_obj, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors)
    
    def retrieve(self, request, pk=None):
       
        stud_obj = Student.objects.get(id=pk)
       
        ser = StudentSerializers(stud_obj)
        return Response(ser.data, status=status.HTTP_200_OK)
    

    def destroy(self, request, pk=None):
        stud_obj = Student.objects.get(id=pk)
        # stud_obj.delete()
        stud_obj.is_active=False
        return Response({"msg":"data deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)
    

# Modelviewset
##############################################################################################################

# BaseAuthentication= 



from rest_framework.viewsets import ModelViewSet

# class BaseClass(ModelViewSet):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

# class StudentModelViewSet(ModelViewSet):      #We can inherite Baseclass also
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     # authentication_classes = [BasicAuthentication]
#     authentication_classes = [SessionAuthentication]    # for session authentication we need to do login logout command
#     permission_classes = [IsAuthenticated]
  

class EmployeeModelView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    # authentication_classes = [BasicAuthentication]          # baseauthentication
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [TokenAuthentication]      # from admin page we create create token
    # python manage.py drf_create_token admin          # to hit this command in console we can create token
    permission_classes = [IsAuthenticated]


# to define the global authentication we need to define in setting.py in rest_framenwork

# agar kudka token kud generate karna hai to login view define karna hoga.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def generate_token(request):
    print(request.data)  # {'username': 'Savita', 'password': 'Python@123'}

    username = request.data.get("username") # admin
    password = request.data.get("password") # admin
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, flag = Token.objects.get_or_create(user=user)  # unpacking
    # print(token, flag)  # flag = True when new token is created else False
    return Response({'token': token.key}, status=status.HTTP_200_OK)  





class StudentModelViewSet(ModelViewSet):      #We can inherite Baseclass also
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]    # for session authentication we need to do login logout command
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    

    
   




   





        




      

      
    