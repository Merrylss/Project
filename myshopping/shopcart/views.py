from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Q, F
# django内置的装饰器函数，用户登录后才能访问
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


import goods
from . import models
import shopcart


@login_required
def shop_cart_add(request, goods_id, count):
    """
    添加商品到购物车功能
    :param request:
    :param goods_id: 商品id
    :param count: 商品数量
    :return:
    """
    # 得到用户购买的商品
    _goods = goods.models.Goods.objects.get(pk=goods_id)
    try:
        # 查询当前用户的购物车是否包含该商品
        shop_cart = models.ShopCart.objects.get(Q(users=request.user) & Q(goods=_goods))
        shop_cart.count += int(count)
        shop_cart.total = float(shop_cart.count) * _goods.price
        shop_cart.save()
    except Exception as e:
        # 查询关键购物对象，添加到购物车中
        shop_cart = models.ShopCart(goods=_goods, count=count, users=request.user)
        shop_cart.total = float(count) * _goods.price
        shop_cart.save()
        print("--------------------->", e)

    shop_cart_list = models.ShopCart.objects.filter(users=request.user).order_by('-add_time')
    return render(request, "shopcart/shop_cart_info.html", {'shop_cart_list': shop_cart_list})

    # return HttpResponse('商品添加成功！')


@login_required
def shop_cart_info(request):
    """
    查看购物车
    :param request:
    :return:
    """
    shop_cart_list = models.ShopCart.objects.filter(users=request.user).order_by('-add_time')
    return render(request, "shopcart/shop_cart_info.html", {'shop_cart_list': shop_cart_list})


@login_required
def shop_cart_del(request, goods_id):
    """
    删除购物车商品
    :param request:
    :return:
    """
    _goods = shopcart.models.ShopCart.objects.get(pk=goods_id)
    print(_goods)
    _goods.delete()
    return HttpResponse('成功')


@login_required
def shop_cart_update(requsest, goods_id, i):
    """
    更该购物车商品信息
    :param requsest:
    :param goods_id:
    :return:
    """
    _goods = shopcart.models.ShopCart.objects.get(pk=goods_id)
    # print(_goods)
    _goods.count = i
    things = goods.models.Goods.objects.get(pk=_goods.goods_id)
    _goods.total = float(i) * things.price
    _goods.save()
    return HttpResponse('成功')

