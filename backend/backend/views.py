from django.shortcuts import get_object_or_404 
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from utils.decorators import jwt_required
from django.views.decorators.csrf import csrf_exempt
from account.models import User

# 腾讯云cos
from qcloud_cos import CosConfig, CosS3Client
from backend import settings
import uuid

from rest_framework.parsers import JSONParser
from note.models import Note, Tag
from note.serializers import NoteSerializer, TagSerializer

"""上传图片到腾讯云"""
@csrf_exempt
@jwt_required
def upload_images(request):
    if request.method == 'POST':
        file = request.FILES['img']
        file_name = file.name
        # 生成唯一的文件名
        unique_file_name = f"{uuid.uuid4().hex}_{file_name}"

        config = CosConfig(Region=settings.TENCENT_CLOUD_REGION, SecretId=settings.TENCENT_CLOUD_SECRET_ID, SecretKey=settings.TENCENT_CLOUD_SECRET_KEY)
        client = CosS3Client(config)

        response = client.put_object(Bucket=settings.TENCENT_CLOUD_BUCKET, Body=file, Key=unique_file_name)
        response_url = f'https://{settings.TENCENT_CLOUD_BUCKET}.cos.{settings.TENCENT_CLOUD_REGION}.myqcloud.com/{unique_file_name}'

        # TODO:后期对上传图片操作进行数据库记录

        return JsonResponse({'status': 'success', 'url': response_url})
    else:
        return JsonResponse({'status': 'failed', 'message': 'Invalid request method'})
    

"""新建笔记"""
@csrf_exempt
@jwt_required
def edit(request):
    user = User.objects.get(id = request.user_id)

    data = JSONParser().parse(request)
    
    # 创建或获取标签
    tags = []
    for tag_data in data.get('tags', []):
        tag_id = tag_data.get('tagid')
        tag, created = Tag.objects.get_or_create(id=tag_id)
        tags.append(tag)
    
    # 创建笔记实例
    note = Note(
        title=data.get('title'),
        abstract=data.get('abstract'),
        content=data.get('content'),
        user=user  
    )
    note.save()
    
    # 关联笔记和标签
    note.tags.set(tags)
    
    # 返回响应
    serializer = NoteSerializer(note)
    return JsonResponse(serializer.data, status=201)