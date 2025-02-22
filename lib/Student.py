from datetime import datetime

from lib.enrollment import Course, Enrollment

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  

    def enroll(self, course):
        """Enrolls the student in a course."""
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        """Returns a copy of the student's enrollments."""
        return self._enrollments.copy()
    
