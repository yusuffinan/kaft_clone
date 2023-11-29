from django.db import models

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('delted', 'Silindi')
]

class Page(models.Model):
    title = models.CharField(max_length=200)
    # slug = models.SlugField()
    content = models.TextField()
    cover_image = models.ImageField(upload_to="page")
    status = models.CharField(default="draft", choices=STATUS, max_length=10)
    created_att = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)
