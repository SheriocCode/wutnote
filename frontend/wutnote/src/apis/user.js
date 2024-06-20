import httpInstance from "@/utils/utils"
import { ElMessage } from 'element-plus'

// 登录
export function login(form){
    return httpInstance.post('/account/login/',{
            username:form.name,
            password:form.pass
     
    },{
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    }).then(res=>{
        // return res.data
    }).catch(err=>{
        ElMessage.error('获取出错！')
    })
}

// 获取个人信息
export function getMyInfo(token){
    return httpInstance.get('/account/my/',{
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }).then(res=>{
        return res.data
    }).catch(err=>{
        ElMessage.error('获取出错！')
    })
}

// 获取我的笔记
export function getMyNotes(token){
    return httpInstance.get('/account/notes/',{
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }).then(res=>{
        return res.data
    }).catch(err=>{
        ElMessage.error('获取出错！')
    })
}

// 获取我的专栏
export function getMyColumns(token){
    return httpInstance.get('/account/columns/',{
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }).then(res=>{
        return res.data
    }).catch(err=>{
        ElMessage.error('获取出错！')
    })
}

// 获取我的关注
export function getMyConcerns(token){
    return httpInstance.get('/account/follows/',{
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }).then(res=>{
        return res.data
    }).catch(err=>{
        ElMessage.error('获取出错！')
    })
}

// 获取我的收藏
export function getMyFavors(token){
    return httpInstance.get('/account/favors//',{
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }).then(res=>{
        return res.data
    }).catch(err=>{
        ElMessage.error('获取出错！')
    })
}