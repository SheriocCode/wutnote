from django.urls import path
from .views import notelist, note_detail, note_column
from .views import user_notes, user_columns
urlpatterns = [
   # 公共视图
   path('notelist/', notelist), # 所有笔记列表
   path('<int:id>/', note_detail), # 根据id查询笔记详情
   path('column/<int:columnid>/', note_column), # 根据专栏id查询专栏内容

   # 他人视图
   path('<int:userid>/notes/', user_notes), # 根据用户id查询文章列表
   path('<int:userid>/columns/', user_columns) # 根据用户id查询专栏列表
]