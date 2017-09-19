# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Keg, Recipe, KegRecipe
# Register your models here.


class KegAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'owner')
    fields = ('id', 'name', 'created', 'owner',)
    list_display = ('id', 'name', 'created', 'owner',)


class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'owner')
    fields = ('id', 'name', 'created', 'owner',)
    list_display = ('id', 'name', 'created', 'owner',)


class KegRecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    fields = ('keg_id', 'recipe_id', 'created', 'is_active',)
    fields = ('keg_id', 'recipe_id', 'created', 'is_active',)


admin.site.register(Keg, KegAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(KegRecipe, KegRecipeAdmin)
