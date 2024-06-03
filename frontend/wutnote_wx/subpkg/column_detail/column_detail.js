// subpkg/column_detail/column_detail.js
import { getNotesByColumn } from '../../apis/column'
Page({

  /**
   * 页面的初始数据
   */
  data: {
    column_id:0,
    column_img:'',
    column_name:'',
    column_info:'',
    notesList:[],
    noteHeight:0
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.setData({
      column_id:options.column_id
    })
    this.getNotesList();
  },

  onReady(options){
    this.getScrollHeight();
  },

  // 根据专栏id查询专栏信息
  async getNotesList(){
    const res = await getNotesByColumn(this.data.column_id);
    this.setData({
      column_name:res.data.title,
      column_info:res.data.abstract,
      column_img:res.data.pic,
      notesList:res.data.records
    })
  },

  // 设置滚动区域的高度
  getScrollHeight:function(){
    const screenInfo = wx.getSystemInfoSync();
    const screenHeight = screenInfo.windowHeight;
    setTimeout(() => {
      const query = wx.createSelectorQuery();
      query.select('.top-container').boundingClientRect(rect=>{
        const height = screenHeight-rect.height;
        console.log(height);
        this.setData({
          noteHeight:height-30
        })
        }).exec();
      }, 500);  
  }
})