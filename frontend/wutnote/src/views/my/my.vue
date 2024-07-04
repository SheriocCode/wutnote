<script setup>
    import { EditPen } from '@element-plus/icons-vue'
    import { computed, ref } from 'vue'

    const nickname = ref(localStorage.getItem("nickname"))
    const signature = ref(localStorage.getItem("signature"))

    // 控制笔记的更改
    const isDisabled = ref(true)
    const inputSytle = computed(()=>{
        return isDisabled.value ? 'disinput' : '';
    }) 

    // 提交个人信息的修改
    const updateMyInfo = () =>{

    }

</script>

<template>
    <el-container class="info-container">
        <div class="info-box">
            <img src="@/assets/avator.png" alt="">
            <div class="edit-info">
                <div class="input-item">
                    <div class="label">昵称</div>
                    <input type="text" 
                        v-model="nickname" 
                        :disabled="isDisabled"
                        :class="inputSytle">
                    <el-icon @click="isDisabled = false"><EditPen /></el-icon>
                </div>
                <div class="input-item">
                    <div class="label">个性签名</div>
                    <input type="text" 
                        v-model="signature" 
                        :disabled="isDisabled"
                        :class="inputSytle">
                    <el-icon @click="isDisabled = false"><EditPen /></el-icon>
                </div>
            </div>
            <div class="button-box">
                <button style="margin-right:50px;">取消</button>
                <button @click="updateMyInfo">修改</button>
            </div>
        </div>
    </el-container>
</template>

<style lang="scss" scoped>
.info-container{
    display: flex;
    justify-content: center;
    padding: 60px 0;
}
.info-box{
    display: inline-block;
    border: 1px solid #fff;
    border-radius: 15px;
    padding: 50px;
    img{
        width: 80px;
        border-radius: 50%;
    }
}
.edit-info{
    .input-item{
        display: flex;
        margin: 20px;
        display: flex;
        align-items: center;
        .label{
            width: 70px;
            text-align: center;
            color: #fff;
            margin-right: 10px;
        }
        /* 可编辑时的样式 */
        input{
            border-bottom: 1px solid #fff;
            background-color: $theme-color;
        }
        /* 不可编辑时的样式 */
        .disinput{
            color:$text-color;
            border-bottom: 1px solid #fff;
            background-color: $theme-color;
        }
        .el-icon{
            margin-left: 10px;
            color: #fff;
        }
    }
    
}
.button-box{
    padding: 50px;
    display: flex;
    justify-content: center;
}
</style>