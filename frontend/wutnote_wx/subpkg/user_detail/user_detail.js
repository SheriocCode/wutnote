// subpkg/user_detail/user_detail.js
import { getUserNotesList, getUserColumnsList } from '../../apis/my'
Page({

  /**
   * 页面的初始数据
   */
  data: {
    noteActive:1,
    noteHeight:0,
    flag:false,
    user_id:0,
    user_name:'',
    user_avatar:'',
    myNotesList:[],
    columnList:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    // console.log("item:"+JSON.stringify(options.userInfo));
    this.setData({
      user_id:options.user_id,
      user_name:options.nickName,
      user_avatar:options.avatar
    })
    this.getNotesById();
    this.getColumnsById();
  },
  onReady(options){
    if(!this.data.flag){
      this.getScrollHeight();
      this.setData({
        readyFlag:true
      })
    }
  },
  // 获取登录用户的笔记
  async getNotesById(){
    const res = await getUserNotesList(this.data.user_id);
    this.setData({
      myNotesList:res.data.records
    })
    // console.log(res);
  },

  // 获取登录用户的专栏
  async getColumnsById(){
    const id = this.data.user_id;
    const res = await getUserColumnsList(id);
    this.setData({
      columnList:res.data.records
    })
    // console.log(res);
  },

  noteActiveSelect:function(event){
    const index = event.currentTarget.dataset.active;
    console.log(index);
    this.setData({
      noteActive:index
    })
  },
  // 设置滚动区域的高度
  getScrollHeight:function(){
    const screenInfo = wx.getSystemInfoSync();
    const screenHeight = screenInfo.windowHeight;
    setTimeout(() => {
      const query = wx.createSelectorQuery();
      query.select('.user-info-container').boundingClientRect(rect=>{
        const height = screenHeight-rect.height;
        console.log(height);
        this.setData({
          noteHeight:height-30
        })
        }).exec();
      }, 500);  
  }
})