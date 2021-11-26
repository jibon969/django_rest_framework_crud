from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def student_api(request):
    api_url = {
        'list': 'student-list',
    }

    return Response(api_url)


def home(request):
    return render(request, "home.html")


@api_view(['GET'])
def student_list(request):
    """
    Show all student list
    :param request:
    :return:
    """
    stu = Student.objects.all()
    # print("stu : ", stu)
    serializer = StudentSerializer(stu, many=True)
    # print("serializer : ", serializer)
    return Response(serializer.data)
