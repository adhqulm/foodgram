"""Административная конфигурация приложения рецептов."""

from django.contrib import admin

from .models import (
    Favorite, Ingredient, Recipe, RecipeIngredient, ShoppingCart, Tag
)


class RecipeIngredientInline(admin.TabularInline):
    """Инлайн для ингредиентов в рецепте."""

    model = RecipeIngredient
    extra = 1
    min_num = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Админка для тегов."""

    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Админка для ингредиентов."""

    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Админка для рецептов."""

    list_display = (
        'id',
        'name',
        'author',
        'cooking_time',
        'get_favorites_count'
    )
    search_fields = ('name', 'author__username')
    list_filter = ('author', 'tags')
    inlines = (RecipeIngredientInline,)

    def get_favorites_count(self, obj):
        """Получение количества добавлений в избранное."""
        return obj.favorites.count()

    get_favorites_count.short_description = 'В избранном'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Админка для избранного."""

    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Админка для списка покупок."""

    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user', 'recipe')
