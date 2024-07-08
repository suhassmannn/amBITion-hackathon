from django.db import models

# class categories(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return f'{self.name}'

class ngos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.category}'     
# post = ngos(name=post['name'],description=post['description'],logo=post['logo'],phone=post['phone'],email=post['email'],category=post['category'],location=post['location'])
