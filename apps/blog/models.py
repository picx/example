from django.db import models

class Author(models.Model):
	full_name = models.CharField('Author Name', max_length = 50)
	email = models.EmailField('Author Email', unique = True)
	bio = models.TextField('Author Biography')
	def __str__(self):
		return self.full_name
	
class Category(models.Model):
	name = models.CharField('Category Name', max_length = 50)
	description = models.CharField('Category Description', max_length = 255)
	class Meta:
		verbose_name_plural = 'Categories'
		
	def __str__(self):
		return self.name
	
class Tag(models.Model):
	name = models.CharField('Tag Name', max_length = 50)
	description = models.CharField('Tag Description', max_length = 255)
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField('Post Title', max_length = 50)
	body = models.TextField('Post Body')
	created_at = models.DateTimeField(auto_now_add = True, auto_now = False) 
	updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)
	author = models.ForeignKey(Author)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)
	def __str__(self):
		return self.title
	