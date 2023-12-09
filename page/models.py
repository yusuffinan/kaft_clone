from django.db import models

STATUS_DEFAULT = "draft"
STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('delted', 'Silindi')
]

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", db_index=True, blank=True, unique=True, null= False, max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(blank=True, null=True, upload_to="page")
    status = models.CharField(default=STATUS_DEFAULT, choices=STATUS, max_length=10)
    created_att = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
class Carousel(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True, upload_to="Carousel")
    status = models.CharField(default=STATUS_DEFAULT, choices=STATUS, max_length=10)
    createt_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)