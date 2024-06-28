<script setup>
    import { ref,onMounted,computed } from 'vue'
    import { useUserStore } from '@/stores/user'
    import noteslistVue from "@/components/noteslist.vue"
    import columnslistVue from "@/components/columnslist.vue"
    import { getMyNotes, getMyColumns, getMyConcerns, getMyFavors} from '@/apis/user'

    // 全局数据存储
    const token = ref(localStorage.getItem('token'))

   
    const nickname = ref(localStorage.getItem('nickname'));
    const avator = ref(localStorage.getItem('avator'));
    const signature = ref(localStorage.getItem('signature'));
  
    // const userInfo = ref({})

    const mynotes = ref({})
    const mycolumns = ref({})
    const myconcerns = ref({})
    const myfavors = ref({})
    onMounted(async ()=>{
        // userInfo.value = JSON.parse(myinfo);
        console.log("userinfo:"+signature.value);
        mynotes.value = (await getMyNotes(token.value)).data.records;
        mycolumns.value = (await getMyColumns(token.value)).data.records;
        myconcerns.value = (await getMyConcerns(token.value)).data.records;
        myfavors.value = (await getMyFavors(token.value)).data.records;
    })
</script>

<template>
    <el-container class="main-container">
        <div class="main-box">
            <div class="my-box">
                <div class="info-box">
                    <img v-if="avator" src="@/assets/avator.png" alt="">
                    <img v-else :src="avator" alt="">
                    <!-- <img src="@/assets/image.png" alt=""> -->
                    <div>
                        <div class="author">{{nickname}}</div>
                        <div class="sign">{{signature}}</div>
                        <!-- <div v-else class="sign">这是一个非常神秘的人...</div>  -->
                    </div>
                </div>
                <div class="menu-box">
                    <el-tabs tab-position="left"  class="tabs-box">
                        <el-tab-pane label="笔记">
                            <noteslistVue :notesList="mynotes"/>
                        </el-tab-pane>
                        <el-tab-pane label="专栏">
                            <columnslistVue :columnslist="mycolumns"/>
                        </el-tab-pane>
                        <el-tab-pane label="关注"></el-tab-pane>
                        <el-tab-pane label="收藏">
                            <noteslistVue :notesList="myfavors"/>
                        </el-tab-pane>
                    </el-tabs>
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
    display: flex;
    justify-content: center;
}
.my-box{
    margin-top: 20px;
    width: 800px;
    display: flex;
    flex-direction: column;
    padding: 30px;
    border-radius: 8px;
    background-color: #141414;
    border: 2px solid $border-color;
    .info-box{
        display: flex;
        align-items: center;
        img{
            width: 100px;
            border-radius: 50%;
            margin-right: 20px;
        }
        .author{
            font-weight: bold;
            color: $text-color;
        }
        .sign{
            margin-top: 10px;
            font-size: 12px;
            color: $text-color;
        }
    }
    .menu-box{
        margin-top: 30px;
        .el-tab-pane{
           margin-left: 50px;
        }
    }
}
</style>
<style lang="scss">
.el-tabs__item.is-active {
    color: $theme-active;
}
.el-tabs__item{
    color: $text-color;
}
.el-tabs__item:hover{
    color: $theme-active;
}
.el-tabs__active-bar{
    background-color: $theme-active;
}
</style>