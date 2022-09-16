from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Name = {self.name} | City = {self.city} | State = {self.state} | Description = {self.desc}>'

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return f'<Title = {self.first_name} | Dojo = {self.dojo_id}>'