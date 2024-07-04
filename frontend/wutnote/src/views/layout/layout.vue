<script setup>
    import { House, Edit, Avatar } from '@element-plus/icons-vue'
    import { ref, onMounted } from 'vue'
    import { useUserStore } from '@/stores/user'
    import { useRouter } from 'vue-router'

    const token = localStorage.getItem('token')
    const avator = ref()
    onMounted(()=>{
        avator.value = localStorage.getItem('avator');
        // window.addEventListener('beforeunload', (event) => {
        //     localStorage.clear(); // 用户关闭网页时清除所有localStorage数据
        // });
    })

    // 退出登录
    const router = useRouter()
    const exit = ()=>{
        localStorage.clear();
        router.push('/login') 
    }
    
</script>

<template>
    <div class="index-contanier">
        <el-container class="index-box">
            <el-header height="60px">
                <div class="menu-box">
                    <div class="header-menu">
                        <router-link to="/home" active-class="active">
                            <div class="menu-item">
                                <el-icon><House /></el-icon>
                                <span>首页</span>
                            </div>
                        </router-link>
                        <router-link to="/create" active-class="active">
                             <div class="menu-item">
                                <el-icon><Edit /></el-icon>
                                <span>创作中心</span>
                            </div>
                        </router-link>
                        <router-link to="/my" active-class="active">
                             <div class="menu-item">
                                <el-icon><Avatar /></el-icon>
                                <span>个人空间</span>
                            </div>
                        </router-link>
                    </div>
                </div>
                <el-dropdown v-if="token">
                    <div class="avatar" >
                        <img :src="avator" alt="">
                    </div>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <router-link to="/my">
                                <el-dropdown-item>个人资料</el-dropdown-item>
                            </router-link>
                            <el-dropdown-item @click="exit()">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
                <div v-else>
                    <button class="login-button" @click="router.push('/login')">登录</button>
                </div>
            </el-header>
            <router-view></router-view>
        </el-container>
    </div>
</template>

<style lang="scss" scoped>
.index-contanier{
    background-color: $theme-color;
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
}
.index-box{
    height: 100%;
}
.el-header{
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: $theme-color;
    .menu-box{
        padding: 0 250px;
    }
    .header-menu{
        border: none;
        display: flex;
        justify-content: space-around;
        .active{
            border-bottom:2px solid $theme-active;
            font-weight: bold;
        }
        .menu-item{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 15px 10px;
            margin: 0 10px;
            color:$theme-text;
        }
       
    }
}

.el-dropdown{
    cursor: pointer;
    .avatar{
        width: 40px;
        height: 40px;
        background-color: pink;
        border-radius: 50%;
        img{
            width: 100%;
        }
    }
}
@media(max-width:900px){
    .index-contanier{
        width: 900px;
    }
}
</style>
