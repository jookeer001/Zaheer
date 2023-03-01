from django.http import JsonResponse
from .models import Student

def get_students(request):
    students = Student.objects.all()
    data = {"students": list(students.values())}
    return JsonResponse(data)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data["name"], 
            surname=data["surname"], 
            year_of_study=data["year_of_study"]
        )
        return JsonResponse({"student": model_to_dict(student)}, status=201)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Student
  
def get_student(request, id):
      try:
          student = Student.objects.get(id=id)
          data = {"student": model_to_dict(student)}
          return JsonResponse(data)
      except ObjectDoesNotExist:
          return JsonResponse({"error": "Student not found."}, status=404)
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json
  
@csrf_exempt
def update_student(request, id):
      try:
          student = Student.objects.get(id=id)
          if request.method == "PUT":
              data = json.loads(request.body)
              student.name = data.get("name", student.name)
              student.surname = data.get("surname", student.surname)
              student.year_of_study = data.get("year_of_study", student.year_of_study)
              student.save()
              return JsonResponse({"student": model_to_dict(student)})
          else:
              return JsonResponse({"error": "Invalid request method."}, status=400)
      except ObjectDoesNotExist:
          return JsonResponse({"error": "Student not found."}, status=404)

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json
  
@csrf_exempt
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
        if request.method == "PUT":
            data = json.loads(request.body)
            student.name = data.get("name", student.name)
            student.surname = data.get("surname", student.surname)
            student.year_of_study = data.get("year_of_study", student.year_of_study)
            student.save()
            return JsonResponse({"student": model_to_dict(student)})
        else:
            return JsonResponse({"error": "Invalid request method."}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Student not found."}, status=404)

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import Student

@csrf_exempt
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        if request.method == "DELETE":
            student.delete()
            return JsonResponse({"message": "Student deleted successfully."})
        else:
            return JsonResponse({"error": "Invalid request method."}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Student not found."}, status=404)        
        