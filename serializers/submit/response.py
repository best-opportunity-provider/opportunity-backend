from serializers.basic import *


class SubmitResponse(BaseModel):
    model_config = {'extra': 'ignore'}

    response_id: ID
