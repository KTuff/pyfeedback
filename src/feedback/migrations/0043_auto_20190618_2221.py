# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-18 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0042_auto_20180608_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='FragebogenUE2016',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fach', models.CharField(blank=True, choices=[('inf', 'Informatik'), ('math', 'Mathematik'), ('ce', 'Computational Engineering'), ('ist', 'Informationssystemtechnik'), ('etit', 'Elektrotechnik'), ('psyit', 'Psychologie in IT'), ('winf', 'Wirtschaftsinformatik'), ('sonst', 'etwas anderes')], max_length=5)),
                ('abschluss', models.CharField(blank=True, choices=[('bsc', 'Bachelor'), ('msc', 'Master'), ('dipl', 'Diplom'), ('lehr', 'Lehramt'), ('sonst', 'anderer Abschluss')], max_length=5)),
                ('semester', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '>=10')], max_length=4)),
                ('geschlecht', models.CharField(blank=True, choices=[('w', 'weiblich'), ('m', 'männlich'), ('s', 'sonstiges')], max_length=1)),
                ('studienberechtigung', models.CharField(blank=True, choices=[('d', 'Deutschland'), ('o', 'anderes Land')], max_length=1)),
                ('ue_wie_oft_besucht', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_besuch_ueberschneidung', models.CharField(blank=True, choices=[('j', 'ja'), ('n', 'nein')], max_length=1)),
                ('ue_besuch_qualitaet', models.CharField(blank=True, choices=[('j', 'ja'), ('n', 'nein')], max_length=1)),
                ('ue_besuch_verhaeltnisse', models.CharField(blank=True, choices=[('j', 'ja'), ('n', 'nein')], max_length=1)),
                ('ue_besuch_privat', models.CharField(blank=True, choices=[('j', 'ja'), ('n', 'nein')], max_length=1)),
                ('ue_besuch_elearning', models.CharField(blank=True, choices=[('j', 'ja'), ('n', 'nein')], max_length=1)),
                ('ue_besuch_zufrueh', models.CharField(blank=True, choices=[('j', 'ja'), ('n', 'nein')], max_length=1)),
                ('ue_besuch_sonstiges', models.CharField(blank=True, choices=[('j', 'ja'), ('n', 'nein')], max_length=1)),
                ('ue_3_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_3_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_3_3', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_3_4', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_3_5', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_3_6', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_3_7', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_3_8', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_3', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_4', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_5', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_6', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_7', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_8', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_9', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_4_10', models.CharField(blank=True, max_length=1)),
                ('ue_4_11', models.CharField(blank=True, max_length=1)),
                ('kennziffer', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_3', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_4', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_5', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_6', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_7', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_8', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_9', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_10', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_11', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_12', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_13', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_14', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_15', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_5_16', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_6_1', models.CharField(blank=True, choices=[('0', '0'), ('1', '0.5'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4'), ('6', '5'), ('7', '>=5')], max_length=1)),
                ('ue_6_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ue_6_3', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('veranstaltung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Veranstaltung')),
            ],
            options={
                'verbose_name': 'Übungsfragebogen 2016',
                'verbose_name_plural': 'Übungfragebögen 2016',
                'ordering': ['semester', 'veranstaltung'],
            },
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_arbeitsbedingungen',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_arbeitsbedingungen_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_didaktik',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_didaktik_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_feedbackpreis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_feedbackpreis_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_lernerfolg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_lernerfolg_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_organisation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_organisation_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_umgang',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ergebnis2016',
            name='ue_umgang_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]