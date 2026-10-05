"""Models for the recipes app."""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

MIN_COOKING_TIME = 1
MAX_COOKING_TIME = 32000
MIN_INGREDIENT_AMOUNT = 1
MAX_INGREDIENT_AMOUNT = 32000


class Tag(models.Model):
    """Tag model."""

    name = models.CharField(
        'Name',
        max_length=32,
        unique=True
    )
    slug = models.SlugField(
        'Slug',
        max_length=32,
        unique=True
    )

    class Meta:
        """Tag model metadata."""

        ordering = ['name']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Return the string representation of the tag."""
        return self.name


class Ingredient(models.Model):
    """Ingredient model."""

    name = models.CharField(
        'Name',
        max_length=128
    )
    measurement_unit = models.CharField(
        'Measurement unit',
        max_length=64
    )

    class Meta:
        """Ingredient model metadata."""

        ordering = ['name']
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_ingredient'
            )
        ]

    def __str__(self):
        """Return the string representation of the ingredient."""
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    """Recipe model."""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Author'
    )
    name = models.CharField(
        'Name',
        max_length=256
    )
    image = models.ImageField(
        'Image',
        upload_to='recipes/'
    )
    text = models.TextField(
        'Description'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        related_name='recipes',
        verbose_name='Ingredients'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Tags'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Cooking time (minutes)',
        validators=[
            MinValueValidator(MIN_COOKING_TIME),
            MaxValueValidator(MAX_COOKING_TIME)
        ]
    )
    pub_date = models.DateTimeField(
        'Publication date',
        auto_now_add=True
    )

    class Meta:
        """Recipe model metadata."""

        ordering = ['-pub_date']
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        """Return the string representation of the recipe."""
        return self.name


class RecipeIngredient(models.Model):
    """Link between a recipe and an ingredient, with an amount."""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Recipe'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Ingredient'
    )
    amount = models.PositiveSmallIntegerField(
        'Amount',
        validators=[
            MinValueValidator(MIN_INGREDIENT_AMOUNT),
            MaxValueValidator(MAX_INGREDIENT_AMOUNT)
        ]
    )

    class Meta:
        """RecipeIngredient model metadata."""

        ordering = ['id']
        verbose_name = 'Recipe ingredient'
        verbose_name_plural = 'Recipe ingredients'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_ingredient'
            )
        ]

    def __str__(self):
        """Return the string representation of the recipe-ingredient link."""
        return f'{self.ingredient} in {self.recipe}'


class Favorite(models.Model):
    """Favorite model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='User'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Recipe'
    )

    class Meta:
        """Favorite model metadata."""

        ordering = ['-id']
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorite'
            )
        ]

    def __str__(self):
        """Return the string representation of the favorite."""
        return f'{self.user} added {self.recipe} to favorites'


class ShoppingCart(models.Model):
    """Shopping cart model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='User'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Recipe'
    )

    class Meta:
        """ShoppingCart model metadata."""

        ordering = ['-id']
        verbose_name = 'Shopping cart'
        verbose_name_plural = 'Shopping carts'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shopping_cart'
            )
        ]

    def __str__(self):
        """Return the string representation of the shopping cart."""
        return f'{self.user} added {self.recipe} to the shopping cart'
