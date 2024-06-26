from rest_framework import serializers
from .models import Specification, Group, Component

class ComponentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Component
    fields = ['id', 'name', 'description', 'part_code', 'group']


class GroupSerializer(serializers.ModelSerializer):
  components = ComponentSerializer(many=True, read_only=True)

  class Meta:
    model = Group
    fields = ['id', 'name', 'group_code', 'specification', 'components']


class SpecificationSerializer(serializers.ModelSerializer):
  groups = GroupSerializer(many=True, read_only=True)

  class Meta:
    model = Specification
    fields = ['id', 'name', 'code_number', 'created_at', 'is_completed', 'groups']
