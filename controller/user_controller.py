from models.sound_model import RecordedSound
from repositories.user_repo import query_user, update_user



def add_history(recorded_sound: RecordedSound):
    
    uid = dict(recorded_sound)["uid"]
    recorded_id= dict(recorded_sound)["recorded_id"]
    played_sound_id = dict(recorded_sound)["played_sound_id"]
    
    result = query_user(uid)
    if 200 in result:
        user = result[200]
        user["record_history"][recorded_id] = played_sound_id
        return update_user(uid, user)
    else:
        return result
    
    
def update_user_point(recorded_sound: RecordedSound):
    uid = dict(recorded_sound)["uid"]
    obtained_point = dict(recorded_sound)["obtained_point"]
    
    result = query_user(uid)
    if 200 in result:
        user = result[200]
        user["total_point"] += obtained_point
        return update_user(uid, user)
    else:
        return result
    