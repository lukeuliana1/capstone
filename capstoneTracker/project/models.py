from os import path
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
# Create your models here.

def image_upload_path(instance, filename):
    return path.join("project-images/"+"-".join((instance.title, str(instance.id)))+"/", filename)


class Project(models.Model):
    manager = models.Manager()
    title = models.CharField(max_length=200)
    slug = models.SlugField(
            max_length=200, unique=True, blank=False, editable=True)    
    brief_description = models.CharField(max_length=100)
    description = models.TextField()
    github = models.CharField(max_length=100, blank=True)
    trello = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(sefl):
        return sefl.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        if self.slug == "":
            self.slug = slugify(self.title)
            self.slug = "-".join((self.slug, str(self.id)))


