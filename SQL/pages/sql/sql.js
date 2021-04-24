// pages/sql/sql.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  ////////////////////////////////////
  onLoad: function() {
    var that = this;
    //读取数据库
    wx.request({
      url: 'http://127.0.0.1:8080/getstu',
      method: 'GET',
      data: {
        something: '1'
      },
      header: {
        'content-Type': 'application/json'
      },
      success(res) {
        console.log(res),
          that.setData({
            postList: res,
          });
      }
    });
    //写入数据库
    wx.request({
      url: 'http://127.0.0.1:8080/getstu',
      method: 'GET',
      data: {
        something1: '小王',
        something2: '16',
        something3: '0'
      },
      header: {
        'content-Type': 'application/x-www-form-urlencoded'
      },
      success(res) {
        console.log(res.data);
        if (res.data.status == 0) {
          wx.showToast({
            title: '提交失败！！！',
            icon: 'loading',
            duration: 1500
          })
        } else {
          wx.showToast({
            title: '提交成功！！！', //这里打印出登录成功
            icon: 'success',
            duration: 1000
          })
        }
      }
    });
  },
  ////////////////////////////////////////////////
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})