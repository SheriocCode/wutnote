<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    // import { defineProps} from 'vue'

    // const props = defineProps({
    //     noteslist:Object
    // })

    const notesList = ref([{
        note_id: 2,
        title: "第二篇文章标题",
        abstract: "这篇文章是关于现代科技对生活的影响，探讨了科技进步如何改变我们的工作、学习和交流方式。",
        borwse_num: 10,
        collect_num: 120,
        like_num: 85,
        tags: [
          {
            tag_id: 20,
            tagname: "科技与生活"
          },
          {
            tag_id: 21,
            tagname: "现代科技"
          }
        ]
      },
      {
        note_id: 3,
        title: "第三篇文章标题",
        abstract: "本文讨论了环境保护的重要性，分析了当前面临的环境问题，并提出了一些可行的解决方案。",
        borwse_num: 15,
        collect_num: 95,
        like_num: 67,
        tags: [
          {
            tag_id: 30,
            tagname: "环境保护"
          },
          {
            tag_id: 31,
            tagname: "可持续发展"
          }
        ]
      }])

    const router = useRouter()
    const navToNoteDetail = (id) =>{
      // console.log("id:"+id);
      router.push(`/note/${id}`)
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
    width: 500px;
    border-bottom: 1px solid $border-color;
    margin-bottom: 20px;
    cursor: pointer;
    .title{
        padding: 10px 0;
        font-weight: bold;
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
    }
}
</style>