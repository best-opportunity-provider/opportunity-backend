from fastapi.responses import JSONResponse

from ..base import app

import serializers.models as ser
import database


@app.post('/submit')
async def submit(response: ser.submit.SubmitResponse) -> JSONResponse:
    form_response = database.OpportunityFormResponse.objects(id=response.response_id)
    # TODO: check for API key
    if not form_response:
        return JSONResponse({'err': 'response_id is invalid'}, status_code=400)
    form_response = form_response[0]
