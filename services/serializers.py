from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Keg, Recipe, KegRecipe


class UserSerializer(serializers.ModelSerializer):
    # kegs = serializers.PrimaryKeyRelatedField(many=True, queryset=Keg.objects.all())
    # recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class KegSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Keg
        fields = ('id', 'name', 'volume', 'created_by', 'created_on')


class RecipeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'srm', 'ibus', 'created_by', 'created_on')


class KegRecipeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = KegRecipe
        fields = ('keg_id', 'recipe_id', 'is_active', 'created_on')
