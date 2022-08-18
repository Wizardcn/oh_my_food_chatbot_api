from repositories.played_sound_repo import query_played_sound


def calculate_obtained_point(recorded_url, played_sound_id):
    result = query_played_sound(played_sound_id)
    if 200 in result:
        played_sound = result[200]
    else:
        return result
    max_point = played_sound["max_point"]
    return max_point