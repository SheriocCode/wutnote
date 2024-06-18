<script setup>
    import noteslistVue from "@/components/noteslist.vue"
    import { Search } from '@element-plus/icons-vue'
    import { ref } from 'vue'

    const keyword = ref('')
    const tagslist = ref(["高等数学","大学物理","课程介绍","期末复习","考研","留学","计算机专业课","保研"])
    const tagSelect = ref()
</script>

<template>
    <el-container class="main-container">
        <div class="main-box">
            <div class="search-box">
                <input type="text" placeholder="请输入搜索内容">
                <el-icon><Search /></el-icon>
            </div>
            <div class="content-box">
                <div class="left-box">
                    <p>热门分类</p>
                    <el-checkbox-group v-model="tagSelect">
                        <el-checkbox v-for="tag in tagslist" :key="tag" 
                                    :label="tag" :value="tag" />
                    </el-checkbox-group>
                </div>
                <div class="right-box">
                    <p>笔记精选</p>
                    <noteslistVue />
                </div>
            </div>
        </div>
    </el-container>
</template>

<style lang="scss" scoped>
.main-container{
    display: flex;
    justify-content: center;
    background-color: $theme-color;
}
.main-box{
    // background-color: pink;
    width: 1000px;
    display: flex;
    flex-direction: column;
}
.search-box{
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
    margin: 20px 0;
    border-radius: 10px; 
    background-color: $low-theme-color;
    input{
        width: 100%;
        height: 15px;
        font-size: 16px;
        border: none;
        outline: none;
        background-color: $low-theme-color;
    }
    input:focus{
        color:$theme-text;
    }
    .el-icon{
        color: $theme-text;
        font-size: 20px;
    }
}
.content-box{
    display: flex;
    .left-box{
        width: 200px;
        height: 600px;
        padding: 0 10px;
        color: $theme-text;
        border-radius: 10px;
        // background-color: pink;
        background-color: #141414;
        p{
            padding: 20px 0;
            font-size: 20px;
            font-weight: bold;
            border-bottom: 2px solid $border-color;
            margin-right: 20px;
        }
        .el-checkbox-group{
            padding: 20px 5px;
            display: flex;
            flex-direction: column;
            .el-checkbox{
                background-color: $theme-color;
                color: $theme-text;
            } 
        }
    }
    .right-box{
        color: $theme-text;
        padding: 0 15px;
        color: $theme-text;
        border-radius: 10px;
        background-color: #141414;
        margin-left: 30px;
        p{
            padding: 20px 0;
            font-size: 20px;
            font-weight: bold;
            border-bottom: 2px solid $border-color;
        }
    }
}
</style>
<style lang="scss">
.el-checkbox .el-checkbox__inner {
    background-color: $theme-color;
    border-color: $border-color; 
}
.el-checkbox .el-checkbox__label{
    margin-left: 18px;
}
</style>