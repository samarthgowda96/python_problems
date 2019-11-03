# [Assignment #2: Save the World!](http://publish.uwo.ca/~rmoir3/asn2.html)

Starting point: [A2.py](A2.py)
Marking scheme: [A2_MarkingScheme.txt](A2_MarkingScheme.txt)
Code check script: [A2_check.py](A2_check.py)

Our first assignment dealt with _data analysis_. We’re going to do a lot more of that, but it’s important to get some exposure to another very important area of modern science: computational _simulation_. If you can simulate something accurately enough, the simulation might have real advantages over actually doing an experiment.

For example, if you simulate a protein folding – and get it right – you can actually stop, rewind, replay, and even do matrix-style ‘bullet time’ pans around the protein, as it folds. This allows you to watch interactions on a level of detail that is completely impossible experimentally. ([Check out Vijay Pande talking about Folding@Home](https://www.youtube.com/watch?v=Pjt1Q2ZZVjA))

Simulations also let you do things you simply _can’t_ do in reality. Suppose you’re a social geographer who wants to study the social impact of different types of natural disasters on a small fishing village. You’d have difficulty getting ethics approval to flood an actual village, or bury it in lava, and then collect data. If, however, your ‘villagers’ exist only in a simulation…there are no constraints on what you can do.

For this assignment, you will be doing a simple __military simulation__. Imagine it is discovered that secretly the Nazis won World War II, and control the world through a network of control of cities and institutions. Then suppose you are part of a force mobilizing to take back control of these cities using highly ethical, e.g., constitutional and non-violent, means, but you need to plan your operation carefully to maximize your likelihood of success. This is where the simulation comes in.

Your task, then, is to write code to simulate the retaking of the world by regaining control of a network of North American cities. Once your simulation is working, you’ll write a bit more code to analyze the data produced by your simulation to determine exciting things like how long it will take to save the world.

## How to approach the assignment
Once again, you are asked to extend existing code. Extending existing code can actually be more challenging than writing code from scratch but, as a scientist or other researcher using programming as tool, this is what 90% of your real-world programming will be.

For the first assignment, you just had to get the code working. For this assignment, it also has to *look pretty*… by which I mean:

- There should be comments in the code Functions should have headers

- explaining what they do in plain English

If you’re not sure how those things should look, use the existing code as a guideline.

Speaking of the existing code… The first thing you should do is [download the existing code](A2.py) and take a quick look at it. Just skim it. Some of the provided functions call on rather complex Python libraries and may look very confusing to you. That’s totally normal. What you really want to look at are the descriptions in the function headers. Right after the `def` line, you’ll see some text wrapped between triple quotes. Read this carefully. This tells you everything you need to know about how to use that function—without you having to understand how all the details of the function work. That is: you can work _one level of abstraction higher_ than the function.

So…look at that code. Seriously. Do it. Familiarizing yourself with what’s going on in the file is the best possible preparation for doing the assignment.

## Data structures you need to know about
Every city in our simulation is going to be represented by a list `[name,regained,neighbours]`

`name` is a string with the name of the city.

`regained` is a `bool`: `True` if the city has been regained; `False` if it lost to the enemy.

`neighbours` is a _list_ (so we’ve nested a list inside a list!) containing the city numbers of the cities that are directly connected by the enemy control network.

Our _world_ is made up of multiple cities. How can we store all these cities? In another list, of course! So the world is a list of lists:

```python3
world = [city1, city2, city3, ...]
```

## Getting started
To make your life easier, I’ve provided a function called `set_up_cities` that will generate some cities, with a randomly generated enemy control network between them, for you. If you call this function, it returns a _list_ of cities, detailing the state of your simulated world. You’d use the function like this:

```python3
my_world = set_up_cities()
```

> ### Note:
> If you don’t want to stick to the default names for the cities, note that there is an optional `name` parameter for this function. This lets you pass in your own list of city names if you want to (this also allows you to create a world with fewer, or more, cities). For the last part of the assignment, however, you will need to use a particular list of city names accessed by the function `get_read_world()` (not actually the real world).

You should probably load up `A2.py` in your interpreter right now and play around with the `set_up_cities()` function just to get a feel for it. Have a look at the lists it generates and make sure you understand their structure.