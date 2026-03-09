from django.http import HttpResponse
from django.shortcuts import render

from .serializers import UserSerializer
from .serializers import CourseSerializer
from .models import Course
from .models import User
from rest_framework.renderers import JSONRenderer

# Create your views here.

def user_list(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    json_render = JSONRenderer().render(serializer.data)
    return HttpResponse(json_render, content_type='application/json')

def course_list(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    json_render = JSONRenderer().render(serializer.data)
    return HttpResponse(json_render, content_type='application/json')
