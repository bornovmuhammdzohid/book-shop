from django.db import models

class Car(models.Model):
    
    nom = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    narx = models.IntegerField()
    rang = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Mashina nomi: {self.nom} Brendi: {self.brend} Narxi: ${self.narx} Rangi: {self.rang}"

class Category(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Maxsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Maxsulot nomi: {self.nom} Narxi: {self.narx} som"
    
class Janr(models.Model):
    janrlar = models.CharField(max_length=100)

    def __str__(self):
        return self.janrlar
    
class Books(models.Model):
    img = models.ImageField(null=True)
    nom = models.CharField(max_length=100)
    ovner = models.CharField(max_length=100)
    janr = models.ForeignKey(Janr, on_delete=models.SET_NULL, null=True)
    narx = models.IntegerField()

    def __str__(self):
        return f'Kitobning nomi {self.nom} -- kitobning aftori {self.ovner}'