<script setup>
    import { ref,onMounted } from 'vue'
    import { useUserStore } from '@/stores/user'
    import noteslistVue from "@/components/noteslist.vue"
    import columnslistVue from "@/components/columnslist.vue"
    import { getMyNotes, getMyColumns, getMyConcerns, getMyFavors} from '@/apis/user'

    // 全局数据存储
    const user = useUserStore();

    // const userInfo = ref({
    //     nickname: "zhangjie",
    //     avator:null,
    //     signature: "这个人很懒，什么都没有留下......"
    // })
    const userInfo = ref({})

    const mynotes = ref({})
    const mycolumns = ref({})
    const myconcerns = ref({})
     const myfavors = ref({})
    onMounted(async ()=>{
        userInfo.value = user.myinfo;
        mynotes.value = (await getMyNotes(user.token)).data.records;
        mycolumns.value = (await getMyColumns(user.token)).data.records;
        myconcerns.value = (await getMyConcerns(user.token)).data.records;
        myfavors.value = (await getMyFavors(user.token)).data.records;
    })
</script>

<template>
    <el-container class="main-container">
        <div class="main-box">
            <div class="my-box">
                <div class="info-box">
                    <img :src="userInfo.avator" alt="">
                    <!-- <img src="@/assets/image.png" alt=""> -->
                    <div>
                        <div class="author">{{userInfo.nickname}}</div>
                        <div class="sign">{{userInfo.signature}}</div>
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