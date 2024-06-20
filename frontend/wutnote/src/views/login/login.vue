<script setup>
    import { ref, reactive } from 'vue'
    import { ElMessage } from 'element-plus'
    import { useRouter } from 'vue-router'
    import { login,getMyInfo } from '@/apis/user'
    import { useUserStore } from '@/stores/user'

    const router = useRouter()  

    const form = reactive({})

    const rules = {
        "name":[
            { required: true, message: '用户名不能为空' }
        ],
        "pass":[
            { required: true, message: '密码不能为空' }
        ]
    }

    // 全局数据存储
    const user = useUserStore();

    // 登录表单校验
    const loginForm = ref(null)
    const resCheck = ()=>{
        loginForm.value.validate(async (valid) => {
        if (valid) {
            const res = await login(form);
            loginForm.value.resetFields();
            user.token = res.token;
            const info = await getMyInfo(user.token);
            user.myinfo = info.data;
            ElMessage({ type: 'success', message: "登录成功" })
            router.push("/home").catch(err=>console.error(err));
            // }
        } else {
            return false;
        }
      });
    }
</script>

<template>
    <div class="bg-box">
        <div class="login-box">
            <h2>登录</h2>
            <div class="method">
                <div class="method-right">
                    <el-form :model="form" ref="loginForm">
                        <el-form-item prop="name" :rules="rules.name">
                            <el-input v-model="form.name" placeholder="用户名"/>
                        </el-form-item>
                        <el-form-item prop="pass" :rules="rules.pass">
                            <el-input v-model="form.pass" placeholder="密码" type="password"/>
                        </el-form-item>
                    </el-form>
                    <el-button type="success" @click="resCheck">登录</el-button>
                </div>
            </div>
        </div>
    </div> 
</template>

<style lang="scss" scoped>
.bg-box{
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    background-color: $theme-color; 
}
.login-box{
    background-color: $low-theme-color; 
    border: 1px solid $border-color; 
    text-align: center; 
    display: inline-block;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    h2{
        color: #fff;
    }
}

.method{
    display: flex;
    margin: auto 50px;
    /* justify-content: space-between; */
}
.method-right{
    display: flex;
    flex-direction: column;
    margin: 20px 0;
    .el-input, .el-button{
        width: 300px;
        height: 40px;
        margin: 10px 0;
    }
    .el-button{
        background-color: $theme-active;
        color: #000;
        font-size: 16px;
    }
}

</style>>

