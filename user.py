"""
The basic plan for this project is a data structure similar to a linked list;
it will have parents and children which can be on any number. A username will be user to
differentiate users and a version attribute will determine the version of Khan Academy
they will be seeing. Parents are equivalent to coaches and children are students of the coach.
The User object is very simple and comes equipped with appropriate getters and setters.
"""


class User(object):
    def __init__(self, username):
        """
        :param username: We are assuming we have some kind of buffer to prevent multiple instances of a username.
        """
        if type(username) is str:
            self.username = username
        else:
            raise TypeError, "Username must be a string."
        self.version = None
        self.parents = []
        self.children = []

    def update_version(self, new_version):
        self.version = new_version

    def update_username(self, new_username):
        if type(new_username) is str:
            self.username = new_username
        else:
            raise TypeError, "Username must be a string."

    def add_child(self, child):
        if type(child) is User:
            self.children.append(child)
        else:
            raise TypeError, "Input must be a User."

    def add_parent(self, parent):
        if type(parent) is User:
            self.parents.append(parent)
        else:
            raise TypeError, "Input must be a User."

    def remove_parent(self, parent):
        if type(parent) != User:
            raise TypeError, "Input must be a User."
        try:
            self.parents.remove(parent)
        except:
            raise ValueError, "Input is not linked with User."

    def remove_student(self, student):
        if type(student) != User:
            raise TypeError, "Input must be a User."
        try:
            self.children.remove(student)
        except:
            raise ValueError, "Input is not linked with User."

    def get_parents(self):
        return self.parents

    def get_children(self):
        return self.children

    def get_version(self):
        return self.version

    def get_username(self):
        return self.username

    def reset(self):
        self.version = None
        self.parents = []
        self.children = []


def coach(coach, student):
    """
    This function allows a coach to coach a student.
    """
    try:
        coach.add_child(student)
        student.add_parent(coach)
    except:
        raise TypeError, "Coach and Student must be Users."


def decoach(coach, student):
    """
    This function allows a coach to stop coaching a student.
    """
    try:
        coach.remove_student(student)
        student.remove_coach(coach)
    except:
        raise ValueError, "Coach and student are not linked."
