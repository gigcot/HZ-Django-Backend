# Generated by Django 4.2.13 on 2024-06-19 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodcart',
            fields=[
                ('foodcartId', models.AutoField(primary_key=True, serialize=False)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foodcarts', to='account.account')),
            ],
            options={
                'db_table': 'foodcart',
            },
        ),
        migrations.CreateModel(
            name='FoodcartItem',
            fields=[
                ('foodcartItemId', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foodcart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='foodcart.foodcart')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
            ],
            options={
                'db_table': 'foodcart_item',
            },
        ),
    ]
