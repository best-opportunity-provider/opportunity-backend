from serializers.basic import *
from enum import IntEnum
from typing import Union

class OpportunityMainInfo(BaseModel):
    model_config = {'extra': 'forbid'}

    name: str
    short_description: str
    description: str
    provider: str
    source_type: int
    source_link: str
    opportunity_timespan: Optional[str] = None


class OpportunityDetailsInfo(BaseModel):
    model_config = {'extra': 'forbid'}

    requirements: Optional[list[str]] = None
    advantages: Optional[list[str]] = None
    target_audience: Optional[list[str]] = None
    industry: Optional[str] = None
    allowance: Optional[str] = None
    expenses: Optional[str] = None


class OpportunitySelectionInfo(BaseModel):
    class StageInfo(BaseModel):
        model_config = {'extra': 'forbid'}

        name: str
        timespan: str
        objectives: list[str]


    model_config = {'extra': 'forbid'}

    selection_stages: Optional[list[StageInfo]] = None


class OpportunityGeoInfo(BaseModel):
    class PlaceInfo(BaseModel):
        model_config = {'extra': 'forbid'}

        name: str
        city: Optional[str] = None
        country: str

    model_config = {'extra': 'forbid'}

    places: Optional[list[PlaceInfo]] = None


class OpportunityTagsInfo(BaseModel):
    model_config = {'extra': 'forbid'}

    tags: Optional[list[str]] = None


class _StringFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['string']
    max_len: Optional[int] = None


class _EmailFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['email']
    max_len: Optional[int] = None


class _NumberFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['number']
    min: Optional[int] = None
    max: Optional[int] = None


class _ChoiceFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['choice']
    choices: list[str]


class _FileFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['file']
    max_size: Optional[int] = None


class _TelFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['tel']


class _RegexFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['regex']
    pattern: str
    max_len: Optional[str] = None


class _DateFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['date']


class _CheckboxFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['checkbox']
    checked_by_default: bool


# V1
class OpportunityFormInfo(BaseModel):
    class FieldInfo(BaseModel):
        model_config = {'extra': 'forbid'}

        name: str
        is_required: bool
        label: str
        parameters: Annotated[Union[
            _StringFieldParams,
            _EmailFieldParams,
            _NumberFieldParams,
            _ChoiceFieldParams,
            _FileFieldParams,
            _TelFieldParams, 
            _RegexFieldParams,
            _DateFieldParams,
            _CheckboxFieldParams
        ], Field(discriminator='type')]

    model_config = {'extra': 'forbid'}
    form: Optional[list[FieldInfo]] = None
