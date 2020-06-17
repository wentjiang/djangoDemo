from rest_framework import serializers

from polls.models import Question

#第一种序列化方法
#Serializing objects
class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()


#第二种序列化方法
#ModelSerializer
class QuestionModellSerializer(serializers.ModelSerializer):
    #添加额外的字段
    test_field = serializers.CharField(source='test_field', read_only=True)
    class Meta:
        model = Question
        fields = ['question_text','pub_date']
        #fields = ['id', 'account_name', 'users', 'created']
        #fields = '__all__'
        #exclude = ['users']