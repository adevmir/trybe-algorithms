def study_schedule(permanence_period, target_time):
    result = 0
    for student in permanence_period:
        if type(target_time) != int\
            or type(student[0]) != int\
                or type(student[1]) != int:
            return None
        if target_time in range(student[0], student[1] + 1):
            result += 1
    return result
