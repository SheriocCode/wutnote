import { request } from "../utils/request"

// 登录
export function userLogin(form){
  return request({
    url:'/account/login/',
    method:'post',
    data: form,
    header:{
      'content-type':'application/x-www-form-urlencoded'
    }
  })
}

// 登录后获取个人信息
export function userInfo(token){
  return request({
    url:'/account/my/',
    method:'get'
  })
}