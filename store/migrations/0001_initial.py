# Generated by Django 4.0.1 on 2022-01-26 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Product_relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('size', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('product_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_color', to='store.product')),
                ('product_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_image', to='store.product')),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_size', to='store.product')),
            ],
        ),
    ]
