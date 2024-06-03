import httpInstance from "@/utils/utils"

// 获取首页笔记
export function getNotesList(){
    return httpInstance({
        method: 'get',
        url: '/note/list',
        params:{
            serach_word:'',
            page:1,
            pageSize:5,
            tag:''
        }
    })
}

// 根据笔记id获取笔记详情
