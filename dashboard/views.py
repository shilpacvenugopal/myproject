from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Table2, Table1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
import json

class Table2Api(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=None):
        if id is not None:
            table2_data = Table2.objects.get(id=id)
            data=self.create_resp(table2_data)
        else:
            table2_data = Table2.objects.all()
            data = []
            for obj in table2_data:
                data.append(self.create_resp(obj))
        return JsonResponse(data, safe=False)

    def create_resp(self,obj):
        return ({
                'id': str(obj.id),
                'student_id': str(obj.student_id),
                'student_name': obj.student.name,
                'student_father_name': obj.student.father_name,
                'student_mother_name': obj.student.mother_name,
                'address': obj.address,
                'gender': obj.gender,
                'age': obj.age,
                'blood_group': obj.blood_group
            })

    def post(self, request):
        data = json.loads(request.body)
        try:
            table1=Table1.objects.create(
                name=data['name'],
                father_name=data['father_name'],
                mother_name=data['mother_name']
            )
            obj = Table2.objects.create(
                student_id=table1.id,
                address=data['address'],
                gender=data['gender'],
                age=data['age'],
                blood_group=data['blood_group']
            )
            return JsonResponse({'id': str(obj.id),"table1":str(table1.id)}, status=201)
        except:
            return JsonResponse({'error': 'Something went wrong'}, status=400)

    def put(self, request, id):
        data = json.loads(request.body)
        try:
            obj = Table2.objects.get(id=id)
            obj.student_id = data['student_id'] if 'student_id' in data else None
            obj.address = data['address'] if 'address' in data else None
            obj.gender = data['gender'] if 'gender' in data else None
            obj.age = data['age'] if 'age' in data else None
            obj.blood_group = data['blood_group'] if 'blood_group' in data else None
            obj.save()
            return JsonResponse({'id': str(obj.id)}, status=204)
        except Table2.DoesNotExist:
            return JsonResponse({'error': 'Table2 object does not exist'}, status=400)

    def delete(self, request, id):
        try:
            obj = Table2.objects.get(id=id)
            obj.delete()
            return JsonResponse({}, status=204)
        except Table2.DoesNotExist:
            return JsonResponse({'error': 'Table2 object does not exist'}, status=400)



class ObtainAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Checking whether the user exists
        user = User.objects.filter(username=username).first()

        #if no user create one user
        if not user:
            user = User.objects.create_user(username=username, password=password)

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            return Response({'token': token.key, 'userid': user.id, 'username': user.username})
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
