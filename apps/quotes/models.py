from django.db import models
from apps.accounts.models import User


class Quote(models.Model):
	posted_id = models.ForeignKey(User)
	quote_by = models.TextField(max_length=50)
	quote_txt = models.TextField(max_length=255)
	class Meta:
		db_table = 'quote'

class Favorite(models.Model):
	usr_id = models.ForeignKey(User)
	quote_id = models.ForeignKey(Quote)
	class Meta:
		db_table = 'fvort'

