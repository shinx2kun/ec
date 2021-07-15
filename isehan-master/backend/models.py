from django.db import models
from users.models import User

# Create your models here.
class ParentCategory(models.Model):
    class Meta:
        verbose_name = '親カテゴリー'
        verbose_name_plural = '親カテゴリー'

    name = models.CharField(
        verbose_name = '名前',
        max_length = 20,
        default = '',
        null = True,
        blank = True,
    )
    def __str__(self):
        return self.name

class ChildCategory(models.Model):
    class Meta:
        verbose_name = '子カテゴリー'
        verbose_name_plural = '子カテゴリー'

    name = models.CharField(
        verbose_name = '名前',
        max_length = 20,
        default = '',
        null = True,
        blank = True,
    )
    parent_category = models.ForeignKey(
        ParentCategory,
        verbose_name='親カテゴリー',
        related_name='child',
        on_delete=models.CASCADE,
        null = True,
        blank = True,
    )
    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    thumbnail = models.ImageField(
        verbose_name = 'サムネ画像',
        upload_to = 'thumbnails/',
        null = True,
        blank = True,
    )
    name = models.CharField(
        verbose_name = '名前',
        max_length = 100,
        null = True,
        blank = True,
    )
    price = models.IntegerField(
        verbose_name = '価格',
        null = True,
        blank = True,
    )
    description1 = models.TextField(
        verbose_name = '商品説明1',
        null = True,
        blank = True,
    )
    description2 = models.TextField(
        verbose_name = '商品説明2',
        null = True,
        blank = True,
    )
    description3 = models.TextField(
        verbose_name = '商品説明3',
        null = True,
        blank = True,
    )
    parent_category = models.ForeignKey(
        ParentCategory,
        verbose_name = '親カテゴリー',
        related_name = 'parent_category',
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )
    child_category = models.ManyToManyField(
        ChildCategory,
        verbose_name='子カテゴリー',
        related_name='child_category',
        null=True,
        blank=True,
    )

class ProductImage(models.Model):
    class Meta:
        verbose_name = '商品画像'
        verbose_name_plural = '商品画像'

    image = models.ImageField(
        verbose_name = '商品画像',
        upload_to = 'images/',
        null = True,
        blank = True,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='商品',
        related_name='image',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

class ProductCompositionTable(models.Model):
    class Meta:
        verbose_name = '成分表'
        verbose_name_plural = '成分表'

    title = models.TextField(
        verbose_name='タイトル',
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name = '説明',
        null = True,
        blank = True,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='商品',
        related_name='description',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

# ショッピングカート
class ShoppingCart(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='ユーザ',
        related_name='shopping_cart',
        on_delete=models.CASCADE
    )
    total_price = models.IntegerField(
        verbose_name='合計金額',
        null=True,
        blank=True,
    )


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(
        ShoppingCart,
        related_name = 'cart_items',
        verbose_name = 'ショッピングカート',
        on_delete = models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        verbose_name = '商品',
        on_delete = models.CASCADE,
        null=True,
        blank=True,
    )
    amount = models.IntegerField(
        verbose_name = '数量',
        null = True,
        blank = True,
    )