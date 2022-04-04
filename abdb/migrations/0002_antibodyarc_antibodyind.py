# Generated by Django 4.0.3 on 2022-04-02 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntibodyArc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_num', models.CharField(max_length=200, null=True, unique=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('host', models.CharField(choices=[('Rabbit', 'Rabbit'), ('Mouse', 'Mouse'), ('Rat', 'Rat'), ('Goat', 'Goat'), ('Horse', 'Horse'), ('Chicken', 'Chicken'), ('Guinea Pig', 'Guinea Pig'), ('Other', 'Other')], max_length=200, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('most_recent_lot_num', models.CharField(max_length=200, null=True)),
                ('recommended_WB_concentration', models.CharField(blank=True, max_length=200, null=True)),
                ('recommended_IHC_concentration', models.CharField(blank=True, max_length=200, null=True)),
                ('recommended_IHCp_concentration', models.CharField(blank=True, max_length=200, null=True)),
                ('recommended_IF_concentration', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AntibodyInd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_num', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('aliquoted', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('date_aliq', models.CharField(blank=True, max_length=200, null=True)),
                ('exp_date', models.CharField(max_length=200, null=True)),
                ('amount_remaining', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat_num', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='abdb.antibody', to_field='cat_num')),
            ],
        ),
    ]