## 后端配置

### 虚拟环境配置

在wutnote目录下

```python
# 创建虚拟环境
python -m venv venv

# 切换目录
cd venv/Scripts
# 激活虚拟环境
activate

# 查看pip包
pip list
# 安装项目所需包
pip install Django
pip install djangorestframework-simplejwt
pip install pymysql
pip install python-dotenv # 腾讯云
```

### 数据库配置

```python
> 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wutnote',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'yourpwd',
        'PORT': '3306'
    }
}
```

环境变量

```python
> .env环境变量
# @ 腾讯云cos
TENCENT_CLOUD_REGION=your_region
TENCENT_CLOUD_SECRET_ID=your_secret_id
TENCENT_CLOUD_SECRET_KEY=your_secret_key
TENCENT_CLOUD_BUCKET=your_bucket_name 

# @ 密钥配置
SECRET_KEY = 'django-insecure-yoursecretkey'
```

