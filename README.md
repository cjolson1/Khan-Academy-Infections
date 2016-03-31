# **Khan Academy Infections Project**



## **Introduction**

This Infections Project is written in and for Python 2.7.

This project allows users to experiment with infections; when rolling out big new features, we like to enable them slowly, starting with just the KA team, then a handful of users, then some more users, and so on, until we’ve ramped up to 100%. This insulates the majority of users from bad bugs that crop up early in the life of a feature.

Enter "infections". We can use the heuristic that each teacher-student pair should be on the same version of the site. So if A coaches B and we want to give A a new feature, then B should also get the new feature. Note that infections are transitive - if B coaches C, then C should get the new feature as well. Also, infections are transferred by both the “coaches” and “is coached by” relations. Ideally, when infecting a coach's students, we would like to infect all of them. If that is not possible, we do not infect them.

Throughout this project, I made several assumptions:
 - There could be loops in coaching (e.g. I coach you and you coach me).
 - There is a mechanism to filter out multiple occurences of a username.
 - If it is not possible to fill an entire user's coaches/students, it cannot and should not be done.
 

To accomplish these infections, we have two functions at our disposal, `total_infection` and `limited_infection`. Both of them use `User` objects and update these users' versions in order to infect them. Furthermore, supplied in this project is the `visualize` function which allows us to create a visualization of the relations between users and the infection's spread.


### **`User`**


The `User` object has four attributes, `parents`, `children`, `version`, and `username`. The `parents` and `children` attributes are arrays that hold other `User` objects that correspond to the user's coaches and students, respectively. The `version` is an attribute of any primitive type and corresonds to the version of the website the `User` is seeing. The `username` is the only input required when creating a `User`, and must be a `String`. We assume that we have a mechanism in place to prevent multiple occurences of a `username` to occur. That being said, in order to link one `User` to another, we must either `coach` or `decoach` them with another `User`.

There are a variety of getters and setters for the `User`, and they are as follows:
 - `update_version(new_version)`
 - `update_username(new_username)`
 - `add_child(child)`
 - `add_parent(parent)`
 - `remove_parent(parent)`
 - `remove_student(student)`
 - `get_parents()`
 - `get_children()`
 - `get_version()`
 - `get_username()`
 - `reset()`

Furthermore, I have created two methods to simplify the coach and uncoaching process.

##### **`coach`**


The `coach` method takes two `User` inputs, the `coach` and the `student`, and facilitates the `coach` coaching the `student`.

##### **`decoach`**


The `decoach` method takes two `User` inputs, the `coach` and the `student`, and facilitates the removal of the coach-student relationship between the two.


The `User`, along with the `coach` and `decoach` functionality provide a framework for us to create a userbase and link them.


### **`total_infection`**


This function takes three inputs: a `graph`, a `victim`, and a `new_version`. The `graph` is simply an array of all the users that are on the platform. The `victim` parameter must be a `User`, and will effectively be the 'patient zero' for the infections that will take place. The `new_version` can be of any type; it simply corresponds to a version of the website that will be seen by the users infected. 

The functionality of `total_infection` is simple. It infects all the coaches and students of the `victim` and repeats the process recursively for any individual connected directly or indirectly to the `victim`. After completing this process, it prints out which users have been infected.


### **`limited_infection`**


The `limited_infection` function takes five inputs, and is much more complex than the aforementioned `total_infection`. It's purpose is to solve the problem of the lack of control around how many users get infected. In order to accomplish this task, `limited_infection` provides several parameters that allow for customization tailored to our needs.

One parameter is the `graph`, which is simply an array of all the users in question. We need this input to update the versions of the users that become infected. Similar to `total_infection` is the `victim`, which is and `new_version` parameters, which are the 'patient zero' for the infection and is a `User` and version of the website the `User` will be seeing, respectively. There are several parameters, however, which we have not seen before.

One key aspect of `limited_infection` is the idea of `preference`; it allows for us give direction to our infection and drive it from patient zero's coaches or students. The `preference`s we can choose from are the Strings `"child"` or `"parent"`, which tells the program to explore patient zero's children or parents, respectively. The final parameter is the `number_of_users`, which is an integer input that gives the program the upper bound on the number of users it can infect.

The functionality of `limited_infection` follows the direction given by the `preference`. It attempts to iteratively infect all the users in the specified direction, and if it can, will try to infect all the newly-infected users' users in the specified direction, etc. until it reaches a point where the number of users queued to be infected would put the number of infected users over the upper-bound given by `number_of_users`. In which case, the program iteratively seeks to fill the remaining infections exactly amongst the users' relevant people, and if it cannot, it will not. After completing this process, it prints out which users have been infected.


### **`visualize`**


The `visualize` function returns a graph detailing the infection's spread throughout a userbase. It's two parameters, `users` and `infect_version` are an array of `User` objects, that represent all the users of the platform, and theh version the function will check the users for. The graph has directional arrows pointing from parents to children (coaches to students) and colors the infected users red and the uninfected users blue. Furthermore, it labels each node on the graph with the corresponding `username` and includes a legend.


## Usage


Using the Infection Project requires first initializing the users that are on the platform, and infecting them in the desired way with a unique version. If desired, we can visualize the infections by running `visualize` and checking for the unique version we infected the users with.

In order to convey the usage of the Infection Project, I will walk you through a simple example of its usage.

Begin by importing all the aforementioned methods which can be accessed simply through the line:

```
from infections import *
```

The first step in any infection is to create the users. Since we only need to initialize users with their usernames we can create `User` objects quite simply. Be sure to not name users the same name. After initializing all the users, it is convienient to collect them all into an array for future use.

```
user1 = User('User 1')
user2 = User('User 2')
user3 = User('User 3')
users = [user1, user2, user3]
```

In order to link the users together, we can utilize the `coach` functionality:

```
coach(user1, user2)
coach(user1, user3)
```

This allows `user1` to coach `user2` and `user3`. 

If we wanted to run a `total_infection` on these users starting from `user1` with the `new_version` being 1, we would simply call the following command:

```
total_infection(users, user1, 1)
```

This console would print the following statements:

```
User 1 has been infected.
User 2 has been infected.
User 3 has been infected.
```

If we want to take this infection procedure a step further, we could visualize the infection by calling the following command immediately following the `total_infection` call:

```
visualize(users, 1)
```

This command would return the following graph:

![alt tag](https://github.com/cjolson1/Khan-Academy-Infections/blob/master/total_infection_visualization.png)

Instead, if we wanted to run a `limited_infection` on 2 users starting from `user1` in the `"child"` direction with the `new_version` being 1, we would call the following command:

```
limited_infection(users, user1, 1, "child", 2)
```

which would yield the following statements in the console:

```
User 1 has been infected.
```

If we want to visualize the `limited_infection`, we can by calling the following command immediately following the `limited_infection` call:

```
visualize(users, 1)
```

This command would return the following graph:

![alt tag](https://github.com/cjolson1/Khan-Academy-Infections/blob/master/limited_infection_visualization.png)

Notice how only one `User` was infected despite the input being two because it is impossible to distribute the infections evenly among the children of `user1`.

These methods are simple and scalable and can be used in increasingly complex fashions, feel free to experiment with them after downloading the files!
