from serializers.basic import *
from enum import IntEnum
from typing import Union


class OpportunityUpdateResponse(BaseModel):
    model_config = {'extra': 'forbid'}

    opportunity_id: Union[None, ID]

    main_data: dict
    details_data: dict
    selection_data: dict
    geo_data: dict
    tags_data: dict
    form_data: dict
