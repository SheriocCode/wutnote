<script setup>
    import { House, Edit, Avatar } from '@element-plus/icons-vue'
    import noteslistVue from "@/components/noteslist.vue";
</script>

<template>
    <el-container class="main-box" height="95%">
        <el-aside width="200px">
                    <el-menu class="aside-menu">
                        <router-link to="/home">
                            <el-menu-item index="1">
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
                                <template #title>个人信息</template>
                            </el-menu-item>
                        </router-link>
                    </el-menu>
        </el-aside>
        <el-main>
            <noteslistVue />
        </el-main>
    </el-container>
</template>

<style lang="scss" scoped>
.main-box{
    background-color: #fff;
    border-radius: 15px;
    position: relative;
    height: 100%;
    .el-aside{
        border-right:1px solid $border-color;
        .el-menu{
            border: none;
            border-radius: 15px;
        }
    }
    
}
</style>