def study_schedule(permanence_period, target_time):
    result = 0
    for student in permanence_period:
        if type(target_time) != int\
            or type(student[0]) != int\
                or type(student[1]) != int:
            return None
        if student[0] <= target_time <= student[1]:
            result += 1
    return result
