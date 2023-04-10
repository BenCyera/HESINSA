from django.db import models


# model
class Product(models.Model):
    # 상품코드
    codes = (
        ('hood-001', 'Hood ver.1'),
        ('hood-002', 'Hood ver.2'),
        ('hood-003', 'Hood ver.3'),
        ('jeans-001', 'Jeans'),
        ('socks-001', 'Socks'),
        ('bucket_hat-001', 'Bucket_hat')
    )
    code = models.CharField(choices=codes, max_length=30, verbose_name="상품 코드")
    # 이름
    NAMES = {
        'hood-001': '빵빵덕 후드티',
        'hood-002': '망곰이 후드티',
        'hood-003': '고심이 후드티',
        'jeans-001': 'Y2K',
        'socks-001': '쫀쫀이 양말',
        'bucket_hat-001': '네가 쓰면 등산객 내가 쓰면 패피'
    }
    name = models.CharField(max_length=50, verbose_name="상품명")
    # 설명
    description = models.TextField(verbose_name="상품 설명")
    # 가격
    price = models.IntegerField(verbose_name="가격")
    # 갯수. 초기갯수는 0개
    inventory = models.IntegerField(default=0, verbose_name="수량")
    input_date = models.DateField(auto_now=False, verbose_name="입고")
    output_date = models.DateField(auto_now=False, verbose_name="출고")
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=2, verbose_name="사이즈")

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        self.name = self.NAMES.get(self.code, '')
        if self.id is not None:
            self.inventory += models.IntegerField(verbose_name="수량")
        super().save(*args, **kwargs)


# model
class Inbound(models.Model):
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)


    def save(self, *args, **kwargs):
        self.product.save()
        super().save(*args, **kwargs)


class Outbound(models.Model):
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    input_date = models.DateField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        self.product.save()
        super().save(*args, **kwargs)