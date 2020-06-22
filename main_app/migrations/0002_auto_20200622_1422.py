# Generated by Django 3.0.5 on 2020-06-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='size',
            field=models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='XS', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=100),
        ),
    ]