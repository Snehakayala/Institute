from rest_framework import serializers
from .models import Stu_Data,Branches

class StuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stu_Data
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    Branches=serializers.SerializerMethodField()
    class Meta:
        model = Stu_Data
        fields = '__all__'

    def get_Branches(self,obj):
            return obj.Branches.branch

class BranchesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Branches
            fields = '__all__'

