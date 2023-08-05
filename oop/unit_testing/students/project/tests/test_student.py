from unittest import TestCase, main
from project.student import Student


class StudentTest(TestCase):
    def setUp(self):
        name = "Jojo"
        courses = None
        self.student = Student(name, courses)

    def test_init(self):
        self.assertEqual(self.student.name, "Jojo")
        self.assertEqual(self.student.courses, {})

    def test_init_with_params(self):
        name = "Jojo"
        courses = {"Math": ["Statistics", "Combinatorics", "Hypothesis"]}
        student = Student(name, courses)
        self.assertEqual(student.name, "Jojo")
        self.assertEqual(student.courses, {"Math": ["Statistics", "Combinatorics", "Hypothesis"]})

    def test_enroll_existing_course(self):
        self.student.courses = {"Math": []}
        result = self.student.enroll("Math", ["Statistics", "Combinatorics", "Hypothesis"])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(expected, result)

    def test_enroll_existing_course_with_notes(self):
        self.student.courses = {"Math": ["Algebra"]}
        result = self.student.enroll("Math", ["Statistics", "Combinatorics", "Hypothesis", "Algebra"])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(expected, result)

    def test_update_notes_via_enroll_with_add_notes_no_param(self):
        self.student.courses = {"Math": []}
        result = self.student.enroll("Math", ["Statistics", "Combinatorics", "Hypothesis"])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(expected, result)

    def test_update_notes_via_enrol_with_add_notes_with_param(self):
        self.student.courses = {"Math": []}
        result = self.student.enroll("Math", ["Statistics", "Combinatorics", "Hypothesis"], "math")
        expected = "Course already added. Notes have been updated."
        self.assertEqual(expected, result)

    def test_update_notes_via_enrol_with_add_notes_param_set_empty(self):
        result = self.student.enroll("Math", ["Statistics", "Combinatorics", "Hypothesis"], "")
        expected = "Course and course notes have been added."
        self.assertEqual(expected, result)

    def test_update_notes_via_enrol_with_add_notes_param_set_y(self):
        result = self.student.enroll("Math", ["Statistics", "Combinatorics", "Hypothesis"], "Y")
        expected = "Course and course notes have been added."
        self.assertEqual(expected, result)

    def test_enroll_new_course_when_different_flag(self):
        result = self.student.enroll("Math", ["Statistics", "Combinatorics", "Hypothesis"], "No")
        expected = "Course has been added."
        self.assertEqual([], self.student.courses["Math"])
        self.assertEqual(expected, result)

    def test_add_notes_existing_course(self):
        self.student.courses = {"Math": []}
        result = self.student.add_notes("Math", ["Statistics", "Combinatorics", "Hypothesis"])
        expected = "Notes have been updated"
        self.assertEqual(expected, result)

    def test_add_notes_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Math", ["Statistics", "Combinatorics", "Hypothesis"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_enrolled_course(self):
        self.student.courses = {"Math": []}
        result = self.student.leave_course("Math")
        expected = "Course has been removed"
        self.assertEqual(expected, result)

    def test_leave_non_enrolled_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
