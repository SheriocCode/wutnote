from django.urls import path
from .views import notelist, note_detail
urlpatterns = [
   path('notelist/', notelist), # 所有笔记列表
   path('<int:id>/', note_detail) # 根据id查询笔记详情
]