from django.contrib import admin
from modules.models import recipes
from modules.models import chef

class fooding(admin.ModelAdmin):
    list_display=('recipe_name','intro','ingredients','making','nut','protein','recipe_image')

class chefs(admin.ModelAdmin):
    list_display=('chef_name','chef_age','chef_exp','chef_info','recipe_name','chef_img')

admin.site.register(recipes,fooding)
admin.site.register(chef,chefs)#if we want to display the model in admin we have to register it here
# Register your models here.
