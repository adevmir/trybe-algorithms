def study_schedule(permanence_period, target_time):
    try:
        if target_time == None:
            return None
        result = 0
        for student in permanence_period:
            if target_time in range(student[0], student[1] + 1):
                result += 1
        return result
    except TypeError:
        return None
