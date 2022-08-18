
from models.sound_model import RecordedSoundRequestBody
from repositories.played_sound_repo import query_played_sound, update_played_sound

def update_count(recorded_sound_request_body: RecordedSoundRequestBody):
    
    played_sound_id = dict(recorded_sound_request_body)["played_sound_id"]
    
    result = query_played_sound(played_sound_id)
    if 200 in result:
        played_sound = result[200]
        played_sound["count"] += 1
        return update_played_sound(played_sound_id, played_sound)
    else:
        return result