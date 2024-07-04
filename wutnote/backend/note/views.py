from django.shortcuts import get_object_or_404 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Note, Tag
from utils.decorators import jwt_required

# Create your views here.
"""所有笔记列表"""
def notelist(request):  
    if request.method == 'GET':  
        notes = Note.objects.all().order_by('-id')
        # 初始化响应数据  
        response_data = {  
            'code': 200,  
            'msg': '请求成功',  
            'data': {  
                'total': notes.count(),  
                'records': [],
            }  
        } 
        # 遍历笔记并获取相关标签  
        for note in notes:  
            note_data = {  
                'note_id': note.id,  
                'title': note.title,  
                'abstract': note.abstract,  
                'borwse_num': note.browse_num,  
                'collect_num': note.collect_num,  
                'like_num': note.favor_num,  
                'tags': []  
            }       
            # 获取笔记的标签信息  
            note_tags = note.tags.all()  
            for tag in note_tags:  
                tag_data = {  
                    'tag_id': tag.id,  
                    'tagname': tag.tagname  
                }  
                note_data['tags'].append(tag_data)          
            # 将笔记数据添加到响应数据中  
            response_data['data']['records'].append(note_data)  
            
        # 返回JSON响应  
        return JsonResponse(response_data) 
    return JsonResponse({'error': 'Invalid request'}, status=400)


"""根据id查询笔记详情"""
def note_detail(request, id):  
    note_id = id
    try:  
        # 获取指定的笔记  
        note = get_object_or_404(Note, id=note_id)  
          
        # 获取笔记的作者昵称  
        author = note.user.nickname 
          
        # 准备返回的数据  
        response_data = {  
            'code': 200,  # 你可以根据需要更改这个值  
            'msg': "success request",  # 同样，你可以根据需要更改这个值  
            'data': {  
                'title': note.title,  
                'author': author,  
                'create_time': note.create_time.strftime('%Y-%m-%d %H:%M:%S'),  
                'content': note.content,  
                'tags': [  
                    {'tag_id': tag.id, 'tagname': tag.tagname} for tag in note.tags.all()  
                ],  
                'browse_num': str(note.browse_num),  
                'like_num': str(note.favor_num),  # 注意这里我假设字段名是favor_num而不是like_num  
                'collect_num': str(note.collect_num),  
            }  
        }  
          
        # 返回JSON响应  
        return JsonResponse(response_data)  
    except Note.DoesNotExist:  
        # 如果笔记不存在，返回一个错误响应  
        return JsonResponse({'error': 'Note does not exist'}, status=404)