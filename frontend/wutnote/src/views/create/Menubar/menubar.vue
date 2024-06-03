<script setup>
    import { ref, reactive } from 'vue'
    import { defineProps } from 'vue'

    const props = defineProps({
        editor: {
            type: Object,
            required: true
        }
    });
    
    const items = reactive([
    {
        icon:'icon-chexiao',
        title:'撤销',
        action: function(){
            console.log(props)
            props.editor.chain().focus().undo().run()
        }
    },{
        icon:'icon-fanchexiao',
        title:'取消撤销',
        action: function(){
            console.log(props)
            props.editor.chain().focus().redo().run()
        },
        isActive: () => props.editor.isActive('strike')
    },{
        icon:'icon-fuwenbenbianjiqi_shanchuxian',
        title:'删除线',
        action: function(){
            console.log(props)
            props.editor.chain().focus().toggleStrike().run()
        },
        isActive: () => props.editor.isActive('strike')
    },{
        icon:'iconfont icon-fuwenbenbianjiqi_jiacu',
        title:'加粗',
        action: function(){
            console.log("加粗")
            props.editor.chain().focus().toggleBold().run()
        },
        isActive: () => props.editor.isActive('bold')
    },{
        icon:'icon-zitifangda',
        title:'字号+',
        action: function(){
            console.log("字号+")
            // props.editor.chain().focus().extendMarkRange('textStyle', { fontSize: 'increase' }).run();
        },
    },{
        icon:'icon-zitisuoxiao',
        title:'字号-',
        action: function(){
            console.log("字号-")
            props.editor.chain().focus().toggleBold().run()
        },
        isActive: () => props.editor.isActive('bold')
    },{
        icon:'icon-h-1',
        title:'一级标题',
        action: function(){
            console.log("一级标题")
            props.editor.chain().focus().toggleHeading({ level: 1 }).run()
        },
        isActive: () => props.editor.isActive('heading', { level: 1 })
    },{
        icon:'icon-h-2',
        title:'二级标题',
        action: function(){
            console.log("二级标题")
            props.editor.chain().focus().toggleHeading({ level: 2 }).run()
        },
        isActive: () => props.editor.isActive('heading', { level: 2 })
    },{
        icon:'icon-h-3',
        title:'三级标题',
        action: function(){
            console.log("三级标题")
            props.editor.chain().focus().toggleHeading({ level: 3 }).run()
        },
        isActive: () => props.editor.isActive('heading', { level: 3 })
    },{
        icon:'icon-h-4',
        title:'四级标题',
        action: function(){
            console.log("四级标题")
           props.editor.chain().focus().toggleHeading({ level: 4 }).run()
        },
        isActive: () => props.editor.isActive('heading', { level: 4 })
     },{
        icon: 'icon-gaoliang',
        title: '高亮',
        action: function(){
            console.log("高亮")
             props.editor.chain().focus().toggleHighlight().run()
        },
        isActive: () => props.editor.isActive('highlight')
      },{
        icon: 'icon-liebiao',
        title: '无序列表',
        action: function(){
            console.log("无序列表")
            props.editor.chain().focus().toggleBulletList().run()
        },
        isActive: () => props.editor.isActive('bulletList')
      },{
        icon: 'icon-youxuliebiao',
        title: '有序列表',
        action: function(){
            console.log("有序列表")
            props.editor.chain().focus().toggleOrderedList().run()
        },
        isActive: () => props.editor.isActive('orderedList')
      },{
        icon: 'icon-quote',
        title: '引用块',
        action: function(){
            console.log("引用块")
            props.editor.chain().focus().toggleBlockquote().run()
        },
        isActive: () => props.editor.isActive('blockquote')
      },{
        icon: 'icon-biaodanzujian-biaoge',
        title: '表格',
        action: function(){
            console.log("表格")
            props.editor.chain().focus()
          .insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run()
        },
        isActive: () => props.editor.isActive('blockquote')
      },
    ])

    // 点击激活样式
    const name = ref('');
    const activeIcon = (nameIcon)=>{
        name.value = nameIcon;
        console.log(name.value);
    }
</script>

<template>
    <div class="bar-container">
        <div class="bar-box">
            <!-- <div :class="['icon-item' ,name==item.icon?'active':'']" -->
            <div :class="['icon-item' ,name==item.icon?'active':'']"
                v-for="item in items" 
                :key="item.icon"
                @click="activeIcon(item.icon),item.action()">
                <i :class="[item.icon,'iconfont']"></i>
                <p>{{item.title}}</p>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.bar-container{
    display: flex;
    justify-content: center;
    background-color: $menubar-bgcolor;
    border-bottom: 1px solid $border-color;
}
.bar-box{
    display: flex;
    .icon-item{
        padding: 5px;
        // border: 1px solid gray;
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #555666;
        cursor: pointer;
        i{
            font-size: 22px;
        }
        p{
            font-size: 12px; 
        }
    }
    // .active{
    //     background-color: $active-color;
    // }
}
</style>