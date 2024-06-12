<script setup>
    import { useRoute} from 'vue-router'
    import { useUserStore } from '@/stores/user'
    import { onMounted, ref } from 'vue'
    import { getNoteDetail } from '@/apis/note'

    const route = useRoute()
    const id = route.params.id;

    const title = ref('')
    const author = ref('')
    const htmlContent = ref()
    onMounted(async ()=>{
        const res = await getNoteDetail(id);
        title.value = res.data.title;
        author.value = res.data.author;
        htmlContent.value = res.data.content;
    })

</script>

<template>
    <el-container class="main-container">
        <h2>{{title}}</h2>
        <div>{{author}}</div>
        <el-main class="note-box">
            <div class="note-detail" v-html="htmlContent"></div>
        </el-main>
    </el-container>
</template>

<style lang="scss" scoped>
.main-container{
    // background-color: pink;
    display: flex;
    justify-content: center;
}
.note-box{
    display: flex;
    justify-content: center;
}
.note-detail{
    width: 800px;
    // background-color: yellow;
}
</style>
