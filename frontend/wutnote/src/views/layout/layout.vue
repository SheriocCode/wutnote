<script setup>
    import { House, Edit, Avatar } from '@element-plus/icons-vue'
    import { ref, onMounted } from 'vue'
    import { useUserStore } from '@/stores/user'

    // 菜单选项激活
    const activeIndex = ref(1)
    const handleSelect = (index)=>{
        activeIndex.value = index;
        // const select = document.getElementsByClassName('el-menu-item')[index];
        // select.style.borderbottom = '1px solid #fff'
    }

    // 全局数据存储
    const user = useUserStore();
    onMounted(()=>{
        const avator = user.myinfo.avator;
    })
    
</script>

<template>
    <div class="index-contanier">
        <el-container class="index-box">
            <el-header height="60px">
                <div class="menu-box">
                    <el-menu class="header-menu" 
                        mode="horizontal"
                        :default-active="activeIndex"
                        @select="handleSelect">
                        <router-link to="/home">
                            <el-menu-item index="1" :class="{ active: activeIndex === index }">
                                <el-icon><House /></el-icon>
                                <template #title><span>首页</span></template>
                            </el-menu-item>
                        </router-link>
                        <router-link to="/create">
                            <el-menu-item index="2">
                                <el-icon><Edit /></el-icon>
                                <template #title>创作中心</template>
                            </el-menu-item>
                        </router-link>
                        <router-link to="/my">
                            <el-menu-item index="3">
                                <el-icon><Avatar /></el-icon>
                                <template #title>个人空间</template>
                            </el-menu-item>
                        </router-link>
                    </el-menu>
                </div>
                <el-dropdown>
                    <div class="avatar">
                        <el-avatar :size="30" :src="avator" />
                    </div>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <router-link to="/my">
                                <el-dropdown-item>个人资料</el-dropdown-item>
                            </router-link>
                            <el-dropdown-item>退出登录</el-dropdown-item>
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
    padding: 10px 0;
    .menu-box{
        width: 420px;
        padding: 0 200px;
    }
    .el-menu{
        border: none;
        background-color: $theme-color;
        .el-menu-item{
            color:$theme-text;
        }
        .router-link-active{
            border-bottom:2px solid $theme-active;
            font-weight: bold;
        }
        
            
    }
}
.el-dropdown{
    cursor: pointer;
}
</style>