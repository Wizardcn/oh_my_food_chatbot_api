from fastapi import APIRouter, status, HTTPException
from models.error_model import DatabaseError, PlayedSoundNotFoundError
from models.sound_model import PlayedSound, ShowPlayedSounds
from repositories.played_sound_repo import query_played_sound, query_played_sounds

played_sound_router = APIRouter(tags=["played_sounds"])

@played_sound_router.get("/", 
                         responses={
                             200: {
                                 "model": ShowPlayedSounds
                             },
                             404: {
                                 "model": PlayedSoundNotFoundError,
                                 "description": "Played Sound Not Found Error"
                             },
                             520: {
                                'model': DatabaseError,
                                'description': 'Database Connection Error'
                             }
                         })
async def get_played_sounds():
    
    result = query_played_sounds()
    if 200 in result:
        return result[200]
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])
    

    
@played_sound_router.get("/{played_sound_id}", 
                         responses={
                             200: {
                                 "model": PlayedSound
                             },
                             404: {
                                 "model": PlayedSoundNotFoundError,
                                 "description": "Played Sound Not Found Error"
                             },
                             520: {
                                'model': DatabaseError,
                                'description': 'Database Connection Error'
                             }
                         })
async def get_played_sound(played_sound_id: str):
    
    """
    ### played_sound_id
    - **played_sound_id** is in **YXXXXX** format
    - **Y** is mood type of played sound
        - **H**: Happy
        - **S**: Sad
        - **F**: Fearful
        - **A**: Angry
        - **E**: Excited
        - *T: Test*
    - **XXXXX** is order of sound like 00001 or 00032
    """
    
    result = query_played_sound(played_sound_id)
    if 200 in result:
        return result[200]
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])