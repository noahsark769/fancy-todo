from django.db import models

class ListItem(models.Model):
	text = models.CharField(max_length=300)
	is_visible = models.BooleanField()
