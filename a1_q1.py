import math


def a1_q1(temperature, degree):
    try:
        raise TypeError('bad type')
    except Exception as e:
        e.add_note('Add some information')
        raise
    # answer = (temperature - 32) * 5 / 9  # F to C
    answer =  temperature * 9 / 5 + 32  # C to F
    return answer
