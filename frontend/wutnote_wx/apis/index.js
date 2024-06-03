import { request } from "../utils/request"

// 笔记分页查询
export function getNotesList(){
  return request({
    url:'/note/notelist/',
    method:'get'
  })
}

// 根据笔记id查询笔记详情
export function getNoteDetail(){
  const query = `id=${id}`;
  const url = `/note/${id}/?${query}`;
 return request({
   url:url,
   method:'get'
 })
}