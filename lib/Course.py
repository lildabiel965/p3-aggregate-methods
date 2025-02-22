from lib.enrollment import Enrollment


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []  

    def add_enrollment(self, enrollment):
        """Adds an enrollment to the course."""
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        """Returns a copy of the course's enrollments."""
        return self._enrollments.copy()
