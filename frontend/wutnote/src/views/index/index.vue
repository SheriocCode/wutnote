<script setup>
    import noteslistVue from "@/components/noteslist.vue";
</script>

<template>
    <el-container class="main-container">
        <el-main class="main-box">
            <noteslistVue />
        </el-main>
    </el-container>
</template>

<style lang="scss" scoped>
.main-container{
    display: flex;
}
.main-box{
    // background-color: pink;
    display: flex;
    justify-content: center;
}
</style>