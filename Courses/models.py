from django.db import models as md 
from djongo import models
from django.utils.text import slugify

class Courses(models.Model):
    training_type = [
        ("Live","Live"),
        ("Pre-recorded","Pre-recorded"),
        ("LMS-Based","LMS-Based"),
        ("Read & Acknowledge","Read & Acknowledge"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255,choices=training_type)
    max_attempts = models.IntegerField(null=True,blank=True)
    status = models.BooleanField(default=False)
    duration_in_days = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255,blank=True ,null= True)
    # supervisor = models.ForeignKey(on_delete=models.DO_NOTHING)
    # created_by = models.ForeignKey(on_delete=models.DO_NOTHING)
    # badge_arrayId = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    ## create slug on each specific save ##
    def save(self, *args , **keargs):
        self.slug = slugify(self.title)
        return super().save(*args , **keargs)
    
    class Meta:
        db_table = "courses"

