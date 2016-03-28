"""
The basic idea behind the infect function is to infect the user in question and infect all
children and parents of the user that are not already infected.
"""


def infect(person, new_version):
    """
    :param person: Who is going to be infected. Type must be a User.
    :param new_version: The new version to give to those infected (can be any type).
    """

    # Update the victim's version.
    person.update_version(new_version)

    # Find all users connected to the victim that are not already infected.
    all = [child for child in person.get_children() if child.get_version() != new_version] + \
          [parent for parent in person.get_parents() if parent.get_version() != new_version]

    # Base case: If no one can be infected, end the infection process for the victim.
    if len(all) == 0:
        return

    # Infect all the uninfected people associated with the victim.
    for human in all:
        infect(human, new_version)