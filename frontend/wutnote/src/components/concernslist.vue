<script setup>
    import { ref } from 'vue'

    
    // const props = defineProps({
    //     concernslist:Object
    // })

    const concernslist = ref([{
        "user_id": 2,
        "avator": null,
        "nickname": "xiaowang",
        "signature": "小王同学真的很爱学习"
      },
      {
        "user_id": 3,
        "avator": null,
        "nickname": "lisi",
        "signature": "李四同学正在修炼中..."
      }])

    //   用户的关注和取消关注
    const cancelConcern = () =>{
        
    }
</script> 

<template>
    <div class="concerns-container">
        <div class="concern-box" v-for="concern in concernslist" :key="concern.user_id">
            <div class="top-info">
                <div class="left-item">
                    <!-- <img :src="concern.avator" alt=""> -->
                    <img src="@/assets/avator1.png" alt="">
                    <div class="name">{{concern.nickname}}</div>
                </div>
                <div class="right-item">
                    <button class="concerned" @click="cancelConcern">已关注</button>
                </div>
            </div>
            <div class="sign">{{concern.signature}}</div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.concerns-container{
    // background-color: pink;
    .concern-box{
        width: 500px;
        padding: 10px 20px;
        margin-bottom: 20px;
        border-bottom: 1px solid $border-color;
        .top-info{
            display: flex;
            justify-content: space-between;
            align-items: center;
            .left-item{
                display: flex;
                align-items: center;
                img{
                    width: 50px;
                    margin-right: 10px;
                    border-radius: 50%;
                }
                .name{
                    color: $text-color;
                }
            }
            .concerned{
               border: 1px solid $border-color; 
               background-color: $theme-color;
               color: $text-color;
            }
        }
        .sign{
            padding: 10px;
            font-size: 14px;
            color: $text-color;
        }
    }
}
</style>
