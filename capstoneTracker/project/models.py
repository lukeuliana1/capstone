from os import path
from django.db import models
from django.utils.text import slugify
from account.models import Student, Employee
from taggit.managers import TaggableManager
# Create your models here.

def image_upload_path(instance, filename):
    return os.path.join("project-images/"+"-".join((instance.title, str(instance.id)))+"/", filename)


class Project(models.Model):
    projects = models.Manager()
    title = models.CharField(max_length=200)
    slug = models.SlugField(
            max_length=200, unique=True, blank=True, editable=True)
    students = models.ForeignKey(Student)
    employees = models.ForeignKey(Employee)
        
    description = models.TextField()
    github = models.URLField(blank=True)
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
        super(Tours, self).save(*args, **kwargs)
        if self.slug == "":
            self.slug = slugify(self.title)
            self.slug = "-".join((self.slug, str(self.id)))

