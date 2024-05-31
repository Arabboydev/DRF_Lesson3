from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class EmployeeAbout(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.TextField()
    email = models.EmailField(max_length=255)

    class Meta:
        db_table = 'employee_about'

    def __str__(self):
        return f"{self.category.name} {self.name}"




