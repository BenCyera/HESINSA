# Generated by Django 4.2 on 2023-04-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_input_time_product_out_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='input_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='out_time',
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(choices=[('hood-001', 'Hood ver.1'), ('hood-002', 'Hood ver.2'), ('hood-003', 'Hood ver.3'), ('jeans-001', 'Jeans'), ('socks-001', 'Socks'), ('bucket_hat-001', 'Bucket_hat')], max_length=30, verbose_name='상품 코드'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='상품 설명'),
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=0, verbose_name='수량'),
        ),
    ]
