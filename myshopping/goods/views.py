from django.shortcuts import render, redirect
# 要求登陆访问
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_GET, require_POST
from django.core.serializers import serialize
from django.http import HttpResponse


from . import models
import stores
import goods


@login_required
def goods_upload(request, store_id):
    """
    上传商品
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 查询商品类型
        goods_101_type = models.GoodsType.objects.filter(parent__isnull=True)
        return render(request, 'goods/goods_upload.html', {'store_id': store_id, 'goods_101_type': goods_101_type})
    elif request.method == 'POST':
        # 获取数据
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        intro = request.POST['intro']
        img_path = request.FILES['img']

        # 类型
        type_id = request.POST['type2']
        goodstype = models.GoodsType.objects.get(pk=type_id)
        store = stores.models.Store.objects.get(pk=store_id)

        # 创建商品对象，完成上传
        goods = models.Goods(name=name, price=price, stock=stock, sales=0, intro=intro, goodstype=goodstype, store=store)
        goods.save()

        # 创建商品图片对象，保存图片
        goods_images = models.GoodsImages(path=img_path, goods=goods)
        goods_images.save()

        # 跳转到商品详情
        # return redirect(reverse('goods:goods_info', kwargs={'goods_id': goods.id}))
        return redirect(reverse('stores:store_info', kwargs={'s_id': store_id}))


@require_GET
def goods_info(request, goods_id):
    """
    查看商品详情
    :param request:
    :return:
    """
    # 获取商品
    goods = models.Goods.objects.get(pk=goods_id)
    return render(request, 'goods/goods_info.html', {'goods': goods})


def goodstype(requset):
    """
    获取二级类型
    :param requset:
    :return:
    """
    # 获取类型编号
    print(111)
    type_id = requset.GET['type_id']
    print(type_id)
    goods_type = models.GoodsType.objects.get(pk=type_id)
    # 查询二级类型对象
    goods_type2_list = models.GoodsType.objects.filter(parent=goods_type)
    # 返回查询到的数据
    return HttpResponse(serialize('json', goods_type2_list))


def man_goods(request):
    """
    男子商品页面
    :param request:
    :return:
    """
    goods_type_1 = goods.models.GoodsType.objects.get(pk=101)
    goods_type_1_list = goods.models.GoodsType.objects.filter(parent=goods_type_1)
    goods_list_1 = goods.models.Goods.objects.filter(goodstype__in=goods_type_1_list)
    print(goods_list_1)
    # 本月主推
    goods_type_4 = goods.models.GoodsType.objects.get(pk=104)
    goods_type_4_list = goods.models.GoodsType.objects.filter(parent=goods_type_4)
    # print(goods_type_1_list)
    goods_list_4 = goods.models.Goods.objects.filter(goodstype__in=goods_type_4_list)
    # print(goods_list_4)
    # 热门推荐
    goods_type_5 = goods.models.GoodsType.objects.get(pk=105)
    goods_type_5_list = goods.models.GoodsType.objects.filter(parent=goods_type_5)
    # print(goods_type_1_list)
    goods_list_5 = goods.models.Goods.objects.filter(goodstype__in=goods_type_5_list)
    return render(request, 'goods/man_goods.html', {"goods_list_1": goods_list_1, "goods_list_4": goods_list_4, "goods_list_5": goods_list_5})


def women_goods(request):
    """
    女子商品页面
    :param request:
    :return:
    """
    goods_type_2 = goods.models.GoodsType.objects.get(pk=102)
    goods_type_2_list = goods.models.GoodsType.objects.filter(parent=goods_type_2)
    goods_list_2 = goods.models.Goods.objects.filter(goodstype__in=goods_type_2_list)
    # 本月主推
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
    return render(request, 'goods/women_goods.html', {"goods_list_2": goods_list_2, "goods_list_4": goods_list_4, "goods_list_5": goods_list_5})


def children_goods(request):
    """
    儿童商品页面
    :param request:
    :return:
    """
    # 本月主推
    goods_type_4 = goods.models.GoodsType.objects.get(pk=104)
    goods_type_4_list = goods.models.GoodsType.objects.filter(parent=goods_type_4)
    # print(goods_type_1_list)
    goods_list_4 = goods.models.Goods.objects.filter(goodstype__in=goods_type_4_list)
    # print(goods_list_4)
    goods_type_3 = goods.models.GoodsType.objects.get(pk=103)
    goods_type_3_list = goods.models.GoodsType.objects.filter(parent=goods_type_3)
    goods_list_3 = goods.models.Goods.objects.filter(goodstype__in=goods_type_3_list)
    # 品牌
    goods_type_5 = goods.models.GoodsType.objects.get(pk=105)
    goods_type_5_list = goods.models.GoodsType.objects.filter(parent=goods_type_5)
    # print(goods_type_1_list)
    goods_list_5 = goods.models.Goods.objects.filter(goodstype__in=goods_type_5_list)
    return render(request, 'goods/children_goods.html', {"goods_list_3": goods_list_3, "goods_list_4": goods_list_4, "goods_list_5": goods_list_5})