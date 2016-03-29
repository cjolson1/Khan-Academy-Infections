"""
This file allows us to visualize infections of Users. It opens a new window with an interactive graph.
"""


import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def visualize(users, infect_version):
    """
    :param users: An array of all User objects in question.
    :param infect_version: The infection version to check for.
    """

    # We are creating a MultiDiGraph because we assume the coaches and students relationships are not bounded
    # by any rules. (e.g. Hypothetically a coach could coach a student and the student could coach the coach.)
    G = nx.MultiDiGraph()

    # Create the matplotlib object that will visualize our graph.
    fig = plt.figure()

    # Determine if a user has the infection or not and add these as nodes to the MultiDiGraph.
    infected = []
    not_infected = []
    for user in users:
        if user.get_version() == infect_version:
            infected.append(user)
        else:
            not_infected.append(user)
    G.add_nodes_from(infected + not_infected)

    # Label the users' nodes with their corresponding username.
    labels = {}
    for user in users:
        labels[user] = r'$%s$' % user.get_username()

    # Create appropriate directional edges from user to user with the direction of parent -> child.
    edges = []
    for user in users:
        for child in user.get_children():
            edges.append((user, child))

    # Position the nodes and edges in a shell layout.
    pos = nx.shell_layout(G)

    # Draw the infected nodes in the shell layout with a red coloring.
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=infected,
        node_shape='s',
        node_color='r',
        node_size=500,
        alpha=1.0
    )

    # Draw the uninfected nodes in the shell layout with a blue coloring.
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=not_infected,
        node_shape='s',
        node_color='b',
        node_size=500,
        alpha=1.0
    )

    # Draw all the edges linking the users together.
    nx.draw_networkx_edges(
        G, pos,
        width=1,
        edgelist=edges,
        alpha=0.8
    )

    # Label the nodes.
    nx.draw_networkx_labels(
        G, pos,
        labels,
        fontsize=10,
        alpha=1.0
    )

    # Create a legend for the figure.
    red_label = mpatches.Patch(
        color='red',
        label='Infected',
        alpha=1.0
    )

    blue_label = mpatches.Patch(
        color='blue',
        label='Not Infected',
        alpha=1.0
    )

    plt.legend(
        handles=[red_label, blue_label],
        bbox_to_anchor=(.8, .1),
        loc='upper left',
        ncol=1
    )

    # Remove the axes on our figure.
    frame = plt.gca()
    frame.axes.xaxis.set_visible(False)
    frame.axes.yaxis.set_visible(False)

    # Give the figure window and graph corresponding titles.
    f = plt.gcf()
    f.canvas.set_window_title('Infection Visualization')
    fig.suptitle("Infections of Users with Version %s" % infect_version, fontsize=15)

    # Graph the graph
    plt.show()