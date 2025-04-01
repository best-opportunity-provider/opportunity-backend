from fastapi.responses import JSONResponse

import serializers.models as ser
import database

from ..base import app
import api


def make_opportunity_json(lang: str, data: Union[
    ser.opportunity.response.OpportunityCreateResponse,
    ser.opportunity.response.OpportunityUpdateResponse]
    ) -> dict:
    json = {
        'fallback_language': lang,
        # Main data
        'name': data.main_data.name,
        'short_description': data.main_data.short_description,
        'source': {'type': data.main_data.source_type, 'link': data.main_data.source_link},  # TODO
        'provider': {'name': data.main_data.provider},  # TODO: logo
        # Details
        'industry': {'name': data.details_data.industry},
        # Tags
        'tags': [{'name': tag} for tag in (data.tags_data.tags if data.tags_data.tags else [])],
        # Languages TODO
        'languages': ['en'],
        # Geo
        'places': [{'name': geo.name, 'country': geo.country, 'city': geo.city} for geo in (data.geo_data.places if data.geo_data.places else [])],
        # Selection
        'sections': [{
            'description': data.main_data.description,
            'opportunity_timespan': data.main_data.description,
            'requirements': data.details_data.requirements,
            'advantages': data.details_data.advantages,
            'target_audience': data.details_data.target_audience,
            'allowance': data.details_data.allowance,
            'expenses': data.details_data.expenses,
            'selection_stages': [stage.json() for stage in (data.selection_data.selection_stages if data.selection_data.selection_stages else [])]
        }]  # TODO: fix
    }
    return json


def make_opportunity_form_json(opp_id: int, lang: str, data: ser.opportunity.opportunity_partial.OpportunityFormInfo):
    pass


@app.post('/opp_create')
async def opportunity_create(response: ser.opportunity.response.OpportunityCreateResponse) -> JSONResponse:
    json = make_opportunity_json(response)  # TODO: lang
    result = api.opportunity.create_opportunity(json).json()
    if 'id' not in result:
        return result
    # Load form
    # json = make_opportunity_form_json(result['id'], 'en', response.form_data)


@app.post('/opp_update')
async def opportunity_update(response: ser.opportunity.response.OpportunityUpdateResponse) -> JSONResponse:
    lang = 'en'  # TODO: lang
    json = make_opportunity_json(response)
    return api.opportunity.update_opportunity(lang, response.opportunity_id, json).json()
