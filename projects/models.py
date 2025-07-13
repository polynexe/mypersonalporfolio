# mypersonalportfolio/projects/models.py

from django.db import models
from django.utils.text import slugify

# Define the Project model to store information about each portfolio project.
class Project(models.Model):
    """
    Represents a project entry in the portfolio.

    Fields:
    - name: The title or name of the project.
    - description: A detailed description of the project.
    - created_at: The date and time when the project entry was created.
    - updated_at: The date and time when the project entry was last updated.
    - slug: A URL-friendly version of the project name, used for clean URLs.
            It's unique to prevent conflicts and allows for direct linking.
    - image: An optional image associated with the project.
             Requires Pillow to be installed (`pip install Pillow`).
    - live_url: An optional URL to the live demo of the project.
    - github_url: An optional URL to the project's GitHub repository.
    """
    name = models.CharField(max_length=200, help_text="The name of the project.")
    description = models.TextField(help_text="A detailed description of the project.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time the project was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time the project was last updated.")

    # Optional fields for a more complete portfolio item:
    # Slug for clean URLs (e.g., /projects/my-awesome-project/)
    slug = models.SlugField(unique=True, max_length=250, blank=True, null=True,
                            help_text="A URL-friendly slug generated from the project name.")
    # Image for the project (requires Pillow: pip install Pillow)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True,
                              help_text="An optional image representing the project.")
    # URL to a live demo of the project
    live_url = models.URLField(max_length=200, blank=True, null=True,
                               help_text="Optional URL to the live demo of the project.")
    # URL to the project's GitHub repository
    github_url = models.URLField(max_length=200, blank=True, null=True,
                                 help_text="Optional URL to the project's GitHub repository.")


    # Override the save method to automatically generate the slug
    def save(self, *args, **kwargs):
        if not self.slug: # Generate slug only if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # Define how the object is represented as a string (useful in Django Admin)
    def __str__(self):
        return self.name

    # Define metadata options for the model
    class Meta:
        ordering = ['-created_at'] # Order projects by creation date, newest first
        verbose_name = "Project"
        verbose_name_plural = "Projects"
