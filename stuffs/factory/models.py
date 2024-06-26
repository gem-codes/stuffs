from django.db import models

class Specification(models.Model):
  name = models.CharField(max_length=100)
  code_number = models.CharField(max_length=20, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  is_completed = models.BooleanField(default=False)

  def __str__(self):
    return f"#{self.name}"

class Group(models.Model):
  specification = models.ForeignKey(
    Specification, 
    related_name='groups', 
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  group_code = models.CharField(max_length=20)

  def __str__(self):
    return f"#{self.name}"
  
class Component(models.Model):
  group = models.ForeignKey(
    Group, 
    related_name='components', 
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  description = models.TextField()
  part_code = models.CharField(max_length=20, blank=True, null=True)

  def __str__(self):
    return self.name