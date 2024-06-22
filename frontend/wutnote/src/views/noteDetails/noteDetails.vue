<script setup>
    import { useRoute} from 'vue-router'
    import { useUserStore } from '@/stores/user'
    import { onMounted, ref } from 'vue'
    import { getNoteDetail } from '@/apis/note'

    const route = useRoute()
    const id = route.params.id;

    const noteInfo = ref({})
    onMounted(async ()=>{
        noteInfo.value  = await getNoteDetail(id);  
    })

</script>

<template>
    <el-container class="main-container">
        <!-- <h2>{{title}}</h2> -->
        <el-main class="note-box">
            <div class="note-detail">
                <p class="title">{{noteInfo.title}}</p>
                <div class="author-info">
                    <div class="top-info">
                        <img src="@/assets/image.png" alt="">
                        <p>{{noteInfo.author}}</p>
                        <div class="tags">
                            <div class="tag-item" v-for="tag in noteInfo.tags" :key="tag.tag_id">{{tag.tagname}}</div>
                        </div>
                    </div>
                    <div class="bottom-info">
                        <div class="left-item">创建于 {{noteInfo.create_time}}</div>
                        <div class="right-item">
                            <div class="item">
                                <i class="iconfont icon-liulan4"></i>
                                {{noteInfo.browse_num}}
                            </div>
                            <div class="item">
                                <i class="iconfont icon-shoucang"></i>
                                {{noteInfo.collect_num}}
                            </div>
                            <div class="item">
                                <i class="iconfont icon-xihuan"></i>
                                {{noteInfo.like_num}}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="content" v-html="noteInfo.content">

                </div>
            </div>
        </el-main>
    </el-container>
</template>

<style lang="scss" scoped>
.main-container{
    background-color: $theme-color;
    display: flex;
    justify-content: center;
}
.note-box{
    display: flex;
    justify-content: center;
    
}
.note-detail{
    margin-top: 20px;
    padding: 20px;
    border-radius: 10px;
    width: 800px;
    // background-color: pink;
    color: #fff;
    border: 2px solid $border-color;
    .title{
        font-size: 18px;
        font-weight: bold;
    }
}

.author-info{
    margin: 20px 0;
    .top-info{
        display: flex;
        align-items: center;
        img{
            margin-right: 10px;
            width: 40px;
            border-radius: 50%;
        }
        p{
            font-size: 14px;
        }
        .tags{
            display: flex;
            border-left: 1px solid #fff;
            margin-left: 10px;
            .tag-item{
                border: 1px solid $theme-active;
                color: $theme-active;
                border-radius: 12px;
                font-size: 10px;
                padding: 5px;
                margin-left: 10px;
            }
        }
    }  
    .bottom-info{
        display: flex;
        justify-content: space-between;
        color: #8C8C8C;
        font-size: 14px;
        margin-top: 10px;
        .right-item{
            display: flex;
        }
        .item{
            margin-left: 10px;
        }
    }
}

.content{
    background-color: $low-theme-color;
    padding: 20px;
    img{
        display: block;
        width: 30%;
    }
}
</style>
<style lang="scss">
    .content p{
        margin: 5px;
    }
</style>
