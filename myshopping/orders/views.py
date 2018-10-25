from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

import shopcart, users

from . import models


def order_confirm(request):
    """
    订单确认
    :param request:
    :return:
    """
    # 获取数据
    buy_goods_id_list = request.POST.getlist('buy_goods_id')
    print(buy_goods_id_list)
    shop_cart_list = shopcart.models.ShopCart.objects.filter(pk__in=buy_goods_id_list)
    print(shop_cart_list)
    if len(shop_cart_list) > 0:
        return render(request, 'orders/order_confirm.html', {'shop_cart_list': shop_cart_list})
    else:
        return redirect(reverse('shopcart:shop_cart_info'))



def order_pay(request):
    """
    订单支付
    :param request:
    :return:
    """
    pass


def order_done(request):
    """
    生成订单
    :param request:
    :return:
    """
    # 获取购买的商品
    shop_cart_list = request.POST.getlist('sc')

    # 获取购买者地址
    addr_id = request.POST['addr_id']
    address = users.models.Address.objects.get(pk=addr_id)
    addr = address.consignee + ";" + address.phone + ";" + address.nation + ";" + address.province\
        + ";" + address.country + ";" + address.street + ";" + address.intro + ";"
    total = 0
    # 生成订单
    myorder = models.MyOrder(user=request.user, address=addr, total=total)
    myorder.save()
    # 创建订单项对象
    for sc_id in shop_cart_list:
        # 查询购物对象
        _shopcart = shopcart.models.ShopCart.objects.get(pk=sc_id)
        # 创建订单对像
        order_item = models.MyOrderItem(goods_img=_shopcart.goods.goodsimages_set.first().path, \
                                        goods_name=_shopcart.goods.name,\
                                        goods_price=_shopcart.goods.price,\
                                        goods_count=_shopcart.count,\
                                        goods_subtotal=_shopcart.total,\
                                        myorder=myorder)

        order_item.save()
        # 计算总计金额
        total += _shopcart.total
    # 更新总计金额
    myorder.total = total
    myorder.save()

    # 提交保存订单，跳转订单详情页面
    return redirect(reverse("orders:order_info", kwargs={'order_id': myorder.id}))


def order_list(request):
    """
    查看订单列表
    :param request:
    :return:
    """
    pass


def order_info(request, order_id):
    """
    查看订单信息
    :param request:
    :return:
    """
    _order = models.MyOrder.objects.get(pk=order_id)
    return render(request, "orders/order_info.html", {"order": _order})



