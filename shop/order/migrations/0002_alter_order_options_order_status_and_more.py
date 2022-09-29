# Generated by Django 4.1.1 on 2022-09-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_ordered']},
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(help_text='Status of order from storehouse', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, help_text='Status of confirming order in cart'),
        ),
    ]
