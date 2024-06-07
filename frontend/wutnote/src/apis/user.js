import httpInstance from "@/utils/utils"

// 登录
export function login(form){
    return httpInstance.post('/account/login/',{
  
            username:form.name,
            password:form.pass
     
    },{
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    }).then(res =>{
        console.log('Logining successfully');
        return res.data;
    })
}