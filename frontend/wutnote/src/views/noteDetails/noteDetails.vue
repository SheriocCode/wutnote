<script setup>
    import { useRoute} from 'vue-router'
    import { useUserStore } from '@/stores/user'
    import { onMounted, ref } from 'vue'

    const route = useRoute()
    const id = route.params.id;

    const htmlTest = useUserStore()
    const htmlContent = ref(htmlTest.htmlContent)
    onMounted(()=>{
        console.log("hhhhhhhhhhh");
    })

</script>

<template>
    <div class="main-box">
        <div class="note-box">
            <div class="note-detail" v-html="htmlContent"></div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.main-box{
    display: flex;
    justify-content: center;
}
.note-box{
    width: 50%;
    height: 100%;
    background-color: pink;
}
</style>
