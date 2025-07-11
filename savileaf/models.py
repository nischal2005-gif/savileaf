from django.db import models
from django.urls import reverse

class DropdownMenuItem(models.Model):
    label = models.CharField(max_length=100, help_text="Text to display in the dropdown")
    url_name = models.SlugField(unique=True, help_text="Slug used in URL: /services/<slug>/")
    section_title = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    features = models.JSONField(default=list, blank=True)  # Example: [{'title': '', 'description': ''}]
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='services/hero/', blank=True, null=True)
    slug = models.SlugField(unique=True,null=True)
    
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Dropdown Menu Item"
        verbose_name_plural = "Dropdown Menu Items"

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.url_name})


class FooterService(models.Model):
    name = models.CharField(max_length=100,null=True)
    url_name = models.CharField(max_length=100, help_text="Enter the Django URL pattern name",null=True)
    slug = models.SlugField(max_length=200, help_text="Slug used in the URL", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        try:
            return reverse(self.url_name, kwargs={'slug': self.slug})  
        except:
            return "#"