# Generated by Django 4.2.3 on 2023-07-14 23:43

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('category_image', models.ImageField(blank=True, upload_to='Category Image/')),
                ('category_description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('category_status', models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active')], max_length=10, verbose_name='Status')),
                ('category_slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('category_create_at', models.DateTimeField(auto_now_add=True)),
                ('category_update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=50, unique=True, verbose_name='Code')),
                ('product_name', models.CharField(max_length=150, verbose_name='Product Name')),
                ('product_description_englih', models.TextField(max_length=255, verbose_name='Description EN')),
                ('product_description_arabic', models.TextField(max_length=255, verbose_name='Description AR')),
                ('product_cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('product_price_after_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Price Ater Discount')),
                ('product_discount_start_date', models.DateField(verbose_name='Discount Start Date')),
                ('product_discount_start_enddate', models.DateField(verbose_name='Discount End Datet')),
                ('product_variant', models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], default='None', max_length=10)),
                ('product_slug', models.SlugField(unique=True)),
                ('product_status', models.BooleanField()),
                ('product_create_at', models.DateTimeField(auto_now_add=True)),
                ('product_update_at', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='Product images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
