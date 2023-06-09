# Generated by Django 4.2 on 2023-04-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('hood-001', 'Hood ver.1'), ('hood-002', 'Hood ver.2'), ('hood-003', 'Hood ver.3'), ('jeans-001', 'Jeans')], max_length=10, verbose_name='상품코드')),
                ('name', models.CharField(max_length=50, verbose_name='상품명')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('inventory', models.IntegerField(default=0, verbose_name='재고')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'ExtraLarge'), ('F', 'Free')], max_length=2, verbose_name='사이즈')),
            ],
        ),
    ]
