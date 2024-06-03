// subpkg/note_detail/note_detail.js
import { getNoteDetail } from "../../apis/index"

Page({

  /**
   * 页面的初始数据
   */
  data: {
    note_id:0,
    noteInfo:{},
    noteContent:{}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.setData({
      note_id:options.note_id
    })
    this.getNoteContent()
  },

  async getNoteContent(){
    const app = getApp();
    // const res = await getNoteDetail(this.data.note_id);
    // let noteData = app.towxml.toJson(res.data.content, 'html');
    let noteData = app.towxml.toJson('<h1>5555</h1><p>1111</p><p>的<strong>点点滴滴</strong></p><p>2222<s>22222222222222</s></p><ul><li><p>222222222</p></li></ul><blockquote><p><s>11</s>66666</p></blockquote>', 'html');
    console.log(noteData);
    this.setData({
      // noteInfo:res.data,
      noteContent:noteData
    })
  }
})