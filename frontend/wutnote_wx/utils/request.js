// const baseurl = "https://mock.apifox.com/m1/4248529-3889906-default";
const baseurl = "http://127.0.0.1:8000";

export const request = (params) => {
  return new Promise(function(resolve,reject){
    const headers = { ...params.header };
    const token = wx.getStorageSync('token');
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    wx.request({
      ...params,
      url: baseurl + params.url,
      method: params.method,
      data: params.data || {},
      header:headers,
      timeout:5000,
      success: (res)=> {
        if (res.statusCode === 200) {
          resolve(res.data);
        } else {
          // 如果状态码不是200，使用reject拒绝Promise
          reject(new Error('Server responded with status code ' + res.statusCode));
        }
      },
      fail: (err) => {
          reject(err)
      }
    })
  })
}

