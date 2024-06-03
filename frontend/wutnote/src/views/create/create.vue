<script setup>
    import { useUserStore } from '@/stores/user'
    import { Back } from '@element-plus/icons-vue'
    import MenuBar from "@/views/create/Menubar/menubar.vue"
    import { ref, onMounted } from 'vue'
    import { useEditor, EditorContent } from "@tiptap/vue-3"
    import StarterKit from "@tiptap/starter-kit"
    import Placeholder from "@tiptap/extension-placeholder"
    import Document from "@tiptap/extension-document"

    const editor = useEditor({
        extensions:[
            Document,
            StarterKit,
            // new FontSize(),
            Placeholder.configure({
                placeholder:"开始你的笔记创作之旅"
            })
        ]
    }) 
    
    const htmlTest = useUserStore()
    const getHtmlContent = () =>{
        if(editor){
            htmlTest.htmlContent = editor.value.getHTML();
            console.log(htmlTest.htmlContent);
        }
    }
</script>

<template>
    <div class="create-container">
        <div class="top-container">
            <router-link to="/home" class="back-box">
                <div class="back">
                    <el-icon><Back /></el-icon>返回
                </div>
            </router-link>
            <el-button @click="getHtmlContent" round>保存笔记</el-button>
        </div>
        <MenuBar :editor="editor"/>
        <div class="editor-contanier">
            <el-scrollbar class="editor-box" style="height: 100%;">
                <div class="scroll-content">
                    <textarea class="title-input" placeholder="请输入标题"></textarea>
                    <editor-content id="editor" :editor="editor"/>
                </div>
            </el-scrollbar> 
        </div>
    </div> 
</template>

<style lang="scss" scoped>
.create-container{
    background-color: $menubar-bgcolor;
    height: 100vh;
}
.top-container{
    background-color: #fff;
    border-bottom: 1px solid $border-color;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    .back-box{
        display: flex;
        justify-content: center;
        .back{
            display: flex;
            align-items: center;
        }
        .el-icon{
            font-size: 22px;
            margin-right: 10px;
        }
    }
}
.editor-contanier{
    height: 75%;
    display: flex;
    justify-content: center;
    padding: 30px;
}
.editor-box{
    width: 800px;
    padding: 20px 50px;
    background-color: #fff;
    border-radius: 15px;
    .scroll-content {
        width: 100%;
        overflow-x: hidden;
    }
    
    .title-input{
        border: none;
        resize: none;
        outline: none;
        width: 100%;
        font-size: 25px;
        border-bottom: 1px solid $border-color;
    }
}

</style>
<style lang="scss">
.tiptap,.ProseMirror-focused {
    outline: none;
}
.tiptap p.is-editor-empty:first-child::before {
  color: #adb5bd;
  content: attr(data-placeholder);
  float: left;
  height: 0;
  pointer-events: none;
}
.tiptap p{
    margin-top: 10px;
    padding-left: 10px;
    // background-color: pink;
}
.tiptap p:hover{
    // margin-top: 10px;
    padding-left: 6px;
    border-left: 4px solid $border-color;
}
blockquote{
    margin: 16px 0;
    padding: 20px 0;
    background-color: $block-color;
    border-left: 4px solid $block-border-color !important;
    p{
        margin: 0 !important;
    }
}
</style>
