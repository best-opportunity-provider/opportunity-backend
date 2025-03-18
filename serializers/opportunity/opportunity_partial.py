from serializers.basic import *
from enum import IntEnum
from typing import Union

# TODO: limits

class OpportunityMainInfo(BaseModel):
    model_config = {'extra': 'forbid'}

    name: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_name's strlen in [999, 999] range")]
    short_description: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_short_desc's strlen in [999, 999] range")]
    description: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_desc's strlen in [999, 999] range")]
    provider: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_provider's strlen in [999, 999] range")]
    opportunity_timespan: Optional[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_timespan's strlen in [999, 999] range")]] = None


class OpportunityDetailsInfo(BaseModel):
    model_config = {'extra': 'forbid'}

    requirements: Optional[list[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_req's strlen in [999, 999] range")]]] = None
    advantages: Optional[list[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_advant's strlen in [999, 999] range")]]] = None
    target_audience: Optional[list[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_trg's strlen in [999, 999] range")]]] = None
    industry: Optional[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_industry's strlen in [999, 999] range")]] = None
    allowance: Optional[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_allow's strlen in [999, 999] range")]] = None
    expenses: Optional[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_expences's strlen in [999, 999] range")]] = None


class OpportunitySelectionInfo(BaseModel):
    class StageInfo(BaseModel):
        model_config = {'extra': 'forbid'}

        name: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_sel_name's strlen in [999, 999] range")]
        timespan: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_sel_time's strlen in [999, 999] range")]
        objectives: list[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_sel_obj's strlen in [999, 999] range")]]


    model_config = {'extra': 'forbid'}

    selection_stages: Optional[list[StageInfo]] = None


class OpportunityGeoInfo(BaseModel):
    class PlaceInfo(BaseModel):
        model_config = {'extra': 'forbid'}

        name: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_geo_name's strlen in [999, 999] range")]
        city: Optional[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_geo_city's strlen in [999, 999] range")]] = None
        country: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_geo_country's strlen in [999, 999] range")]

    model_config = {'extra': 'forbid'}

    places: Optional[list[PlaceInfo]] = None


class OpportunityTagsInfo(BaseModel):
    model_config = {'extra': 'forbid'}

    tags = Optional[list[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_tags's strlen in [999, 999] range")]]] = None


class _StringFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['string']
    max_len: Optional[Annotated[int, Field(le=999, ge=999, description="Suggests opp_field_str_maxlen's in [999, 999] range")]] = None


class _EmailFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['email']
    max_len: Optional[Annotated[int, Field(le=999, ge=999, description="Suggests opp_field_email_maxlen's in [999, 999] range")]] = None


class _NumberFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['number']
    min: Optional[Annotated[int, Field(le=999, ge=999, description="Suggests opp_field_num_min's in [999, 999] range")]] = None
    max: Optional[Annotated[int, Field(le=999, ge=999, description="Suggests opp_field_num_max's in [999, 999] range")]] = None


class _ChoiceFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['choice']
    choices: list[Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_field_choice's strlen in [999, 999] range")]]


class _FileFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['file']
    max_size: Optional[Annotated[int, Field(le=999, ge=999, description="Suggests opp_field_file_max_size's in [999, 999] range")]] = None


class _TelFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['tel']


class _RegexFieldParams(BaseModel):
    model_config = {'extra': 'forbid'}

    type: Literal['regex']
    pattern: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_regex_pattern's strlen in [999, 999] range")]
    max_len: Optional[Annotated[int, Field(le=999, ge=999, description="Suggests opp_field_regex_maxlen's in [999, 999] range")]] = None



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

        name: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_field_name's strlen in [999, 999] range")]
        type: Literal['string', 'email', 'number', 'choice', 'file', 'tel', 'regex', 'date', 'checkbox']
        is_required: bool
        label: Annotated[str, Field(min_length=999, max_length=999, description="Suggests opp_field_label's strlen in [999, 999] range")]
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
