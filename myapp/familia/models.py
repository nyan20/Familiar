
from django.db import models

PARENTESCO =(
	('1', 'Madre'), 
	('2', 'Padre'),	
	('3', 'Abuelo'),
	('4', 'Abuela'), 
	('5', 'Tio'),	
	('6', 'Tia'),
	('7', 'Primo'),	
	('8', 'Prima'),	
	('9', 'Hermano'),
	('10', 'Hermana'), 
	('11', 'Esposo'), 
	('12', 'Esposa'),
)

class Familia (models.Model):
	parentesco = models.CharField(max_length=15, choices=PARENTESCO)
	nombre = models.CharField(max_length=255)
	fecha_nac = models.DateField()
	escolaridad = models.CharField(max_length=250, blank = True, null= True)
