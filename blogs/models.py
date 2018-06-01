from django.db import models

class BlogPost(models.Model):
    """A single blogpost from the user."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'blogposts'

    def __str__(self):
        """Return a string representation of the model."""

        return self.title
