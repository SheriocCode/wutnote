// index.js
import { getNotesList } from "../../apis/index"
Page({
  data:{
    queryObj:{
      serach_word:'',
      page:1,
      pageSize:5,
      tag:''
    },
    scrollLeft:0,
    notesList:[],
    total:0,
    tags:[{
          "tag_id": 1,
          "tagname": "数学"
      },
      {
          "tag_id": 2,
          "tagname": "物理"
      },
      {
          "tag_id": 3,
          "tagname": "化工"
      },
      {
          "tag_id": 4,
          "tagname": "材料"
      },
      {
          "tag_id": 5,
          "tagname": "马克思"
      },
      {
          "tag_id": 6,
          "tagname": "自动化"
      },
      {
          "tag_id": 7,
          "tagname": "计算机"
      },
      {
          "tag_id": 8,
          "tagname": "国际教育"
      },
      {
          "tag_id": 9,
          "tagname": "外国语"
      },
      {
          "tag_id": 10,
          "tagname": "基础大类"
      }
    ]
  },

  onLoad(){
    this.getNotes();
    // this.setData({
    //   syWidth: wx.getSystemInfoSync().windowWidth
    // })
  },

  // 导航跳转
  navToSearch:function(){
    wx.navigateTo({
      url: '../../subpkg/search/search',
    })
  },

  // 笔记分页查询
  async getNotes(){
    const res = await getNotesList();
    // console.log(this.data.queryObj);
    // console.log(res.data);
    this.setData({
      notesList:res.data.records,
      total:res.data.total
    })
  }
})
