# Generated by Django 5.0.4 on 2024-06-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cita',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.TextField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'contacto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='detalle_factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_citas_pendientes', models.IntegerField(blank=True, null=True)),
                ('abono', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detalle_factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('block', models.CharField(blank=True, max_length=50, null=True)),
                ('departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='diseños',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('estilo', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'diseños',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'emails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'estudio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'materiales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='metodo_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'metodo_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='portafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('foto', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'portafolio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=45, null=True)),
                ('cuerpo', models.CharField(blank=True, max_length=200, null=True)),
                ('calificacion', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reseña',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='tatuador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'tatuador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'telefono',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='transacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'transacciones',
                'managed': False,
            },
        ),
    ]
