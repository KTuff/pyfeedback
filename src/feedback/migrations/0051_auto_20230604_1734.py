# Generated by Django 2.2.28 on 2023-06-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0050_remove_fragebogen2020_v_7_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veranstaltung',
            name='digitale_eval',
            field=models.BooleanField(blank=True, default=True, help_text='Die Evaluation soll digital durchgeführt werden. Die Studierenden füllen die Evaluation online aus.', verbose_name='Digitale Evaluation'),
        ),
    ]