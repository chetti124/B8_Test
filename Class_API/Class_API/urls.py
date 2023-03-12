"""Class_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app3 import views
from app3.urls import new_urlpatterns
from django.conf.urls import url
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import views as jwt_views






urlpatterns = [
    path('admin/', admin.site.urls),

    # GenericApiview
    # path('api/stud-generic-view/', views.StudentListMixins.as_view()),
    # path('api/stud-create-view/', views.StudentCreateMixins.as_view()),

    # Neewd to pass id
    # path('api/stud-update-view/<int:pk>/', views.StudentUpdateMixins.as_view()),
    # path('api/stud-P-update-view/<int:pk>/', views.Student_P_UpdateMixins.as_view()),

    # path('api/stud-Retrieve-view/<int:pk>/', views.StudentRetriveMixins.as_view()),
    # path('api/stud-destroy-view/<int:pk>/', views.StudentDeleteMixins.as_view()),


    # Combined Mixins

    # path('api/stud-combined-list-create/', views.StudentListCreatMixins.as_view()),
    # path('api/stud-update-retrieve-destry/<int:pk>/', views.StudentRetriewUpdateDestroy.as_view()),

    # Concreate view

    # path('api/stud-concreate-list/', views.StudentConcreateList.as_view()),
    # path('api/stud-concreate-create/', views.StudentConcreateCreate.as_view()),

    # id required
    # path('api/stud-concreate-retrieve/<int:pk>/', views.StudentConcreateRetrieve.as_view()),
    # path('api/stud-concreate-update/<int:pk>/', views.StudentConcreateUpdate.as_view()),
    # path('api/stud-concreate-delete/<int:pk>/', views.StudentConcreateDelete.as_view()),
    # path('api/stud-viewset-list/', views.UserViewSet.as_view()),

   
    path("api/", include(new_urlpatterns)),
    


    # This url for session authentication
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Tokenauthentication

    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),   # built in token.
    path('api/generate-token/', views.generate_token),     # user defined token.

    # JWT Token

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

   

]
