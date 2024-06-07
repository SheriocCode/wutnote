import httpInstance from "@/utils/utils"

// 处理上传的图片
export function handelImageFile(file){
    const formData = new FormData();
    formData.append('img',file);
    return httpInstance.post('/upload/img',file,{
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    }).then(res => {
        console.log("Upload img successfullly:",res);
    }).catch(error => {
        console.error('Error uploading image:', error);
    });
}

// 添加笔记
export function addNote(form){
    return httpInstance.post('/edit',form,{
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    }).then(res => {
        console.log("Add note successfullly:",res);
    }).catch(error => {
        console.error('Error adding note:', error);
    });
}