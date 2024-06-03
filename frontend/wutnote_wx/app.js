// app.js
// import { Towxml } from "./towxml/main"
const Towxml = require('./towxml/main')
App({
  onLaunch() {
    wx.clearStorageSync();
  },
  towxml:new Towxml()
})
