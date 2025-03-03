from serializers.basic import *


class SubmitResponse(BaseModel):
    model_config = {'extra': 'ignore'}

    api_key: API_KEY
    response_id: ID
