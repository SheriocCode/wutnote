from django.db import models
from django.utils import timezone  
from account.models import User

# Create your models here.
"""标签表"""
class Tag(models.Model):  
    id = models.BigAutoField(primary_key=True)  # 自增的BigIntegerField主键  
    tagname = models.CharField(max_length=10, unique=True)  # 标签名称，不超过10个字符，唯一  
  
    def __str__(self):  
        return self.tagname  


"""专栏表"""
class NotebookColumn(models.Model):  
    title = models.CharField(max_length=100)  
    description = models.TextField(blank=True)  
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='columns')  
    created_at = models.DateTimeField(auto_now_add=True)  
  
    def __str__(self):  
        return self.title
    
"""笔记表"""
class Note(models.Model):  
    id = models.BigAutoField(primary_key=True)  # 自增的BigIntegerField主键  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')  # 用户（作者）id，逻辑外键  
    title = models.CharField(max_length=20)  # 标题  
    abstract = models.CharField(max_length=20)  # 笔记摘要  
    content = models.TextField()  # 笔记内容（使用TextField来存储大量文本）  
    # content_path = models.CharField(max_length=255, blank=True, null=True)  # 如果需要云路径，可以添加这个字段  
    browse_num = models.BigIntegerField(default=0)  # 浏览数  
    favor_num = models.BigIntegerField(default=0)  # 点赞数  
    collect_num = models.BigIntegerField(default=0)  # 收藏数  
    visibility = models.IntegerField(choices=((1, '公开'), (0, '私有')), default=1)  # 可见权限，1公开 0私有  
    create_time = models.DateTimeField(default=timezone.now)  # 发表时间  
    update_time = models.DateTimeField(auto_now=True)  # 修改时间  

    # 笔记标签功能：笔记和标签多对多
    tags = models.ManyToManyField(Tag, related_name='notes',null=True, blank=True)  # 与Tag模型建立多对多关系
    # 专栏功能：一个用户有多个专栏，一个专栏有多个笔记。而每个笔记只对应一个专栏
    column = models.ForeignKey(NotebookColumn, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)  
  
    def __str__(self):  
        return self.title

"""用户收藏笔记表"""
class UserFavoriteNote(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')  
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='favorited_by')  
  
    class Meta:  
        unique_together = ('user', 'note')  # 确保用户不能重复收藏同一个笔记  
  
    def __str__(self):  
        return f"Favorite by {self.user.username} of note {self.note.id}"
    
