
# wutnote
### 项目概览
一款多平台同步的笔记共享软件，基于**Vue3PC端**+**微信小程序端**+基于**Django后端**管理😍😍

> @[Sherioc](https://github.com/SheriocCode) (゜ω゜)┏=👉：系统架构、页面原型设计、Django后端  
> @[Aminlex](https://github.com/Aminlex)（很棒的前端er）（づ￣3￣）づ╭❤️～：Vue前端、微信小程序端

PC端
![image](https://github.com/user-attachments/assets/a897cb87-a6a9-4ff9-852c-06ea4c08a792)
![image](https://github.com/user-attachments/assets/e2b98fd0-93f4-4187-b49a-8e691bb78932)
![image](https://github.com/user-attachments/assets/ae0d4e5e-17fe-47de-bb8e-fbc10112f64c)
![image](https://github.com/user-attachments/assets/0ca48ff9-f6d2-4a34-9f1a-f1fb6da201ff)

管理端
![image](https://github.com/user-attachments/assets/159ec8a2-add8-4399-b798-3cfece2ff3e6)
![image](https://github.com/user-attachments/assets/898df273-c28b-4a2e-b4d5-e2181f7b6963)

### 页面原型（figma）
![image](https://github.com/user-attachments/assets/c165d7ae-b566-4ef3-a4dd-36145e25be76)

### ER模型
![](https://github.com/user-attachments/assets/d1a1d3a7-fef0-46b2-a348-621561beb067)

### 数据库
![image](https://github.com/user-attachments/assets/58149d68-3ddf-4f0c-9c28-3266dbb4005b)

### 接口文档
![image](https://github.com/user-attachments/assets/e763c20d-6501-4a8b-a80a-a112020bfd1d)



### 后端配置

#### 虚拟环境配置

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

#### .env

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
