Component({
  properties:{
    items:{
      type:Array,
      value:[],
      observer:'onItemsChange'
    }
  },
  data:{
  },
  methods:{
    navToColumn:function(event){
      const item = event.currentTarget.dataset.item;
      item.url = "../../subpkg/column_detail/column_detail?column_id="+item.column_id;
      // console.log("column_url:"+JSON.stringify(item));
      wx.navigateTo({
        url: item.url,
      })
    }
  }
})