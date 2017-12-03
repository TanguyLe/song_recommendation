import math
def black_box_ml(songs_data, playlist):
    # Doing something
    #get_distance(songs_data, playlist[0], playlist[1])

    return "Suggestion: Baby - Justin Bieber"


def get_distance(songs_data, song_num_1, song_num_2):

    durations = songs_data['Duration'].tolist()
    key_sigs = songs_data['KeySignature'].tolist()
    key_sigs_conf = songs_data['KeySignatureValues'].tolist()
    tempos = songs_data['Tempo'].tolist()
    time_sigs = songs_data['TimeSignature'].tolist()
    time_sigs_conf = songs_data['TimeSignatureConfidence'].tolist()


    sum_durations = math.pow(durations[song_num_1-1] - durations[song_num_2-1], 2) +
                    math.pow(key_sigs[song_num_1-1] - key_sigs[song_num_2-1], 2) +
                    math.pow(key_sigs_conf[song_num_1-1] - key_sigs_conf[song_num_2-1], 2) +
                    math.pow(tempos[song_num_1-1] - tempos[song_num_2-1], 2) +
                    math.pow(time_sigs[song_num_1-1] - time_sigs[song_num_2-1], 2) +
                    math.pow(time_sigs_conf[song_num_1-1] - time_sigs_conf[song_num_2-1], 2)

    distance = math.sqrt(sum_durations)

    return distance
