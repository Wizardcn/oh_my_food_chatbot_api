from fastapi import APIRouter, status, HTTPException
from controller.played_sound_controller import update_count
from controller.user_controller import add_history, update_user_point
from models.error_model import DatabaseError, PlayedSoundNotFoundError
from models.sound_model import RecordedSound, RecordedSoundRequestBody
from repositories.recorded_sound_repo import create_recorded_sound

recorded_sound_router = APIRouter(tags=["recorded_sounds"])

@recorded_sound_router.post("/", status_code=status.HTTP_201_CREATED,
                            responses={
                                201: {
                                    "model": RecordedSound,
                                    "description": "Recorded Sound Was Created"
                                },
                                404: {
                                 "model": PlayedSoundNotFoundError,
                                 "description": "Played Sound Not Found Error"
                                }
                                ,
                                520: {
                                    'model': DatabaseError,
                                    'description': 'Database Connection Error'
                                }
                            }
                            
                            )
async def add_recorded_sound(recorded_sound_request_body: RecordedSoundRequestBody):
    
    update_count_result = update_count(recorded_sound_request_body)
    if 200 not in update_count_result:
        error_key = list(update_count_result.keys())[0]
        raise HTTPException(status_code=error_key, detail=update_count_result[error_key])
        
    result = create_recorded_sound(recorded_sound_request_body)
    if 201 in result:
        recorded_sound = result[201]
        
        # error cases: cannot find user from uid, 
        add_history(recorded_sound)
        update_user_point(recorded_sound)
        return recorded_sound
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])
