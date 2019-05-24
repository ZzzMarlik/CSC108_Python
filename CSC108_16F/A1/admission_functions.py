SPECIAL_CASE_SCHOOL_1 = 'Fort McMurray Composite High'
SPECIAL_CASE_SCHOOL_2 = 'Father Mercredi High School'
SPECIAL_CASE_YEAR = '2016'

# Add other constants here
NO_EXAM = 'NE'

def is_special_case(record):
    """ (str) -> bool

    Return True iff the student represented by record is a special case.

    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    True
    >>> is_special_case('Jacqueline Smith,Father Something High School,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    """

    # Complete the body of the function here
    return (((SPECIAL_CASE_SCHOOL_1 in record) or
             (SPECIAL_CASE_SCHOOL_2 in record)) and
            (SPECIAL_CASE_YEAR in record))

# Complete the rest of the functions here

def get_final_mark(record, coursework_mark, exam_mark):
    """ (str, str, str) -> float

    Return the final mark of a particular course that students get
    by coursework_mark and exam_mark in their record.

    Pre-condition: 10 <= course_mark < 100 and 10 <= final_mark < 100

    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts', '90', '94')
    92.0
    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,NE,ENG,92,88,CHM,80,85,BArts', '90', 'NE')
    90.0
    >>> get_final_mark('Jacqueline Smith,Father Something High School,2016,MAT,90,NE,ENG,92,88,CHM,80,85,BArts', '90', 'NE')
    45.0
    >>> get_final_mark('Eyal de Lara,Fort McMurray Composite High,2016,MAT,90,92,ENG,92,NE,BIO,77,85,BSci', '90', '92')
    91.0
    """

    if (NO_EXAM in exam_mark) and (is_special_case(record)):
        return float(coursework_mark)
    elif (NO_EXAM in exam_mark):
        return float(coursework_mark) / 2
    else:
        return ((float(coursework_mark) + float(exam_mark)) / 2)

def get_both_marks(course_record, course_code):
    """ (str, str) -> str

    Return the course_mark and the exam_mark by matching the course_code with
    the course_record.

    Pre-condition: 10 <= course_mark <= 99 and 10 <= final_mark <= 99

    >>> get_both_marks('ABC,10,20', 'ABC')
    '90 94'
    >>> get_both_marks('ENG,92,NE', 'ENG')
    '92 NE'
    >>> get_both_marks('CHM,85,86', 'ABC')
    ''
    """
    if course_code in course_record:
        return course_record[4:6] + ' ' + course_record[7:9]
    else:
        return ''

def extract_course(transcript, course_num):
    """ (str, int) -> str

    Return the name and marks of one course from transcript of students by
    course_num

    Pre-condition: course_num >= 1

    >>> extract_course('MAT,90,94,ENG,92,NE,CHM,80,85', 1)
    'MAT,90,94'
    >>> extract_course('MAT,90,94,ENG,92,NE,CHM,80,NE', 3)
    'CHM,80,NE'
    """
    return transcript[(course_num - 1) * 10:(9 + (course_num - 1) * 10)]

def applied_to_degree(student_record, degree):
    """ (str, str) -> bool

    Return True iff and only if the degree in the student_record is matching
    the degree.

    >>> applied_to_degree('Jacqueline Smith,Some High School,2016,MAT,90,94,ENG,92,NE,CHM,80,85,BArts', 'BArts')
    True
    >>> applied_to_degree('Jacqueline Smith,Some High School,2016,MAT,90,94,ENG,92,NE,CHM,80,85,BArts', 'BSci')
    False
    >>> applied_to_degree('King Arthur,Some High School,2016,MAT,90,94,ENG,92,NE,CHM,80,85,BSci', 'BArts')
    False
    """

    return student_record[-len(degree):] == degree

def decide_admission(student_avg, cutoff):
    """ (number, number) -> str

    Return the result of admission by comparing student_avg and the cutoff

    >>> decide_admission(90, 80)
    'accept with scholarship'
    >>> decide_admission(92, 90)
    'accept'
    >>> decide_admission(83, 85)
    'reject'
    """

    if student_avg >= cutoff + 5:
        return 'accept with scholarship'
    elif student_avg >= cutoff:
        return 'accept'
    else:
        return 'reject'
