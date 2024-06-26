from django.db import models
from factory.exceptions import SpecificationCompletedException

class Specification(models.Model):
  name = models.CharField(max_length=100)
  code_number = models.CharField(max_length=20, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  is_completed = models.BooleanField(default=False)

  def is_fully_assigned(self):
    return all(component.part_code for group in self.groups.all() for component in group.components.all())

  def check_and_mark_completed(self):
    self.is_completed = self.is_fully_assigned()
    self.save()

  def save(self, *args, **kwargs):
    if self.pk and self.is_completed:
        raise SpecificationCompletedException()
    super(Specification, self).save(*args, **kwargs)
 
  def __str__(self):
    return f"{self.id} {self.name}"

class Group(models.Model):
  specification = models.ForeignKey(
    Specification, 
    related_name='groups', 
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  group_code = models.CharField(max_length=20)

  def save(self, *args, **kwargs):
    if self.specification.is_completed:
      raise SpecificationCompletedException(detail="Groups of a completed Specification cannot be modified.")
    super(Group, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.id} {self.name}"
  
class Component(models.Model):
  group = models.ForeignKey(
    Group, 
    related_name='components', 
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  description = models.TextField()
  part_code = models.CharField(max_length=20, blank=True, null=True)

  def save(self, *args, **kwargs):
    if self.group.specification.is_completed:
      raise SpecificationCompletedException("Components of a completed Specification cannot be modified.")
    super(Component, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.id} {self.name}"
