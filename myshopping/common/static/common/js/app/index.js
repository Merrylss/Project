$(function(){
    $('.type1li').mouseover(function () {
        $(this).children('ul').css('display', 'block')
    });
    $('.type1li').mouseout(function () {
        $(this).children('ul').css('display', 'none')
    });

    // 添加到购物车
    $('.add-cart').click(function () {
        // 获取商品编号
        var $goods_id = $(this).attr('goods_id');
        console.log($goods_id);

        // 发送ajax请求，添加到购物车
        $.ajax({
            url: '/shopcart/'+$goods_id+'/'+1+'/shop_cart_add/',
            type: 'GET',
            success:function (response) {
                console.log(response);
                alert('商品添加成功！')
            },

            error:function () {
                console.log('请求失败')
            }
        })
    })



});