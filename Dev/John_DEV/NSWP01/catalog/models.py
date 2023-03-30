
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique shoe instances

from datetime import date
# Create your models here.


#models for COLOR, BRAND, SIZE, and TYPE
# class color(models.Model):
#     '''model representing a shoe color'''
#     name = models.CharField(max_length=200, help_text='Enter a Shoe Color (Red, Black, White, Tan)')
#
#     def __str__(self):
#         '''string for representing the Model Object.'''
#         return self.name
# class Brand(models.Model):
#     """Model representing shoe brand."""
#     name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Nike, Addidas, Converse, Etc.)')
#
#     def get_absolute_url(self):
#         """Returns the URL to access a particular brand instance."""
#
#         return reverse('brand_detail', args=[str(self.id)])
#     def __str__(self):
#     """String for representing the Model object."""
#         return f''
#
# class Size(models.Model):
#     '''Model representing shoe size.'''
