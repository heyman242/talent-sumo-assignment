# Generated by Django 4.2.2 on 2023-06-21 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type', models.CharField(choices=[('text', 'Text'), ('audio', 'Audio'), ('video', 'Video')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shared_with', models.ManyToManyField(blank=True, related_name='shared_notes', to='notes.registereduser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='notes.registereduser')),
            ],
        ),
    ]