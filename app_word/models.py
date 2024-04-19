from django.db import models


class Origin(models.Model):
    origin_name = models.CharField(max_length=255)

    def __str__(self):
        return self.origin_name

    class Meta:
        verbose_name_plural = 'Origins'
        verbose_name = 'origin'
        db_table = 'origins'


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'category'
        db_table = 'categories'


class Word(models.Model):
    word_name = models.CharField(max_length=255)
    word_origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    word_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word_description = models.TextField()
    word_examples = models.TextField()

    def __str__(self):
        return self.word_name

    class Meta:
        verbose_name_plural = 'Words'
        verbose_name = 'word'
        db_table = 'words'
