from serializers.basic import *
from enum import IntEnum
from typing import Union

from .opportunity_partial import *
from .localization import *


class OpportunityCreateResponse(BaseModel):
    model_config = {'extra': 'forbid'}

    main_data: OpportunityMainInfo
    details_data: OpportunityDetailsInfo
    selection_data: OpportunitySelectionInfo
    geo_data: OpportunityGeoInfo
    tags_data: OpportunityTagsInfo
    form_data: OpportunityFormInfo


class OpportunityUpdateResponse(BaseModel):
    model_config = {'extra': 'forbid'}

    opportunity_id: ID

    main_data: OpportunityMainInfo
    details_data: OpportunityDetailsInfo
    selection_data: OpportunitySelectionInfo
    geo_data: OpportunityGeoInfo
    tags_data: OpportunityTagsInfo
    form_data: OpportunityFormInfo
