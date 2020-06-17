import io

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 定义的系统的方法
from django.utils import timezone
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Question
from polls.serializers import QuestionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def post(request):
    return HttpResponse("post test")

class PollAPIView(APIView):
    def put(self, request, format=None):
        id=self.request.query_params.get('id',0)
        return Response('id' + id)
    def post(self, request):
        question = Question()
        question.question_text = "the question is what?"
        question.pub_date = timezone.now()

        # 序列化方法1
        serializer = QuestionSerializer(question)
        print(serializer.data)
        #反序列化
        stream = io.BytesIO(JSONRenderer().render(serializer.data))
        data = JSONParser().parse(stream)
        print(QuestionSerializer(data).data)


        return Response(serializer.data)