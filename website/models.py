from django.db import models

from website.random_primary import RandomPrimaryIdModel

class OneWord(RandomPrimaryIdModel):
    word = models.CharField(max_length=255, blank=False, null=False)
    footer = models.CharField(max_length=1024, blank=True, null=True)
    bg_color = models.CharField(max_length=7, default="#e74c3c")
    fg_color = models.CharField(max_length=7, default="#c0392b")
    
