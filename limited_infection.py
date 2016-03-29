"""
The limited_infection utilizes a modified breadth-first search to select who will be infected.
It allows for preferences of whether to favor parents or children. The selection of the number of users
to infect is not exact; if it is not possible to infect all children under a coach, it will not be done.
"""


from bfs import bfs


def limited_infection(graph, victim, new_version, preference, number_of_users):
    """
    :param graph: An array of all users in the system.
    :param victim: Who will be 'patient zero'. Must be a User.
    :param new_version: The new version to update users with.
    :param preference: Selection of the strings "child" and "parent" to choose which direction to favor.
    :param number_of_users: How many users we want to infect.
    """

    # If the input supplied is not indicative of a direction to traverse, we throw an error.
    if preference not in ["child", "parent"]:
        raise ValueError, "Invalid preference. Choose from 'parent' or 'child'."

    # The result of the disbursement of infections is supplied through the modified bfs function.
    result = bfs(victim, preference, number_of_users)

    # Because we used deepcopy to preserve the integrity of our data structure in bfs, we must update the users
    # supplied to us in the graph because those are the original users that we want to infect.
    for user in graph:
        for item in result:
            if item.get_username() == user.get_username() and user.get_version() != new_version:
                user.update_version(new_version)
        if user.get_version() == new_version:
            print user.get_username(), "has been infected."