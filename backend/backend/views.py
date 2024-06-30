from django.shortcuts import get_object_or_404 
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
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

# 腾讯元器ai文本创作
import requests

# 流式返回数据
from django.http import StreamingHttpResponse

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
        
        return JsonResponse({'code': 200, 'msg': 'success upload','data':{'url':response_url}})
    else:
        return JsonResponse({'code': 400, 'msg': 'Invalid request method'})
    

"""新建笔记"""
@csrf_exempt
@jwt_required
def edit(request):
    if request.method == 'POST':
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
        return JsonResponse({'code':200, 'msg':'success upload', 'data':{}})
    else:
        return JsonResponse({'code': 400, 'msg': 'Invalid request method'})

import time
"""流式返回数据"""
def stream_response(request):
    def file_iterator(files, delay=1):
        for file in files:
            yield f'data: {file}\n\n'  # 使用data:前缀发送消息，后面跟着两个换行符\n\n
            time.sleep(delay)

    files = ['file1.txt', 'file2.txt', 'file3.txt']
    iterator = file_iterator(files, delay=1)

    response = StreamingHttpResponse(iterator, content_type='text/event-stream')  # 设置Content-Type为text/event-stream
    return response

"""腾讯元器"""
@csrf_exempt
def get_hunyuan_response(request):
    if request.method == 'POST':
        requset_data = JSONParser().parse(request)
        tool = requset_data.get('tool')
        text = requset_data.get('text')

        prompt = f'请对一下文本进行{tool}操作:{text}'

        data = {
            "assistant_id": "v0mR1uV19Gjw",
            "user_id": "rodneyxiong",
            "stream": False,
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": prompt,
                    }
                ]
                }
            ]
        }

        # 调用腾讯元器
        url = settings.TECENT_YUANQI_URL

        headers = {
            'X-Source': 'openapi',
            'Content-Type': 'application/json',
            'Authorization': settings.TENCENT_YUANQI_TOKEN 
        }

        response = requests.post(url, headers=headers, json=data)
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Invalid request method. Please use POST."})


def follow(request):
    return JsonResponse({"hello":"hello"})

def unfollow(request):
    return JsonResponse({"heloo":"hello"})