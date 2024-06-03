from django.urls import path
from .views import login_view, protected_view, my_view, follow_view, notes, columns, favors
urlpatterns = [
   path('login/', login_view),
   path('protected_view/',protected_view),

   path('my/', my_view), # 个人页
   path('notes/', notes), # 查询我的文章列表
   path('columns/', columns), # 查询我的专栏列表
   path('favors/', favors), # 查询我的收藏列表
   path('follows/', follow_view), # 查询我的关注列表
]