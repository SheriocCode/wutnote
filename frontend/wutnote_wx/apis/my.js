import { request } from "../utils/request"

//查询个人笔记
export function getNotesListById(){
  return request({
    url:'/account/notes/',
    method:'get'
  })
}

//查询个人专栏
export function getColumnsListById(token){
  return request({
    url:'/account/columns/',
    method:'get'
  })
}

//查询个人收藏
export function getCollectsListById(token){
  return request({
    url:'/account/favors/',
    method:'get'
  })
}

//查询个人关注
export function getConcernsListById(token){
  return request({
    url:'/account/follows/',
    method:'get'
  })
}

// 根据Id查询笔记
export function getUserNotesList(id){
   const query = `userid=${id}`;
   const url = `/note/${id}/notes/?${query}`;
  return request({
    url:url,
    method:'get'
  })
}


// 根据Id查询专栏
export function getUserColumnsList(id){
  const query = `userid=${id}`;
   const url = `/note/${id}/columns/?${query}`;
  return request({
    url:url,
    method:'get',
    params:{
      'userid':id
    }
  })
}