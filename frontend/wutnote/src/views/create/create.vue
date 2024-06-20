<script setup>
    import { ref, onMounted, reactive } from 'vue'
    import { useUserStore } from '@/stores/user'
    import { handelImageFile,addNote } from '@/apis/create'
    import { ElMessage } from 'element-plus'
    import { Back } from '@element-plus/icons-vue'

    import MenuBar from "@/views/create/Menubar/menubar.vue"
    import { useEditor, EditorContent } from "@tiptap/vue-3"
    import StarterKit from "@tiptap/starter-kit"
    import Placeholder from "@tiptap/extension-placeholder"
    import Document from "@tiptap/extension-document"
    import Highlight from '@tiptap/extension-highlight'
    import Image from '@tiptap/extension-image'
    import HeadingExtension from '@tiptap/extension-heading'

    // import CodeBlock from '@tiptap/extension-code-block'
    // import CodeBlockLowlight from '@tiptap/extension-code-block-lowlight'
    // import lowlight from 'lowlight'
    // import javascript from 'lowlight/lib/languages/javascript'

    import Table from '@tiptap/extension-table'
    import TableRow from '@tiptap/extension-table-row'
    import TableCell from '@tiptap/extension-table-cell'
    import TableHeader from '@tiptap/extension-table-header'

    const CustomTableCell = TableCell.extend({
    addAttributes() {
        return {
        // 展开现有属性,?.是可选链操作符,可以自行百度(懂的大佬当我没说)
        ...this.parent?.(),

        // 添加新的属性
        backgroundColor: {
            default: null,
            parseHTML: (element) => element.getAttribute('data-background-color'),
            renderHTML: (attributes) => ({
            'data-background-color': attributes.backgroundColor,
            style: `background-color: ${attributes.backgroundColor}`
            })
        }
        }
    }
    })
    // lowlight.registerLanguage('javascript', javascript)

// const CodeBlockExtension = CodeBlock.extend({
//   addOptions() {
//     return {
//       highlight: highlight,
//     };
//   },
// });
    const editor = useEditor({
        content: `<h1>Heading 1</h1><p>Some content here...</p><h2>Heading 2</h2><p>Some more content here...</p>`,
        extensions:[
            Document,
            StarterKit,
            Image,
            // CodeBlock,
            // CodeBlockLowlight.configure({
            //     lowlight,
            // }),
            Highlight.configure({multicolor:true}),
            HeadingExtension.configure({levels:[1,2,3]}),
            Table.configure({
                resizable:true
            }),
            TableRow,
            TableCell,
            TableHeader,
            CustomTableCell,
            Placeholder.configure({
                placeholder:"开始你的笔记创作之旅"
            })
        ]
    }) 

    // 粘贴复制图片
    const handelPaste = async (event) =>{
        // 获取粘贴的数据
        const pasteData = event.clipboardData || window.clipboardData;
        const items = pasteData.items;
        if (items && items.length > 0) {
            for (let item of items) {
                if (item.type.match('image')) {
                    console.log("粘贴事件触发");
                    // 处理图片
                    const file = item.getAsFile();
                    const res = await handelImageFile(file);
                    editor.chain().focus().setImage({ src: res.data.url }).run()
                }
            }
        }
    }

    // 笔记目录生成
    const tableOfContents = ref([]);
    const generateContents = () => {
 
    };

    // 控制笔记保存信息的提交
    const noteDialogShow = ref(false)
    const noteForm = reactive({
        title:"",
        abstract:"",
        content:"",
        tags:[]
    })
    const tagIput = ref('')
    const inputVisible = ref(false)
    const showInput = () =>{
        inputVisible.value = true
    }
    // 标签添加
    const handleInputConfirm = () =>{
        // console.log("hhhhhhhh"+tagIput.value);
        noteForm.tags.push(tagIput.value)
        tagIput.value = ''
        inputVisible.value = false
    }
    // 标签删除
    const handleClose = (tag) =>{
        const index = noteForm.tags.indexOf(tag)
        noteForm.tags.splice(index,1)
    }


    // 提交表单
    const noteFormRef = ref(null)
    const noteFormCheck = ()=>{
        resForm.value.validate(async (valid) => {
        if (valid) {  
            // 获取编辑器里面的内容
            noteForm.content = editor.value.getHTML();       
            await addNote(noteForm);                                        
            noteFormRef.value.resetFields();
        }
      });
    }
    // 取消提交
    // const handelCancel = () =>{
    //     noteForm.tags = '';
    //     noteDialogShow.value = false;
    // }
</script>

<template>
    <div class="create-container">
        <MenuBar :editor="editor"/>
        <div class="editor-contanier">
            <el-scrollbar class="editor-box" style="height: 100%;">
                <div class="scroll-content">
                    <!-- <textarea class="title-input" placeholder="请输入标题"></textarea> -->
                    <editor-content id="editor" :editor="editor"  @paste="handelPaste" style="color:#DCDCDC;"/>
                </div>
            </el-scrollbar> 
        </div>
        <div class="save-container">
            <div class="save-box">
                <div class="top-box">
                    <p>笔记设置</p>
                    <el-button @click="noteFormCheck">保存笔记</el-button>
                    
                </div>
                <div class="bottom-box">
                    <div class="note-container">
                        <el-form v-model="noteForm" ref="noteFormRef" class="note-box" >
                            <el-form-item prop="title" label="标题：">
                                <input v-model="noteForm.title" style="width: 240px"/>
                            </el-form-item>
                            <el-form-item prop="tags" label="标签：">
                            <div class="addtags-box">
                                <input
                                    v-if="inputVisible"
                                    v-model="tagIput"
                                    @keyup.enter="handleInputConfirm"/>
                                <el-button v-else class="button-new-tag" @click="showInput">
                                + 添加标签
                                </el-button>
                                <div class="tags-box">
                                    <el-tag
                                        v-model="noteForm.tags"
                                        v-for="tag in noteForm.tags"
                                        :key="tag"
                                        closable
                                        @close="handleClose(tag)">
                                        {{ tag }}
                                    </el-tag>
                                </div>
                            </div>
                            </el-form-item>
                            <el-form-item prop="abstact" label="摘要：">
                                <textarea v-model="noteForm.abstact"
                                        placeholder="请输入对笔记内容的概述" 
                                        cols="10"/>
                            </el-form-item>
                        </el-form>
                    </div>
                </div>
            </div> 
        </div>
    </div> 

    <!-- 笔记保存表单 -->
    <!-- <el-dialog 
        v-model="noteDialogShow" 
        title="笔记保存" 
        width="400" align-center>
        
        <div class="button-box">
            <el-button @click="handelCancel">取消</el-button>
            <el-button type="primary" @click="noteFormCheck">保存</el-button>
        </div>
    </el-dialog>  -->
</template>

<style lang="scss" scoped>
.create-container{
    background-color: $theme-color;
    display: flex;
    flex-direction: column;
}

.editor-contanier{
    height: 500px;
    display: flex;
    justify-content: center;
    padding: 30px;
}
.editor-box{                                  
    width: 800px;
    padding: 20px 50px;
    background-color: $low-theme-color;
    border-radius: 15px;
    .scroll-content {
        width: 100%;
        overflow-x: hidden;
    }
}


.save-container{
    display: flex;
    justify-content: center;
    margin: 20px 0;
    .save-box{
        width: 850px;
        // padding: 15px;
        background-color: $theme-color;
        border: 2px solid $border-color;
        // background-color: pink;
        color: $theme-text;
        .top-box{
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid $border-color;
            p{
                font-size: 16px;
            }
        }
    }
}
.el-button{
    background-color: $theme-active;
    color: $theme-color;
    border: none;
}
.bottom-box{
    padding: 0 50px;
    .addtags-box{
        .el-tag{
            background-color: $low-theme-color;
            color: $theme-text;
            border: none;
        }
    }
}
.note-container{
    display: flex;
    input{
        height: 28px;
        border-radius: 5px;
    }
}
.note-box{
    .el-form-item{
        margin: 15px 0;
    }
    .addtags-box{
        display: flex;
        flex-direction: column;
        .tags-box{
            margin-top: 10px;
        }
    }
    textarea{
        resize: none;
        width: 500px;
        height: 250px;
        outline: none;
        background-color: #282828;
        border: none;
        color:#DCDCDC;
        font-size: 16px;
        padding: 10px;
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
    border-left: 4px solid $theme-active;
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
/* 设置表格宽高 */
.ProseMirror table {
  width: 60%; /* 表格宽度 */
  border-collapse: collapse; /* 边框合并 */
}

.ProseMirror table td,
.ProseMirror table th {
  border: 1px solid #ddd; /* 单元格边框 */
  padding: 2px; /* 单元格内边距 */
  p{
    margin:0;
  }
}

/* 设置表头颜色 */
.ProseMirror table th {
  background-color: #f0f0f0; /* 表头背景颜色 */
}

.el-form-item__label {
  color: $theme-text;
}
blockquote{
  border-left: 3px solid $theme-color; /* 引用块左边的线 */
  color: $text-color; /* 文字颜色 */
  background-color: $theme-color; /* 背景色 */
}

</style>
