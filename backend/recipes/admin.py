"""Admin configuration for the recipes app."""

from django.contrib import admin

from .models import (
    Favorite, Ingredient, Recipe, RecipeIngredient, ShoppingCart, Tag
)


class RecipeIngredientInline(admin.TabularInline):
    """Inline for ingredients in a recipe."""

    model = RecipeIngredient
    extra = 1
    min_num = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin for tags."""

    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Admin for ingredients."""

    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Admin for recipes."""

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
        """Get how many times the recipe was favorited."""
        return obj.favorites.count()

    get_favorites_count.short_description = 'In favorites'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Admin for favorites."""

    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Admin for shopping carts."""

    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user', 'recipe')
