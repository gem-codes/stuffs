from rest_framework.exceptions import APIException

class SpecificationCompletedException(APIException):
  status_code = 400
  default_detail = "Completed Specification cannot be modified."
  default_code = 'specification_completed'

  def __init__(self, detail=None, code=None):
    self.detail = detail or self.default_detail
    self.code = code or self.default_code
    super().__init__(detail=self.detail, code=self.code)

