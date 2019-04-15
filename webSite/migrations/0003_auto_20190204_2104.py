# Generated by Django 2.1.4 on 2019-02-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0002_category_favorite_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['categoryName'], 'verbose_name': 'Catégorie'},
        ),
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['productID'], 'verbose_name': 'Favoris', 'verbose_name_plural': 'Favoris'},
        ),
        migrations.AddField(
            model_name='product',
            name='imgURL',
            field=models.URLField(null=True, verbose_name="URL de l'image du produit"),
        ),
    ]
