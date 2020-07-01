# Generated by Django 3.0.7 on 2020-07-01 20:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('choice_type', models.CharField(max_length=12, verbose_name="Type de choix. 'UNIQUE' pour des ptits ronds, 'MULTIPLE' pour des carrés, 'POURCENT' pour des pourcentages")),
            ],
            options={
                'verbose_name': 'Sondage',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='VoteHash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.SlugField(max_length=32)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
            options={
                'verbose_name': 'Choix',
                'ordering': ['poll'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=300)),
                ('votes', models.FloatField(default=0)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
            options={
                'verbose_name': 'Choix',
            },
        ),
    ]
