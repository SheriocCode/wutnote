<script setup>
    import { ref, reactive } from 'vue'
    import { defineProps } from 'vue'

    const props = defineProps({
        editor: {
            type: Object,
            required: true
        }
    });
    
    // 基础样式设置
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
        icon: 'icon-code',
        title: '代码块',
        action: function(){
            props.editor.chain().focus().toggleCodeBlock().run()
        },
        isActive: () => props.editor.isActive('blockquote')
      },{
        icon: 'icon-quote',
        title: '引用块',
        action: function(){
            console.log("引用块")
            props.editor.chain().focus().toggleBlockquote().run()
        },
        isActive: () => props.editor.isActive('blockquote')
      }
    ])

    // 图片上传样式
    const imgItem = reactive({
        icon:'icon-charutupian',
        title:'图片',
        action: function(){
            
        }
    })

    // 表格样式设置
    const tableItems = reactive({
        icon:'icon-biaodanzujian-biaoge',
        title:'表格',
        items:[
            {
                title:'新增表格',
                action: function(){
                    props.editor.chain().focus().insertTable({ rows: 2, cols: 3 }).run();
                }
            },{
                title:'删除表格',
                action: function(){
                    props.editor.chain().focus().deleteTable().run()
                }
            },{
                title:'上面添加一行',
                action: function(){
                    props.editor.chain().focus().addRowBefore().run()
                }
            },{
                title:'下面添加一行',
                action: function(){
                    props.editor.chain().focus().addRowAfter().run()
                }
            },{
                title:'左边添加一列',
                action: function(){
                    props.editor.chain().focus().addColumnBefore().run()
                }
            },{
                title:'右边添加一列',
                action: function(){
                    props.editor.chain().focus().addColumnAfter().run()
                }
            },{
                title:'删除行',
                action: function(){
                    props.editor.chain().focus().deleteRow().run()
                }
            },{
                title:'删除列',
                action: function(){
                    props.editor.chain().focus().deleteColumn().run()
                }
            }
        ]
    })

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
            <div class="icon-item">
                <i :class="[imgItem.icon,'iconfont']"></i>
                <p style="margin-top:2px;">{{imgItem.title}}</p>
            </div>
            <el-dropdown trigger="click">
                <div class="icon-item">
                    <i :class="[tableItems.icon,'iconfont']"
                        style="margin-bottom:5px;"></i>
                    <p >{{tableItems.title}}</p>
                </div>
                <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item 
                        v-for="item in tableItems.items" 
                        :key="item.title"
                        @click="item.action">
                        {{item.title}}
                    </el-dropdown-item>
                </el-dropdown-menu>
                </template>
            </el-dropdown>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.bar-container{
    margin-top: 10px;
    display: flex;
    justify-content: center;
    background-color: $theme-color;
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
        color: $theme-text;
        cursor: pointer;
        i{
            font-size: 20px;
        }
        p{
            font-size: 12px; 
        }
    }
}
</style>