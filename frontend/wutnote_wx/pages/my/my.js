// pages/my/my.js
import { userLogin } from '../../apis/login'
import { getNotesListById, getColumnsListById, getCollectsListById, getConcernsListById } from '../../apis/my'
Page({                                  

  /**
   * 页面的初始数据
   */
  data: {
    userInfo:{
      username:"登录/注册",
      recordCount:0,
      starCount:0,
      avator:"../../images/tabicons/my.png"
    },
    navActive:1,
    noteActive:1,
    noteHeight:0,
    flag:false,
    myNotesList:[],
    columnList:[],
    collectList:[],
    concernList:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    const user = wx.getStorageSync('user')
    this.setData({
      userInfo:{
        username:user.nickname,
        // avator:user.avator
      }
    })
    this.getNotesById();
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
    const res = await getNotesListById();
    this.setData({
      myNotesList:res.data.records
    })
    // console.log(res);
  },

  // 获取登录用户的专栏
  async getColumnsById(){
    const res = await getColumnsListById();
    this.setData({
      columnList:res.data.records
    })
    // console.log(res);
  },

  // 获取登录用户的收藏
  async getCollectsById(){
    const res = await getCollectsListById();
    this.setData({
      collectList:res.data.records
    })
    // console.log(res);
  },

  // 获取登录用户的关注列表
  async getConcernsById(){
    const res = await getConcernsListById();
    this.setData({
      concernList:res.data.records
    })
  },
  
  // 我的三个模块的选择跳转
  navSelect:function(event){
    const index = event.currentTarget.dataset.active;
    if(index == 2){
      this.getCollectsById();
    }else if(index == 3){
      this.getConcernsById();
    }
    this.setData({
      navActive:index
    })
  },

  // 我的文章板块的笔记和专栏跳转
  noteActiveSelect:function(event){
    const index = event.currentTarget.dataset.active;
    if(index == 1){
      this.getNotesById();
    }else if(index == 2){
      this.getColumnsById();
    }
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
      query.select('.my-container').boundingClientRect(rect=>{
        const height = screenHeight-rect.height;
        console.log(height);
        this.setData({
          noteHeight:height-30
        })
        }).exec();
      }, 500);  
  },

  // 关注的跳转
  navToUserDetail:function(event){
    const item = event.currentTarget.dataset.item;
    item.url = "../../subpkg/user_detail/user_detail?user_id="+item.user_id+"&nickName="+item.nickname+"&avatar="+item.avator;
    // console.log("item:"+JSON.stringify(item));
    // console.log("url:"+item.url);
    wx.navigateTo({
      url: item.url,
    })
  }
})