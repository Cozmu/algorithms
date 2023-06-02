def study_schedule(permanence_period, target_time):
    student_accountant = 0
    if not target_time or type(permanence_period) != list:
        return None
    for student in permanence_period:
        if student[0] <= target_time <= student[1]:
            student_accountant += 1

    return student_accountant

