import httpInstance from "@/utils/utils"
import { useUserStore } from "@/stores/user"

// 处理上传的图片
export function handelImageFile(file,token){
    const formData = new FormData();
    formData.append('img',file);
    return httpInstance.post('/upload/img/',formData,{
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }).then(res=>{
        return res.data
    }).catch(err=>{
        const user = useUserStore();
        user.isLoading = false;
        ElMessage.error('上传出错！')
    })
}

// 添加笔记
export function addNote(form,token){
    return httpInstance.post('/edit/',{
        title:form.title,
        abstract:form.abstract,
        content:form.content,
        tags:[]
    },{
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }).then(res=>{
        return res;
    }).catch(err=>{
        ElMessage.error('上传失败！')
    })
}