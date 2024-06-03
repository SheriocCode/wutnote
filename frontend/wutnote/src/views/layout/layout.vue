<script setup>
</script>

<template>
    <div class="index-contanier">
        <el-container class="index-box">
            <el-header height="5%">
                <el-dropdown>
                    <div class="avatar">
                        <el-avatar :size="30" :src="circleUrl" />
                    </div>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item>个人资料</el-dropdown-item>
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
    background-color: $border-color;
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
}
.index-box{
    height: 100%;
    padding: 10px;
}
.el-header{
    display: flex;
    justify-content: flex-end;
    .el-dropdown{
        margin-right: 20px;
    }
}
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