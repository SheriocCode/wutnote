<script setup>
    import { House, Edit, Avatar } from '@element-plus/icons-vue'
    import { ref, onMounted } from 'vue'
    import { useUserStore } from '@/stores/user'
    import { useRouter } from 'vue-router'

    // 菜单选项激活
    const activeIndex = ref(1)
    const handleSelect = (index)=>{
        activeIndex.value = index;
        // const select = document.getElementsByClassName('el-menu-item')[index];
        // select.style.borderbottom = '1px solid #fff'
    }

    const token = localStorage.getItem('token')
    onMounted(()=>{
        const avator = localStorage.getItem('avator');
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
                        <router-link to="/home">
                            <div :class="['menu-item',{ active: activeIndex === 1 }]"
                                @click="handleSelect(1)">
                                <el-icon><House /></el-icon>
                                <span>首页</span>
                            </div>
                        </router-link>
                        <router-link to="/create">
                             <div :class="['menu-item',{ active: activeIndex === 2 }]"
                                @click="handleSelect(2)">
                                <el-icon><Edit /></el-icon>
                                <span>创作中心</span>
                            </div>
                        </router-link>
                        <router-link to="/my">
                             <div :class="['menu-item',{ active: activeIndex === 3 }]"
                                @click="handleSelect(3)">
                                <el-icon><Avatar /></el-icon>
                                <span>个人空间</span>
                            </div>
                        </router-link>
                    </div>
                </div>
                <el-dropdown>
                    <div class="avatar" v-if="token">
                        <el-avatar :size="30" :src="avator" />
                    </div>
                    <div v-else>
                        <button class="login-button" @click="router.push('/login')">登录</button>
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
            </el-header>
            <router-view></router-view>
        </el-container>
    </div>
</template>

<style lang="scss" scoped>
.index-contanier{
    // background-color: $border-color;
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
        .menu-item{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 15px 10px;
            margin: 0 10px;
            color:$theme-text;
        }
        .active{
            border-bottom:2px solid $theme-active;
            font-weight: bold;
        }
       
    }
}
.login-button{
    border: none;
    background-color: $theme-active;
    padding: 5px 20px;
    border-radius: 10px;
}
.el-dropdown{
    cursor: pointer;
}
@media(max-width:900px){
    .index-contanier{
        width: 900px;
    }
}
</style>
