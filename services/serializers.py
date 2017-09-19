from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Keg, Recipe, KegRecipe


class UserSerializer(serializers.ModelSerializer):
    kegs = serializers.PrimaryKeyRelatedField(many=True, queryset=Keg.objects.all())
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'kegs', 'recipes')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class KegSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Keg
        fields = ('id', 'name', 'owner', 'created')


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'owner', 'srm', 'ibus', 'created')


class KegRecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = KegRecipe
        fields = ('keg_id', 'recipe_id', 'is_active', 'created')