import { request } from "../utils/request"

export function getNotesByColumn(id){
  const query = `columnid=${id}`;
   const url = `/note/column/${id}/?${query}`;
  return request({
    url:url,
    method:'get'
  })
}