from rest_framework import status
from.models import Stu_Data,Branches
from .serializers import StudentSerializer,BranchesSerializer,StuSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse


# Create your views here.


class BranchAPI(APIView):
    def post(self, request, format=None):
        grpserializer = BranchesSerializer(data=request.data)
        if grpserializer.is_valid():
            branch = grpserializer.save()
        request.data['Branches'] = branch.id
        stuserializer = StuSerializer(data=request.data)
        if stuserializer.is_valid():
         stuserializer.save()
        return Response(stuserializer.data)


    def get(self, request, s,format=None):
        branch = Branches.objects.filter(branch=s)
        serializer = BranchesSerializer(branch, many=True)
        return Response(serializer.data)

    def patch(self,request, id,format=None):
        data = Branches.objects.get(id=id)
        serializer = BranchesSerializer(instance=data, data=request.data)
        if serializer.is_valid():
            try:
                if id < 20:
                    stu = Branches.objects.get(id=id)

            except Exception as e:
                return Response({'message': 'id not exist'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
        return Response(serializer.data)


    def delete(self,request, id,format=None):
        try:
            event = Branches.objects.filter(id=id)
        except Exception as e:
            return Response({'message': 'Branch not exist'}, status=status.HTTP_400_BAD_REQUEST)
        # event = Branches.objects.filter(branch=s)
        event.delete()
        return Response('Deleted')

class StubranchAPI(APIView):
    def get(self, request, format=None):
        student = Stu_Data.objects.filter(Branches_id__branch='EEE').values_list('name',flat=True)
        serializer = StuSerializer(student, many=True)
        return JsonResponse(serializer.data)


class StudentAPI(APIView):

    def get(self, request, format=None):
        student = Stu_Data.objects.all()
        serializer = StudentSerializer(student, many=True,context={'request':request}).data
        return Response(serializer.data)

    def patch(self,request,id,format=None):
        stu = Stu_Data.objects.get(id=id)
        serializer = StudentSerializer(instance=stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def delete(self,request,id,format=None):
        try:
            stu = Stu_Data.objects.get(id=id)
        except Exception as e:
            return Response({'message': 'id not exist'}, status=status.HTTP_400_BAD_REQUEST)
        stu.Branches.delete()
        return Response({'message': 'data deleted successfully'}, status=status.HTTP_200_OK)
