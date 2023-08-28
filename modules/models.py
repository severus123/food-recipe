from django.db import models


class recipes(models.Model):#creatint the model so that we can enter the recipes and add it to the database
    recipe_image=models.ImageField(upload_to="recipess/",max_length=500,null=True,default=None)
    recipe_name=models.CharField(max_length=100)
    intro=models.CharField(max_length=1000)
    ingredients=models.CharField(max_length=1000)
    making=models.CharField(max_length=1000)
    nut=models.CharField(max_length=100)
    protein=models.CharField(max_length=100)

class chef(models.Model):
    chef_name=models.CharField(max_length=100)
    chef_age=models.PositiveIntegerField()
    chef_exp=models.CharField(max_length=500)
    chef_info=models.CharField(max_length=1000)
    recipe_name = models.ForeignKey(recipes, on_delete=models.CASCADE)
    chef_img=models.FileField(upload_to="chefs/",max_length=1000,null=True,default=None)

    # Create your models here.

    
