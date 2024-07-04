<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    import { defineProps} from 'vue'

    const props = defineProps({
        notesList:Object
    })

   
    const router = useRouter()
    const navToNoteDetail = (id) =>{
      // console.log("id:"+id);
       window.open(`/note/${id}`, '_blank');
    //   router.push(`/note/${id}`)
    }
</script>

<template>
    <div class="notes-container">
        <div class="note-box" v-for="note in notesList" :key="note.note_id" @click="navToNoteDetail(note.note_id)">
            <div class="title">{{note.title}}</div>
            <div class="abstract">{{note.abstract}}</div>
            <div class="info">
                <div class="left-box">
                    <div class="tags-box" v-for="tags in note.tags" :key="tags.tag_id">
                        <div class="item">{{tags.tagname}}</div>
                    </div>
                </div>
                <div class="right-box">
                    <div class="item">
                        <i class="iconfont icon-liulan4"></i>
                        {{note.borwse_num}}
                    </div>
                    <div class="item">
                        <i class="iconfont icon-shoucang"></i>
                        {{note.collect_num}}
                    </div>
                    <div class="item">
                        <i class="iconfont icon-xihuan"></i>
                        {{note.like_num}}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.note-box{
    // font-family: '微软雅黑';
    background-color: $low-theme-color;
    width: 500px;
    border: 1px solid $border-color;
    margin-top: 20px;
    padding: 10px;
    border-radius: 10px;
    cursor: pointer;
    .title{
        padding: 10px 0;
        // font-weight: bold;
        color: $theme-text;
        font-size: 18px;
    }
    .abstract{
        color: $text-color;
        font-size: 14px;
        line-height: 24px;
    }
    .info{
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: $text-color;
        padding: 10px 0;
        .left-box,.right-box{
            display: flex;
            .item{
                margin-right: 10px;
            }
        }
        .tags-box .item{
            border: 1px solid $theme-active;
            color: $theme-active;
            border-radius: 12px;
            font-size: 10px;
            padding: 5px;
        }
    }
}

</style>
