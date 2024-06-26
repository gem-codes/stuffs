from rest_framework.exceptions import APIException

class SpecificationCompletedException(APIException):
  status_code = 400
  default_detail = "Completed Specification cannot be modified."
  default_code = 'specification_completed'
