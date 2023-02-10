from django.db import models


class Car(models.Model):
    AT = 'AT'
    MA = 'MA'
    CAMBIO = [
        (AT, 'Automatic'),
        (MA, 'Manual')
    ]
    name = models.CharField(
        'Nome',
        max_length=50
    )
    price = models.DecimalField(
        'Preço',
        decimal_places=2,
        max_digits=5
    )
    year = models.SmallIntegerField(
        'Ano'
    )
    transmission = models.CharField(
        'Transmissão',
        max_length=2,
        choices=CAMBIO,
        default=MA,
    )
    manufacturer = models.ForeignKey(
        'Manufacturer',
        verbose_name='Fabricante',
        on_delete=models.CASCADE,
        related_name='cars'
    )

    def __str__(self):
        return f'{self.name} - {self.model}'

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['name']

class Manufacturer(models.Model):
    name = models.CharField(
        'nome',
        max_length=20
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'


class City(models.Model):
    name = models.CharField(
        'Nome',
        max_length=50
    )
    state = models.ManyToManyField(
        'State',
        verbose_name='Estado'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class State(models.Model):
    SP = 'sp'
    RJ = 'rj'
    STATE = [
        (SP, 'São Paulo'),
        (RJ, 'Rio de Janeiro'),
    ]
    name = models.CharField(
        'Nome',
        max_length=2,
        choices=STATE,
        default=SP
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
