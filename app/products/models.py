from django.conf import settings
from django.db import models


class Product(models.Model):

    # BREAD_TYPE_WHITE = 'WHI'
    # BREAD_TYPE_HEARTY = 'HEA'
    # BREAD_TYPE_PARMESAN = 'PAR'
    # BREAD_TYPE_WHEAT = 'WHE'
    # BREAD_TYPE_HONEYOAT = 'HON'
    # BREAD_TYPE_FLAT = 'FLA'
    #
    # BREAD_TYPE_CHOICES = (
    #     (BREAD_TYPE_WHITE, '화이트'),
    #     (BREAD_TYPE_HEARTY, '하티'),
    #     (BREAD_TYPE_PARMESAN, '파마산오레가노'),
    #     (BREAD_TYPE_WHEAT, '위트'),
    #     (BREAD_TYPE_HONEYOAT, '허니오트'),
    #     (BREAD_TYPE_FLAT, '플랫'),
    # )

    # breads = models.CharField(
    #     max_length=3,
    #     choices=BREAD_TYPE_CHOICES,
    #     verbose_name='빵',
    # )

    breads = models.OneToOneField(
        'breads',
        max_length=3,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name='빵',
    )
    vegetables = models.ManyToManyField(
        'vegetables',
        blank=True,
        verbose_name='야채',
    )

    product_maker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='레시피 제작자',
    )
    img_profile = models.ImageField(upload_to='user', blank=True)
    img_profile_thumbnail = models.ImageField(upload_to='user', blank=True)

    def __str__(self):
        return f'{self.pk} : {self.breads}|{list(self.vegetables.all().values_list("name", flat=True))}'


class Breads(models.Model):
    """
    Product와 OneToOneField로 연결된 bread
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='100자까지의 bread의 이름을 저장합니다.',
    )

    class Meta:
        verbose_name_plural = '선택한 breads'

    def __str__(self):
        return self.name


class Vegetables(models.Model):
    """
    Product와 ManyToMany로 연결된 vegetables
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='100자까지의 vegetable의 이름을 저장합니다.',
    )

    class Meta:
        verbose_name_plural = '선택한 vegetables'

    def __str__(self):
        return self.name
