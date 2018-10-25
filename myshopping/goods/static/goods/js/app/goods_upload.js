$(function(){
    //一级类型下拉列表改变，触发事件
   $('#type1').change(function(){
       //清空二级类型列表的子元素
      $('#type2').empty();
       //发送ajax请求
       $.ajax({
           url:'/goods/goodstype/',
           type:'GET',
           data:{
               'type_id': $('#type1').val()
           },
           success:function (response) {
               // console.log(response);
               //将服务器返回的json字符串转换为json对象
               json_obj = JSON.parse(response);
               console.log(json_obj);
               //循环获取数据
               for (i in json_obj){
                   console.log(json_obj[i].fields.name, json_obj[i].pk);
                   // 添加到网页中
                   var $option = $('<option>');
                   $option.attr('value', json_obj[i].pk);
                   $option.text(json_obj[i].fields.name);
                   $("#type2").append($option)
               }
           },
           error:function(){
               console.log('请求失败！')
           }

       })
   });
});