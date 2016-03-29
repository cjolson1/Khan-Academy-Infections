"""
This function is a modified version of breadth-first search. It starts with the victim's children/parents
and if the number of these individuals is less than or equal to the number of infections left to give out,
we add these users to a set of visited users. We continue to infect each level's users until the number of users in the
level that aren't infected if greater than the goal. In which case, we allocate the remaining infections such that
all children of a parent are infected. This is not always possible, and the program recognizes that. If multiple
solutions are possible, the program will only return one of the possible configurations for simplicity.
"""


from copy import deepcopy
from itertools import permutations
from random import choice


def bfs(victim, preference, goal):
    """
    :param victim: Who is 'patient zero'. Must be a User.
    :param preference: Selection of either "child" of "parent".
    :param goal: Similar to the number_of_users input for the limited_infection script.
    :return: A set of the Users that need to have their versions updated.
    """

    # Determine which direction to traverse the graph, to parents or children.
    goal -= 1
    if preference == 'child':
        people = victim.get_children()
    elif preference == "parent":
        people = victim.get_parents()
    else:
        raise ValueError, "Invalid preference. Choose from 'parent' or 'child'."

    # I used a dictionary to track parents/children at each level so I could select
    # the appropriate users when the while loop ended for more precise allocation of
    # infections.
    level = 1
    visited = set()
    visited.add(victim.get_username())
    turn_on = {level: [victim]}
    while True:
        if goal == 0 or len(people) == 0:
            break
        if len(people) <= goal:
            level += 1
            turn_on[level] = []
            valid = []
            for person in people:
                if person.get_username() not in visited:
                    valid.append(person)
                    goal -= 1
                    turn_on[level].append(person)
                    visited.add(person.get_username())
            temp = []
            for item in valid:
                if preference == 'child':
                    temp.extend([child for child in item.get_children() if child.get_username() not in visited])
                elif preference == "parent":
                    temp.extend([parent for parent in item.get_parents() if parent.get_username() not in visited])
                else:
                    raise ValueError, "Invalid preference. Choose from 'parent' or 'child'."
            people = deepcopy(temp)
        else:
            break

    # Now we determine which users we should update versions for.
    leftover = goal

    # The variable leftover = 0 iff there is an exact disbursement of infections throughout the levels.
    if leftover == 0:

        # If the disbursement of infections is exact, we create a set of the users and return it.
        selection = turn_on
        to_update = set()
        for level in selection.values():
            for item in level:
                to_update.add(item)
        return to_update

    # If the disbursement of infections has leftovers, we look through the previous level's users and
    # see if we can fill all their children/parents exactly.
    notable = turn_on[level]
    final = []
    found = False
    for parent in notable:
        temp = deepcopy(turn_on)
        if preference == 'child':
            item = parent.get_children()
        elif preference == "parent":
            item = parent.get_parents()
        else:
            raise ValueError, "Invalid preference. Choose from 'parent' or 'child'."
        unvisited = [i for i in item if i.get_username() not in visited]
        if len(unvisited) == leftover:
            found = True
            temp[level + 1] = []
            for i in unvisited:
                temp[level + 1].append(i)
            final.append(temp)
        else:
            final.append(temp)

    # If there are no previous level's users that have exactly the number of children/parents we are
    # looking for, we iterate through permutations of the previous level's users to find the best
    # allocation of infections.
    if not found:
        for perm in permutations(notable):
            for parent in perm:
                temp = deepcopy(turn_on)
                if preference == 'child':
                    item = parent.get_children()
                elif preference == "parent":
                    item = parent.get_parents()
                else:
                    raise ValueError, "Invalid preference. Choose from 'parent' or 'child'."
                unvisited = [i for i in item if i.get_username() not in visited]
                if len(unvisited) < leftover:
                    leftover -= len(unvisited)
                    temp[level+1] = []
                    for i in unvisited:
                        temp[level+1].append(i)
                    final.append(temp)
                else:
                    final.append(temp)

    # Filter for the final selection that has the most infections
    most_infections = []
    counts = []
    for i in final:
        count = 0
        for key in i.keys():
            count += len(i[key])
        counts.append(count)
    indices = [i for i, x in enumerate(counts) if x == max(counts)]
    for j in indices:
        most_infections.append(final[j])

    # If their are multiple options, we default to choosing a random one. We then format the return as a
    # set of the Users to be updated.
    selection = choice(most_infections)
    to_update = set()
    for level in selection.values():
        for item in level:
            to_update.add(item)
    return to_update
