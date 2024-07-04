from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User
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
        'code': 200,  # 你可以根据需要更改这个值  
        'msg': "success request",  # 同样，你可以根据需要更改这个值  
        'data': {  
            'nickname': user.nickname,
            'avator': user.avatar,
            'signature': user.signature,
        }  
    } 
    return JsonResponse(response_data)