"""
The total_infection has an input for who is the 'patient zero' and an input for the new version the
people will be seeing. It recursively infects all parents and children of the 'patient zero' and
continues the same process for each parent/child.
"""


from infect import infect


def total_infection(victim, new_version):
    """
    :param victim: Who will be infected first. Type must be a User.
    :param new_version: The new version to give to those infected (can be any type).
    """

    # Update the victim's version.
    victim.update_version(new_version)
    children = victim.get_children()
    parents = victim.get_parents()
    all = children + parents

    # Infect all the people linked to the victim.
    for person in all:
        infect(person, 1)
