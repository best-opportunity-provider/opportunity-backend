from fastapi.responses import JSONResponse

import serializers.models as ser
import database

from ..base import app


@app.post('/opp_update')
async def opportunity_update(response: ser.opportunity.response.OpportunityUpdateResponse) -> JSONResponse:
    pass


"""
    form_response = database.OpportunityFormResponse.objects(id=response.response_id)
    if not form_response:
        return JSONResponse({'err': 'response_id is invalid'}, status_code=400)
    form_response = form_response[0]
    fill_submit_form(form_response.form, form_response.data.to_python())
    # TODO: checkout for user
"""
