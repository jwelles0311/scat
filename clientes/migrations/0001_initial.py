# Generated by Django 5.1.3 on 2024-12-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('cnpj', models.CharField(max_length=14, primary_key=True, serialize=False, unique=True, verbose_name='CNPJ')),
                ('corporate_reason', models.CharField(max_length=100, verbose_name='Cliente')),
                ('address', models.CharField(max_length=50, verbose_name='Endereço')),
                ('number', models.CharField(max_length=10, verbose_name='Numero')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2)),
                ('contact', models.CharField(max_length=30, verbose_name='Contato')),
                ('phone', models.CharField(max_length=10, verbose_name='Tel')),
                ('cell', models.CharField(max_length=11, verbose_name='Cel')),
            ],
            options={
                'ordering': ['corporate_reason'],
            },
        ),
    ]
