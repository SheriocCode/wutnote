// pages/login/login.js
import { userLogin, userInfo } from '../../apis/login'
Page({

  /**
   * 页面的初始数据
   */
  data: {
    username:'',
    passsword:''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },
  
  nameInput:function(e){
    this.setData({
      username: e.detail.value 
    });
  },
  passInput:function(e){
    this.setData({
      password: e.detail.value 
    });
  },
  // submitLogin:function(e){
  //   this.login(e.detail.value); 
  //   console.log( e.detail.value);
  // },
  async submitLogin(e){
    const res = await userLogin(e.detail.value);
    wx.setStorageSync('token', res.token)
    const token = wx.getStorageInfoSync('token');
    // console.log("res"+JSON.stringify(res));
    if(token){
      const res = await userInfo(token);
      // console.log(res.data);
      wx.setStorageSync('user', res.data)
      wx.switchTab({
        url: '../index/index',
      })
    }
  }
})