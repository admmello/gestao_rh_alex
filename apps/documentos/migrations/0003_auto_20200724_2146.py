# Generated by Django 3.0.8 on 2020-07-24 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20200724_2142'),
        ('documentos', '0002_documento_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]