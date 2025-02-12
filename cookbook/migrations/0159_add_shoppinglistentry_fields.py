# Generated by Django 3.2.7 on 2021-10-01 20:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
from django_scopes import scopes_disabled

from cookbook.models import PermissionModelMixin


def copy_values_to_sle(apps, schema_editor):
    with scopes_disabled():
        ShoppingListEntry = apps.get_model('cookbook', 'ShoppingListEntry')
        entries = ShoppingListEntry.objects.all()
        for entry in entries:
            if entry.shoppinglist_set.first():
                entry.created_by = entry.shoppinglist_set.first().created_by
                entry.space = entry.shoppinglist_set.first().space
        if entries:
            ShoppingListEntry.objects.bulk_update(entries, ["created_by", "space", ])


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0158_userpreference_use_kj'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglistentry',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shoppinglistentry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppinglistentry',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpreference',
            name='shopping_share',
            field=models.ManyToManyField(blank=True, related_name='shopping_share', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoppinglistentry',
            name='space',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cookbook.space'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppinglistrecipe',
            name='mealplan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.mealplan'),
        ),
        migrations.AddField(
            model_name='shoppinglistrecipe',
            name='name',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AddField(
            model_name='shoppinglistentry',
            name='ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.ingredient'),
        ),
        migrations.AlterField(
            model_name='shoppinglistentry',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cookbook.unit'),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='mealplan_autoadd_shopping',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='mealplan_autoexclude_onhand',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shoppinglistentry',
            name='list_recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='cookbook.shoppinglistrecipe'),
        ),
        migrations.CreateModel(
            name='FoodInheritField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            bases=(models.Model, PermissionModelMixin),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='mealplan_autoinclude_related',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='food',
            name='inherit_fields',
            field=models.ManyToManyField(blank=True, to='cookbook.FoodInheritField'),
        ),
        migrations.AddField(
            model_name='space',
            name='food_inherit',
            field=models.ManyToManyField(blank=True, to='cookbook.FoodInheritField'),
        ),
        migrations.AddField(
            model_name='shoppinglistentry',
            name='delay_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='default_delay',
            field=models.DecimalField(decimal_places=4, default=4, max_digits=8),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='filter_to_supermarket',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='shopping_recent_days',
            field=models.PositiveIntegerField(default=7),
        ),
        migrations.RenameField(
            model_name='food',
            old_name='ignore_shopping',
            new_name='food_onhand',
        ),
        migrations.AddField(
            model_name='space',
            name='show_facet_count',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(copy_values_to_sle),
    ]
