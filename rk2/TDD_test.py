import unittest
from rk2 import Group, Course, GroupCourse, query_b1, query_b2, query_b3

class TestQueries(unittest.TestCase):
    def setUp(self):
        # Cтуденческие группы
        self.groups = [
            Group(1, 'IU1-12A', 26),
            Group(2, 'IU1-11B', 28),
            Group(3, 'IU3-21C', 20),
            Group(4, 'IU4-42D', 24),
            Group(5, 'IU5-44B', 19),
        ]
        # Учебные курсы
        self.courses = [
            Course(1, 'First'),
            Course(2, 'Second'),
            Course(3, 'Third'),
            Course(4, 'Fourth'),
        ]
        # Студенческая группа - Учебный курс
        self.groups_courses = [
            GroupCourse(1, 1),
            GroupCourse(1, 2),
            GroupCourse(2, 3),
            GroupCourse(4, 4),
            GroupCourse(4, 5),
            GroupCourse(3, 5),
        ]

    def test_query_b1(self):
        result = query_b1(self.groups, self.courses)
        self.assertEqual(len(result), 5)

    def test_query_b2(self):
        result = query_b2(self.groups, self.courses)
        self.assertEqual(len(result), 4)

    def test_query_b3(self):
        result = query_b3(self.groups, self.courses, self.groups_courses)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()