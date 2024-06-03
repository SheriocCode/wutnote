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
    navToNoteDeatil:function(event){
      const item = event.currentTarget.dataset.item;
      item.url = "../../subpkg/note_detail/note_detail?note_id="+item.note_id;
      // console.log("note_url:"+JSON.stringify(item));
      wx.navigateTo({
        url: item.url,
      })
    }
  }
})