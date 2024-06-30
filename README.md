## 后端配置

### 虚拟环境配置

```python
> 在 wutnote 项目根目录下
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
pip install django-cors-headers
pip install python-dotenv
pip install cos-python-sdk-v5 # 腾讯云

```

### .env

```python
> 在backend目录下.env文件
# @ 密钥配置
SECRET_KEY = 'django-insecure-yoursecretkey'

# @ MySQL数据库配置
DB_NAME = 'wutnote'
DB_HOST = '127.0.0.1'
DB_USER = 'username'
DB_PASSWORD = 'passowrd'
DB_PORT = '3306'

# @ 腾讯云cos
TENCENT_CLOUD_REGION=your_region
TENCENT_CLOUD_SECRET_ID=your_secret_id
TENCENT_CLOUD_SECRET_KEY=your_secret_key
TENCENT_CLOUD_BUCKET=your_bucket_name

# @ 腾讯元器api
TECENT_YUANQI_URL
TENCENT_YUANQI_TOKEN

# @ 支付宝沙箱配置
ALIPAY_SERVER_URL
ALIPAY_APP_ID
ALIPAY_APP_PRIVATE_KEY
ALIPAY_PUBLIC_KEY
```
