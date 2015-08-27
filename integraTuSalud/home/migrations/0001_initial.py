# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('autor', models.CharField(max_length=200)),
                ('contenido', tinymce.models.HTMLField()),
                ('imagen', models.ImageField(upload_to=b'static/img/')),
                ('etiqueta', models.CharField(default=b'MED', max_length=3, choices=[(b'MED', b'MEDICINA'), (b'FIS', b'FISIOTERAPIA'), (b'ODO', b'ODONTOLOGIA'), (b'EST', b'ESTUDIANTIL')])),
                ('fecha', models.DateTimeField(verbose_name=b'fecha de publicacion')),
            ],
        ),
    ]
