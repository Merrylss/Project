from django.shortcuts import render
# django内置的装饰器函数，指定访问方式
from django.views.decorators.http import require_GET, require_POST
# django内置的装饰器函数，用户登录后才能访问
from django.contrib.auth.decorators import login_required
# Create your views here.

import goods


# 只允许GET访问
@require_GET
# 只允许登陆后访问
# @login_required
def index(request):
    """
    首页
    :param request:
    :return:
    """
    # if request.session['user']:
    # 查询所有商品类型，一级类型
    goodstype_101_list = goods.models.GoodsType.objects.filter(parent__isnull=True)

    # 查询所有的[5种]商品类型：在首页中指定的数据
    # 男子
    goods_type_1 = goods.models.GoodsType.objects.get(pk=101)
    goods_type_1_list = goods.models.GoodsType.objects.filter(parent=goods_type_1)
    # print(goods_type_1_list)
    goods_list_1 = goods.models.Goods.objects.filter(goodstype__in=goods_type_1_list)[:4]
    # print(goods_list_1)
    # 女子
    goods_type_2 = goods.models.GoodsType.objects.get(pk=102)
    goods_type_2_list = goods.models.GoodsType.objects.filter(parent=goods_type_2)
    # print(goods_type_1_list)
    goods_list_2 = goods.models.Goods.objects.filter(goodstype__in=goods_type_2_list)
    # print(goods_list_2)
    # 童装
    goods_type_3 = goods.models.GoodsType.objects.get(pk=103)
    goods_type_3_list = goods.models.GoodsType.objects.filter(parent=goods_type_3)
    # print(goods_type_1_list)
    goods_list_3 = goods.models.Goods.objects.filter(goodstype__in=goods_type_3_list)
    # print(goods_list_3)
    # 运动
    goods_type_4 = goods.models.GoodsType.objects.get(pk=104)
    goods_type_4_list = goods.models.GoodsType.objects.filter(parent=goods_type_4)
    # print(goods_type_1_list)
    goods_list_4 = goods.models.Goods.objects.filter(goodstype__in=goods_type_4_list)
    # print(goods_list_4)
    # 品牌
    goods_type_5 = goods.models.GoodsType.objects.get(pk=105)
    goods_type_5_list = goods.models.GoodsType.objects.filter(parent=goods_type_5)
    # print(goods_type_1_list)
    goods_list_5 = goods.models.Goods.objects.filter(goodstype__in=goods_type_5_list)
    # print(goods_list_5)
    return render(request, 'common/index.html', {'goodstype_101_list': goodstype_101_list,\
                                                 'goods_list_1': goods_list_1, \
                                                 'goods_list_2': goods_list_2,\
                                                 'goods_list_3': goods_list_3, \
                                                 'goods_list_4': goods_list_4, \
                                                 'goods_list_5': goods_list_5})
