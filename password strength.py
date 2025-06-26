from zxcvbn import zxcvbn

def analyze_password_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']

    return {
        'score': score,
        'crack_time': result['crack_times_display']['offline_slow_hashing_1e4_per_second'],
        'feedback': feedback
    }
