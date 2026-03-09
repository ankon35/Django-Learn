from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100, write_only=True)


class CourseSerializer(serializers.Serializer):
    course_name = serializers.CharField(max_length=100)
    course_code = serializers.CharField(max_length=10)
    description = serializers.CharField()


