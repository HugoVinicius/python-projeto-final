# Generated by Django 3.0.6 on 2020-06-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20200608_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaspagar',
            name='situacao',
            field=models.CharField(choices=[('1', 'Pago'), ('2', 'A pagar')], default=2, max_length=4),
        ),
        migrations.AlterField(
            model_name='contasreceber',
            name='situacao',
            field=models.CharField(choices=[('1', 'Recebido'), ('2', 'A receber')], default=2, max_length=4),
        ),
    ]
