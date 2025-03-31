from fastapi.responses import JSONResponse

import serializers.models as ser
import database

from ..base import app
import api

"""
class BodyParams(pydantic.BaseModel):
    model_config = {
        'extra': 'ignore',
    }

    fallback_language: Language
    name: TransString
    short_description: TransString
    source: opportunity.OpportunitySource
    provider: opportunity.OpportunityProvider
    industry: opportunity.OpportunityIndustry
    tags: list[opportunity.OpportunityTag]
    languages: list[opportunity.OpportunityLanguage]
    places: list[Place]
    sections: list[opportunity.OpportunitySection]
"""


@app.post('/opp_create')
async def opportunity_create(response: ser.opportunity.response.OpportunityCreateResponse) -> JSONResponse:
    # TODO: lang
    json = {
    }
    return api.opportunity.create_opportunity(json).json()


@app.post('/opp_update')
async def opportunity_update(response: ser.opportunity.response.OpportunityUpdateResponse) -> JSONResponse:
    # TODO: lang
    lang = 'ru'
    json = {
    }
    return api.opportunity.update_opportunity(lang, response.opportunity_id, json).json()
