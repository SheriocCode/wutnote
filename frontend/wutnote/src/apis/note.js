import httpInstance from "@/utils/utils"
import { ElMessage } from 'element-plus'

// 获取首页笔记
export function getNotesList(){
    return httpInstance({
        method: 'get',
        url: '/note/notelist/'
    }).then(res=>{
        return res.data
    }).catch(err=>{
        ElMessage.error('获取出错！')
    })
}

// 根据笔记id获取笔记详情
export function getNoteDetail(id){
    return httpInstance.get(`/note/${id}/`)
        .then(res=>{
            return res.data;
        }).catch(err=>{
            ElMessage.error('获取出错！')
        })
}