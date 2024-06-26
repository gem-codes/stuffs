from rest_framework import viewsets
from .models import Specification, Group, Component
from .serializers import SpecificationSerializer, GroupSerializer, ComponentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class SpecificationViewSet(viewsets.ModelViewSet):
  queryset = Specification.objects.all()
  serializer_class = SpecificationSerializer

  @action(detail=True, methods=['PUT', 'PATCH'])
  def mark_specification_as_completed(self, request, pk=None):
    specification = self.get_object()
    specification.check_and_mark_completed()
    if specification.is_completed:
      return Response({
        'message': 'Specification marked as completed'
        })
    else:
      return Response({
        'message': 'Specification cannot be marked as completed'}, 
        status=400
        )


class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer


class ComponentViewSet(viewsets.ModelViewSet):
  queryset = Component.objects.all()
  serializer_class = ComponentSerializer

  @action(detail=True, methods=['PATCH'])
  def assign_part(self, request, pk=None):
    component = self.get_object()
    part_code = request.data.get('part_code')

    if part_code is not None:
      component.part_code = part_code
      component.save()

      return Response({'message': 'Part assigned successfully.'})
    else:
      return Response({'error': 'Part code must be provided.'}, status=400)
