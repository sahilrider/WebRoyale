from django.db import models

# Create your models here.

class Typ(models.Model):
	name=models.CharField(max_length=20)
	def __str__(self):
		return self.name

class Arena(models.Model):
	name=models.CharField(max_length=30,default='Training Camp')
	number=models.IntegerField(primary_key=True)
	def __str__(self):
		return self.name

class Rarity(models.Model):
	name=models.CharField(max_length=20)
	def __str__(self):
		return self.name

class Crd(models.Model):
	name=models.CharField(max_length=25)
	typ=models.ForeignKey(Typ,on_delete=models.CASCADE)
	elixir=models.IntegerField()
	description=models.TextField()
	rarity=models.ForeignKey(Rarity,on_delete=models.CASCADE)
	arena=models.ForeignKey(Arena,on_delete=models.CASCADE)

	def __str__(self):
		return self.name