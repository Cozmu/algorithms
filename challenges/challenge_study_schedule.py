def study_schedule(permanence_period, target_time):
    student_accountant = 0
    if not target_time or type(permanence_period) != list:
        return None
    for time_one, time_two in permanence_period:
        if not isinstance(time_one, int) or not isinstance(time_two, int):
            return None
        if time_one[0] <= target_time <= time_two[1]:
            student_accountant += 1

    return student_accountant
