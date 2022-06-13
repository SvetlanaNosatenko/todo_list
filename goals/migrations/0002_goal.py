# Generated by Django 4.0.1 on 2022-06-12 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
                ('title', models.CharField(max_length=255, verbose_name='Цель')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Описание')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'К выполнению'), (2, 'В процессе'), (3, 'Выполнено'), (4, 'Архив')], default=1, verbose_name='Статус')),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Низкий'), (2, 'Средний'), (3, 'Высокий'), (4, 'Критический')], default=2, verbose_name='Приоритет')),
                ('due_date', models.DateField(blank=True, default=None, null=True, verbose_name='Дедлайн')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.goalcategory', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goals', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Цель',
                'verbose_name_plural': 'Цели',
            },
        ),
    ]
