from django.shortcuts import get_object_or_404 
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from account.models import User

from django.views.decorators.csrf import csrf_exempt
from utils.decorators import jwt_required


"""上传图片"""
@csrf_exempt
def upload_images(request):
    return JsonResponse({'hello':'hello'})