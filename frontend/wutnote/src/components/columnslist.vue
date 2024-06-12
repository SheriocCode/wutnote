<script setup>
    import { ref } from 'vue'
    // import { defineProps} from 'vue'

    // const props = defineProps({
    //     columnslist:Object
    // })

    const columnslist = ref([{
        "column_id": 1,
        "name": "Java学习专栏",
        "note_num": 0
      },
      {
        "column_id": 2,
        "name": "Python学习专栏",
        "note_num": 0
      }])
</script>

<template>
    <div class="columns-container">
        <div class="column-box" v-for="column in columnslist" :key="column.column_id">
            <div class="name">{{column.name}}</div>
            <div class="note-num">{{column.note_num}} 篇笔记</div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.columns-container{
    // background-color: pink;
    .column-box{
        width: 500px;
        padding: 10px 20px;
        margin-bottom: 20px;
        border-bottom: 1px solid $border-color;
        .note-num{
            margin-top: 10px;
            font-size: 14px;
            color: $text-color;
        }
    }
}
</style>