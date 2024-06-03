from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Follow
from note.models import Note, NotebookColumn, UserFavoriteNote
from utils.jwt import generate_jwt_token  # 生成jwt
from utils.decorators import jwt_required

# Create your views here.

"""登录"""
@csrf_exempt  # 不使用CSRF保护
def login_view(request):  
    if request.method == 'POST':  
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        try:  
            user = User.objects.get(username=username)  
            # # TODO:优化密码验证的逻辑（比如使用哈希和比对）  
            # if user.check_password(password):  # 后期自定义check_password方法  
            if password == user.pwd: 
                token = generate_jwt_token(user)  
                return JsonResponse({'token': token})  
            else:  
                return JsonResponse({'error': 'Invalid credentials'}, status=400)  
        except User.DoesNotExist:  
            return JsonResponse({'error': 'User not found'}, status=400)  
    return JsonResponse({'error': 'Invalid request'}, status=400)


"""测试Authorization token"""
@jwt_required
def protected_view(request):
    userid = request.user_id
    return JsonResponse({'message': 'Protected resource','userid':userid})

"""个人页"""
@jwt_required
def my_view(request):
    user = User.objects.get(id = request.user_id)
    response_data = {  
        'code': 200,  
        'msg': "success request",  
        'data': {  
            'nickname': user.nickname,
            'avator': user.avatar,
            'signature': user.signature,
        }  
    } 
    return JsonResponse(response_data)

"""查询我的文章列表"""
@jwt_required
def notes(request):
    user = User.objects.get(id = request.user_id)
    notes =  Note.objects.filter(user = user)
    response_data = {  
        'code': 200,  
        'msg': '请求成功',  
        'data': {  
            'records': [],
        }  
    } 
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
    return JsonResponse(response_data) 

"""查询我的专栏列表"""
@jwt_required
def columns(request):
    user = User.objects.get(id = request.user_id)
    columns =  NotebookColumn.objects.filter(owner = user)
    response_data = {  
        'code': 200,  
        'msg': '请求成功',  
        'data': {  
            'records': [],
        }  
    } 
    for column in columns:
        column_data = {
            'column_id' : column.id,
            'name' :column.title,
            'note_num' :0
        }       
        # TODO:查询该column下的笔记数量
         
        response_data['data']['records'].append(column_data)  
    return JsonResponse(response_data)

"""查询我的收藏列表"""
@jwt_required
def favors(request):
    user = User.objects.get(id=request.user_id)
    favors = UserFavoriteNote.objects.filter(user = user)
    response_data = {  
        'code': 200,  
        'msg': '请求成功',  
        'data': {  
            'records': [],
        }  
    } 
    for favor in favors:
        favor_data = {
            'note_id': favor.note.id,
            'title': favor.note.title,
            'abstract': favor.note.abstract,
            'borwse_num': favor.note.browse_num,  
            'collect_num': favor.note.collect_num,  
            'like_num': favor.note.favor_num,  
            'tags': []  
        }
        # 获取笔记的标签信息  
        note_tags = favor.note.tags.all()  
        for tag in note_tags:  
            tag_data = {  
                'tag_id': tag.id,  
                'tagname': tag.tagname  
            }  
            favor_data['tags'].append(tag_data)          
        # 将笔记数据添加到响应数据中  
        response_data['data']['records'].append(favor_data)  
    return JsonResponse(response_data) 

"""查询我的关注列表"""
@jwt_required
def follow_view(request):
    user = User.objects.get(id = request.user_id)
    follows = Follow.objects.filter(follower = user)
    response_data = {  
        'code': 200,  
        'msg': "success request",  
        'data': {  
            'records': [],
        }  
    } 
    for follow in follows:
        follo_data = {
            'user_id': follow.following.id,
            'avator': follow.following.avatar,
            'nickname': follow.following.nickname,
            'signature': follow.following.signature,
        }
        response_data['data']['records'].append(follo_data)  

    return JsonResponse(response_data)