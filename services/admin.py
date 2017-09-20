# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Keg, Recipe, KegRecipe
# Register your models here.


class KegAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_by', 'created_on')
    fields = ('id', 'name', 'created_by', 'created_on',)
    list_display = ('id', 'name', 'created_by', 'created_on',)


class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_by', 'created_on')
    fields = ('id', 'name', 'created_by', 'created_on',)
    list_display = ('id', 'name', 'created_by', 'created_on',)


class KegRecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    fields = ('keg_id', 'recipe_id', 'is_active', 'created_on',)
    list_display = ('id', 'is_active', 'created_on',)


admin.site.register(Keg, KegAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(KegRecipe, KegRecipeAdmin)
