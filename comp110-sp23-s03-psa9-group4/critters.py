"""
Module: critters

A Python implementation of Critters!

Authors:
1) Antonio Barcelos - abarcelos@sandiego.edu
2) Will Dobrzanski - wdobrzanski@sandiego.edu
"""

import random
from tkinter import *
from tkinter.font import Font
from enum import Enum


class Critter:
    """
    Representation of a critter in our world. This class will act as the
    parent/super class for all of the specific critter types we define.

    DO NOT MODIFY THIS CLASS IN ANY WAY!
    """

    def __init__(self, location):
        self.x = location[0]
        self.y = location[1]

    def __str__(self):
        """
        Returns a string representation of this critter.
        This representation is used when fighting another critter.
        """
        return "?"

    def get_move(self, neighbors):
        """ Gets the next move the critter wants to make. """
        return Direction.CENTER

    def fight(self, opponent):
        """ Gets the next fight move for the critter. """
        return Attack.FORFEIT

    def eat(self):
        """ Returns True if the critter wants to eat, False otherwise. """
        return False

    def get_color(self):
        """ Returns the color with which to display this critter. """
        return "black"

    def set_location(self, x, y):
        """ Changes the location of this Critter. """
        self.x = x
        self.y = y

    def set_world_dimensions(self, width, height):
        """ Sets the width and height of world that critter lives in. """
        self.world_width = width
        self.world_height = height



"""
To Do: Complete the Bear, Cheetah, Lion, and Torero classes below.

Note: remove the "pass" statement after you start implementing the constructor.
"""

class Bear(Critter):
    """ Bear patterns """

    def __init__(self, location, is_grizzly):
        self.is_grizzly = is_grizzly
        super().__init__(location)
        self.dirs = [Direction.NORTH , Direction.WEST]
        self.move_number = 0
        pass

    def __str__(self):
        """String value for bear is B"""
        return "B"

    def get_move(self, neighbors):
        """ ALterates between north and west in zigzag pattern"""
        i = self.move_number % 2
        self.move_number = self.move_number + 1
        return self.dirs[i]

    def fight(self, opponent):
        """ ALways scratches"""
        return Attack.SCRATCH

    def get_color(self):
        """ Gets bear color, brown if grizzly and snow if other"""
        if self.is_grizzly == True:
            return "brown"
        else:
            return "snow"

    def eat(self):
        """Always eats"""
        return True


class Cheetah(Critter):
    """ Cheetah Patterns"""
    
    def __init__(self, location, hunger_count):
        self.hunger = hunger_count

        super().__init__(location)
        self.dirs = [Direction.NORTH, Direction.SOUTH, Direction.EAST,
                Direction.WEST]
        self.move_number = 3
        self.first_move = random.choice(self.dirs)

    def __str__(self):
        """Labeled based on their hunger count"""
        return str(self.hunger)

    def get_move(self, neighbors):
        """ Moves 3 moves in a random direction then switches to another random direction for 3 more moves"""
        
        while self.move_number >= 0:
            if self.move_number == 0:
                self.first_move = random.choice(self.dirs)
                self.move_number = 3
            self.move_number = self.move_number - 1
            return self.first_move


    def fight(self, opponent):
        """ if it is hungry it scratches and if not hungry it pounces"""
        if self.hunger > 0:
            return Attack.SCRATCH
        else: 
            return Attack.POUNCE

    def get_color(self):
        """CHeetah color is red"""
        return "red"

    def eat(self):
        """ hunger level drops by 1 point each time it eats until zero"""
        if self.hunger > 0:
            self.hunger = self.hunger - 1
            return True
        else:
            return False


class Lion(Critter):
    """ Lion patterns """

    def __init__(self, location):
        self.hunger = False
        super().__init__(location)
        self.dirs = [Direction.SOUTH, Direction.WEST , Direction.NORTH , Direction.EAST]
        self.move_number = 0

    def __str__(self):
        """ Lion laabel is L"""
        return "L"

    def get_move(self, neighbors):
        """ moves in 5x5 square"""

        if self.move_number == 20:
            self.move_number = 0

        self.move_number = self.move_number + 1

        while self.move_number in range(6):
            return self.dirs[0]

        while self.move_number in range(6,11):
            return self.dirs[1]

        while self.move_number in range(11,16):
            return self.dirs[2]

        while self.move_number in range(16,21):
            return self.dirs[3]


    def fight(self, opponent):
        """ roar against bears and pounce at anything else"""

        if opponent == "B":
            self.hunger = TRUE
            return Attack.ROAR
            
        else:
            self.hunger = TRUE
            return Attack.POUNCE


    def get_color(self):
        """color is golden"""
        return "goldenrod3"

    def eat(self):
        """lion will eat after it gets in a fight"""

        if self.hunger == True:
            self.hunger = False
            return True

        else:
            return False




class Torero(Critter):
    """ torrero patterns """
    
    def __init__(self, location):
        super().__init__(location)
        self.dirs = [Direction.NORTH, Direction.SOUTH, Direction.EAST,
                Direction.WEST]
        
        self.move_number = 15

        self.circles = 10

        self.first_move = random.choice(self.dirs)

        self.circleMoves = random.choice(self.dirs)

    def __str__(self):
        """String value is T"""
        return "T"

    def get_move(self, neighbors):
        """Moves in random direction 15 spaces then in 1 random direction 10 times before repeating"""

        if self.move_number and self.circles == 0:
                
                self.first_move = random.choice(self.dirs)
                self.circleMoves = random.choice(self.dirs)
                self.move_number = 15
                self.circles = 10

        while self.move_number > 0:

            self.move_number = self.move_number - 1

            return self.first_move
         
        
         
        while self.move_number == 0:

            self.circleMoves = random.choice(self.dirs)

            self.circles = self.circles - 1

            return self.circleMoves
        

    def fight(self, opponent):
        """ counters other animal attacks"""

        num_list = []
        for num in range(1,1000):
            num_list.append(str(num))


        if opponent == "B":
            return Attack.ROAR
        elif opponent == "L":
            return Attack.SCRATCH
        elif opponent in num_list:
            return Attack.ROAR
        elif opponent == "0":
            return Attack.SCRATCH
        else:
            return random.choice([Attack.POUNCE , Attack.SCRATCH, Attack.ROAR])


    def get_color(self):
        """color is green"""
        return "dark sea green"

    def eat(self):
        """never eats"""
        return False












""" DO NOT MODIFY ANYTHING PAST THIS POINT!!!! """










class Direction(Enum):
    """ Enumeration for directions in the world. """
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    CENTER = 5

class Attack(Enum):
    """ Enumeration for possible Critter attacks. """
    ROAR = 1
    POUNCE = 2
    SCRATCH = 3
    FORFEIT = 4

FOOD_COMA_PERIOD = 2 # how many times critter can eat before falling asleep
FOOD_COMA_SLEEP_TIME = 20  # how long a critter sleeps after eating too much
GESTATION_PERIOD = 40 # how long the mating period is for critters
FOOD_RESPAWN_PERIOD = 50 # how often to spawn new food

after_id = None
root = None
world = None

turn_time_ms = 1000

turn_number = 0
turn_string = None

start_button = None
stop_button = None
tick_button = None
reset_button = None

bear_stats_string = None
cheetah_stats_string = None
lion_stats_string = None
torero_stats_string = None

class World:
    """
    Representation of a 2D grid world containing critters.
    """

    def __init__(self, width, height, window, food_probability):
        """
        Initializes our world to have the given dimensions, with each spot
        in the world having a food_probability chance of containing food.

        The world starts out without any critters: use the add_critter method
        to start populating the world.
        """
        self.width = width
        self.height = height
        self.food_probability = food_probability
        self.critter_grid = [[None] * width for _ in range(height)]
        self.critter_location = {}

        # each spot in the world will have food_probability chance of having food
        self.food_grid = [[False] * width for _ in range(height)]
        for x in range(width):
            for y in range(height):
                if random.random() < food_probability:
                    self.food_grid[y][x] = True


        self.sleep_time = {} # map critter to how many more turns to sleep
        self.gestate_time = {} # map critter to how many more turns of mating
        self.pregnant_critters = [] # list of pregnant critters
        self.amount_eaten = {} # map critter to how much they have eaten

        # map from critter type to amount that are alive
        self.num_alive = {"Bear": 0, "Lion": 0, "Cheetah": 0, "Torero": 0}

        # map from critter type to amount they've eaten
        self.num_eaten = {"Bear": 0, "Lion": 0, "Cheetah": 0, "Torero": 0}

        # map from critter type to amount of fights won
        self.num_wins = {"Bear": 0, "Lion": 0, "Cheetah": 0, "Torero": 0}

        # start with no critters and every spot in the world is open
        self.critters = []
        self.open_spots = [(x, y) for x in range(width)
                           for y in range(height)]

        # creates a GUI for us to draw our world on
        self.canvas = Canvas(window, bg="#d9ffcc", height=(14*height),
                             width=(14*width), bd=0, relief='sunken',
                             highlightthickness=0)
        self.canvas.pack()


    def clear(self):
        """
        Clears the world, resetting everything back to an initial state.

        DO NOT USE THIS RIGHT NOW, AS IT HAS NOT BEEN TESTED!
        """
        self.critter_grid = [[None] * self.width for _ in range(self.height)]

        self.food_grid = [[False] * self.width for _ in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                if random.random() < self.food_probability:
                    self.food_grid[y][x] = True

        self.sleep_time = {} # map critter to how many more turns to sleep
        self.gestate_time = {} # map critter to how many more turns of mating
        self.pregnant_critters = [] # list of pregnant critters
        self.amount_eaten = {} # map critter to how much they have eaten

        # start with no critters and every spot in the world is open
        self.critters = []
        self.open_spots = [(x, y) for x in range(self.width)
                           for y in range(self.height)]

    def get_stats(self, critter_type):
        """
        Returns a tuple of stats for the given critter type, e.g. "Bear".
        """
        return self.num_alive[critter_type], self.num_wins[critter_type], \
            self.num_eaten[critter_type]

    def get_open_spot(self):
        """ Returns a random open spot in the world. """
        location = random.choice(self.open_spots)
        self.open_spots.remove(location)
        return location

    def add_critter(self, critter, location):
        """ Places a new critter in the world at the given location. """
        self.critters.append(critter)
        self.critter_location[critter] = location
        self.critter_grid[location[1]][location[0]] = critter
        self.amount_eaten[critter] = 0
        self.num_alive[type(critter).__name__] += 1

    def food_at(self, x, y):
        """ Returns True if there is food at the given location, False
        otherwise. """
        x = x % self.width
        y = y % self.height
        return self.food_grid[y][x]

    def grow_food(self):
        """ Adds food to a random open spot in the world. """
        food_x, food_y = random.choice(self.open_spots)
        self.food_grid[food_y][food_x] = True

    def feed_critter(self, critter, x, y):
        """
        Feeds the given critter the food at the given location.

        Returns True if the critter fell asleep because of eating, False
        otherwise.
        """
        x = x % self.width
        y = y % self.height
        if not self.food_grid[y][x]:
            raise RuntimeError("Tried removing food where there was none.")
        else:
            self.num_eaten[type(critter).__name__] += 1
            self.food_grid[y][x] = False
            self.amount_eaten[critter] += 1

            if self.amount_eaten[critter] % FOOD_COMA_PERIOD == 0:
                self.sleep_time[critter] = FOOD_COMA_SLEEP_TIME
                return True
            else:
                return False

    def rest_critters(self):
        """
        Marks sleeping critters as having rested for an additional turn.
        If they have been sleeping long enough, the critter will be woken up.
        """
        for critter in list(self.sleep_time.keys()):
            if self.sleep_time[critter] == 0:
                del self.sleep_time[critter]
            else:
                self.sleep_time[critter] -= 1

    def mate_critters(self, mother, father):
        """
        Marks two critters as mating, setting one as the mother and the
        other as the father. The mother is the critter that spawn off the baby
        at the end of the gestation period.
        """
        self.pregnant_critters.append(mother)
        self.gestate_time[mother] = GESTATION_PERIOD
        self.gestate_time[father] = GESTATION_PERIOD

    def gestate_critters(self):
        """
        Marks mating critters as having gestated for an additional turn.

        If they have been gestating long enough, they a new baby critter will
        be formed.
        """
        for critter in list(self.gestate_time.keys()):
            if self.gestate_time[critter] == 0:
                del self.gestate_time[critter]

                # if this is the mother, a new baby critter will be added to
                # the world.
                if critter in self.pregnant_critters:
                    self.pregnant_critters.remove(critter)

                    # TODO: get closest open spot to this critter
                    baby_loc = self.get_open_spot()
                    baby = spawn_critter(type(critter).__name__, baby_loc,
                                         self)
                    self.add_critter(baby, baby_loc)

            else:
                self.gestate_time[critter] -= 1

    def get_critter(self, x, y):
        """ Returns the critter at the given location, or None if one isn't
        there. """
        x = x % self.width
        y = y % self.height
        return self.critter_grid[y][x]

    def move_critter(self, critter, new_x, new_y):
        """ Move the given critter to the given location. """
        new_x = new_x % self.width
        new_y = new_y % self.height

        curr_x, curr_y = self.critter_location[critter]
        self.open_spots.append((curr_x, curr_y))
        self.critter_grid[new_y][new_x] = critter
        self.critter_grid[curr_y][curr_x] = None
        self.critter_location[critter] = (new_x, new_y)
        critter.set_location(new_x, new_y)

    def remove_critter(self, critter):
        """ Remove this critter from the world, for its time has come. """
        curr_x, curr_y = self.critter_location[critter]
        self.open_spots.append((curr_x, curr_y))
        self.critter_grid[curr_y][curr_x] = None
        del self.critter_location[critter]

    def bury_critter(self, critter):
        """ Remove all traces of critter from the world. """
        self.num_alive[type(critter).__name__] -= 1

        world.critters.remove(critter)

        if critter in self.sleep_time:
            del self.sleep_time[critter]
        if critter in self.gestate_time:
            del self.gestate_time[critter]
        if critter in self.pregnant_critters:
            self.pregnant_critters.remove(critter)
        if critter in self.amount_eaten:
            del self.amount_eaten[critter]

    def is_sleeping(self, critter):
        """ Returns True if the critter is sleeping, False otherwise. """
        return critter in self.sleep_time

    def is_mating(self, critter):
        """ Returns True if the critter is mating, False otherwise. """
        return critter in self.gestate_time

    def get_location(self, critter):
        """ Returns the location of the critter in the world. """
        return self.critter_location[critter]

    def draw(self):
        """ Redraws the world on the canvas. """
        regular_font = Font(family="Arial", size=-14, weight="bold")
        small_font = Font(family="Arial", size=-7, weight="bold")
        self.canvas.delete(ALL)
        for y in range(self.height):
            for x in range(self.width):
                # draw food (if any) then critter (if any)
                if self.food_grid[y][x]:
                    self.canvas.create_text(14*x+8, 14*y+8, text=".",
                                            font=regular_font,
                                            fill="black")
                    self.canvas.create_text(14*x+7, 14*y+7, text=".",
                                            font=regular_font,
                                            fill="tomato2")

                val = self.critter_grid[y][x]
                if val is not None:
                    # create a shadow for easier viewing
                    self.canvas.create_text(14*x+8, 14*y+8, text=str(val),
                                            font=regular_font,
                                            fill="black")
                    self.canvas.create_text(14*x+7, 14*y+7, text=str(val),
                                            font=regular_font,
                                            fill=val.get_color())

                    # add embellishments to indicate sleeping or mating
                    if val in self.gestate_time:
                        self.canvas.create_text(14*x+7, 14*y+7,
                                                text="<3",
                                                font=small_font,
                                                fill="red")
                    elif val in self.sleep_time:
                        self.canvas.create_text(14*x+7, 14*y+7,
                                                text="zzz",
                                                font=small_font,
                                                fill="black")


def adjust_turn_time(scalar):
    """ Adjusts the amount of ms for each turn. """
    global turn_time_ms
    turn_time_ms = 1000 // int(scalar)


def create_window():
    """ Returns a new GUI window. """
    root = Tk()
    root.title("Critters Simulator")
    root.geometry("975x750")

    # make sure this pops in front of all other windows
    root.lift()
    root.attributes("-topmost", True)
    root.grid_propagate(0)

    # Set up the frame where the world canvase will go
    canvas_frame = Frame(root)
    canvas_frame.grid(row=0, column=0)

    # set up frame with controls and turn count (bottom part of window)
    controls = Frame(root)
    controls.grid(row=1, column=0)

    turn_speed_slider = Scale(controls, from_=1, to=30, label="Turn Speed",
                              showvalue=0, orient=HORIZONTAL,
                              command=adjust_turn_time)
    turn_speed_slider.set(10)
    turn_speed_slider.grid(row=0, column=0)

    global turn_string
    turn_string = StringVar()
    turn_string.set("Turn: 0")
    turn_label = Label(controls, textvariable=turn_string)
    turn_label.grid(row=0, column=1)

    global start_button
    start_button = Button(controls, text="Start", command=sim_loop)
    start_button.grid(row=0, column=2)
    global stop_button
    stop_button = Button(controls, text="Stop", state=DISABLED,
                         command=stop_sim_loop)
    stop_button.grid(row=0, column=3)

    global tick_button
    tick_button = Button(controls, text="Tick", command=do_turn)
    tick_button.grid(row=0, column=4)

    #reset_button = Button(controls, text="Reset", command=reset_simulation)
    #reset_button.grid(row=0, column=5)

    # set up the frame with simulation stats, to go on the right side of the
    # window
    stats = Frame(root, width=200)
    stats.grid(row=0, column=1, rowspan=2, padx=15, sticky=N)

    frame_text_color = "blue"
    l = LabelFrame(stats, fg=frame_text_color, text="Bear", width=100)
    l.pack(fill='x', expand=True)
    global bear_stats_string
    bear_stats_string = StringVar()
    bear_stats_string.set("Alive: \nKills: \nEaten: \nPoints: ")
    bear_stats = Label(l, textvariable=bear_stats_string, justify=LEFT)
    bear_stats.pack(fill='x', expand=True)

    l2 = LabelFrame(stats, fg=frame_text_color, text="Cheetah", width=100)
    l2.pack(fill='x', expand=True)
    global cheetah_stats_string
    cheetah_stats_string = StringVar()
    cheetah_stats_string.set("Alive: \nKills: \nEaten: \nPoints: ")
    cheetah_stats = Label(l2, textvariable=cheetah_stats_string, justify=LEFT)
    cheetah_stats.pack(fill='x', expand=True)

    l3 = LabelFrame(stats, fg=frame_text_color, text="Lion", width=100)
    l3.pack(fill='x', expand=True)
    global lion_stats_string
    lion_stats_string = StringVar()
    lion_stats_string.set("Alive: \nKills: \nEaten: \nPoints: ")
    lion_stats = Label(l3, textvariable=lion_stats_string, justify=LEFT)
    lion_stats.pack(fill='x', expand=True)

    l4 = LabelFrame(stats, fg=frame_text_color, text="Torero", width=100)
    l4.pack(fill='x', expand=True)
    global torero_stats_string
    torero_stats_string = StringVar()
    torero_stats_string.set("Alive: \nKills: \nEaten: \nPoints: ")
    torero_stats = Label(l4, textvariable=torero_stats_string, justify=LEFT)
    torero_stats.pack(fill='x', expand=True)

    return root, canvas_frame


def sim_loop():
    """
    Starts doing turns of the simulation, waiting turn_time_ms between each
    turn.
    """
    global root
    global after_id
    do_turn()
    after_id = root.after(turn_time_ms, sim_loop)
    start_button.config(state=DISABLED)
    tick_button.config(state=DISABLED)
    stop_button.config(state=NORMAL)

def stop_sim_loop():
    """ Stops the simulation from doing more turns. """
    global after_id
    if after_id:
        root.after_cancel(after_id)
        after_id = None

        # update buttons
        start_button.config(state=NORMAL)
        tick_button.config(state=NORMAL)
        stop_button.config(state=DISABLED)

def reset_simulation():
    """
    Resets the similator to a beginning state.
    DO NOT USE THIS FUNCTION!
    """
    global world
    global turn_number
    stop_sim_loop()
    num_critters = len(world.critters)
    world.clear()
    initialize_critters(num_critters)
    turn_number = 0
    world.draw()

def battle(critter1, critter2):
    """
    Performs a fight between two critters.

    Returns a tuple of (winner, loser).
    """

    c1_attack = critter1.fight(str(critter2))
    c2_attack = critter2.fight(str(critter1))

    if c1_attack == c2_attack:
        if random.random() < 0.5:
            return critter1, critter2
        else:
            return critter2, critter1
    elif c2_attack == Attack.FORFEIT \
    or c1_attack == Attack.ROAR and c2_attack == Attack.SCRATCH \
    or c1_attack == Attack.SCRATCH and c2_attack == Attack.POUNCE \
    or c1_attack == Attack.POUNCE and c2_attack == Attack.ROAR:
        return critter1, critter2
    else:
        return critter2, critter1

def do_turn():
    """ Performs a single turn of the simulation. """
    global world

    world.rest_critters()
    world.gestate_critters()

    # shuffle the critters to avoid first spawned critters always getting
    # first chance at moving
    random.shuffle(world.critters)

    dead_critters = []
    for critter in world.critters:
        if critter in dead_critters:
            continue
        elif world.is_sleeping(critter) or world.is_mating(critter):
            continue

        # check if there's food at the critter's location
        curr_x, curr_y = world.get_location(critter)
        if world.food_at(curr_x, curr_y):
            # if critter wants to eat, feed it
            if critter.eat():
                fell_asleep = world.feed_critter(critter, curr_x, curr_y)
                if fell_asleep:
                    continue

        # Determine who this critter's neighbors are so we can give this
        # information to them when they are going to decide how to move.
        neighbors = {}

        north_neighbor = world.get_critter(curr_x, curr_y-1)
        if north_neighbor is not None:
            north_neighbor = str(north_neighbor)
        neighbors[Direction.NORTH] = north_neighbor

        east_neighbor = world.get_critter(curr_x+1, curr_y)
        if east_neighbor is not None:
            east_neighbor = str(east_neighbor)
        neighbors[Direction.EAST] = east_neighbor

        south_neighbor = world.get_critter(curr_x, curr_y+1)
        if south_neighbor is not None:
            south_neighbor = str(south_neighbor)
        neighbors[Direction.SOUTH] = south_neighbor

        west_neighbor = world.get_critter(curr_x-1, curr_y)
        if west_neighbor is not None:
            west_neighbor = str(west_neighbor)
        neighbors[Direction.WEST] = west_neighbor


        move = critter.get_move(neighbors)

        if move == Direction.NORTH:
            dest_x, dest_y = curr_x, curr_y-1
        elif move == Direction.EAST:
            dest_x, dest_y = curr_x+1, curr_y
        elif move == Direction.SOUTH:
            dest_x, dest_y = curr_x, curr_y+1
        elif move == Direction.WEST:
            dest_x, dest_y = curr_x-1, curr_y
        else:
            # Critter didn't want to move so nothing left to do
            continue

        other_critter = world.get_critter(dest_x, dest_y)
        if other_critter == None:
            world.move_critter(critter, dest_x, dest_y)
        else:
            if type(critter) != type(other_critter):
                # battle if they are different critter types
                if not world.is_sleeping(other_critter):
                    winner, loser = battle(critter, other_critter)
                else:
                    # if other critter was sleeping, they automatically lose
                    winner, loser = critter, other_critter

                # FIXME: make this a world method
                world.num_wins[type(winner).__name__] += 1

                dead_critters.append(loser)
                world.remove_critter(loser)

            else:
                # there is another critter of the same type here.
                if not world.is_mating(other_critter):
                    world.mate_critters(critter, other_critter)
                continue

    for critter in dead_critters:
        world.bury_critter(critter)

    global turn_number
    turn_number += 1
    turn_string.set("Turn: " + str(turn_number))

    # check if we need to grow food now
    if turn_number % FOOD_RESPAWN_PERIOD == 0:
        world.grow_food()

    # update stats in right side of window
    global bear_stats_string
    alive, kills, eaten = world.get_stats("Bear")
    total_points = alive + kills + eaten
    bear_stats_string.set("Alive: %d\nKills: %d\nEaten: %d\nPoints: %d" %
                          (alive, kills, eaten, total_points))

    global cheetah_stats_string
    alive, kills, eaten = world.get_stats("Cheetah")
    total_points = alive + kills + eaten
    cheetah_stats_string.set("Alive: %d\nKills: %d\nEaten: %d\nPoints: %d" %
                             (alive, kills, eaten, total_points))

    global lion_stats_string
    alive, kills, eaten = world.get_stats("Lion")
    total_points = alive + kills + eaten
    lion_stats_string.set("Alive: %d\nKills: %d\nEaten: %d\nPoints: %d" %
                          (alive, kills, eaten, total_points))

    global torero_stats_string
    alive, kills, eaten = world.get_stats("Torero")
    total_points = alive + kills + eaten
    torero_stats_string.set("Alive: %d\nKills: %d\nEaten: %d\nPoints: %d" %
                            (alive, kills, eaten, total_points))

    world.draw()

def spawn_critter(critter_name, location, world):
    if critter_name == "Bear":
        is_a_grizzly = random.choice([True, False])
        critter = Bear(location, is_a_grizzly)
    elif critter_name == "Lion":
        critter = Lion(location)
    elif critter_name == "Cheetah":
        hunger_level = random.randrange(10)
        critter = Cheetah(location, hunger_level)
    elif critter_name == "Torero":
        critter = Torero(location)

    critter.set_world_dimensions(world.width, world.height)
    return critter

def initialize_critters(num_each_type):
    """ Create and randomly place critters. """
    for i in range(num_each_type * 4):
        critter_loc = world.get_open_spot()
        if i%4 == 0:
            critter_name = "Bear"
        elif i%4 == 1:
            critter_name = "Cheetah"
        elif i%4 == 2:
            critter_name = "Lion"
        else:
            critter_name = "Torero"

        critter = spawn_critter(critter_name, critter_loc, world)
        world.add_critter(critter, critter_loc)


def simulate(world_width, world_height, num_each_type):
    """
    Perform simulation of a world with num_each_type of 4 different types
    of critters.
    """
    global root
    root, canvas_frame = create_window()

    global world
    world = World(world_width, world_height, canvas_frame, 0.05)

    initialize_critters(num_each_type)

    world.draw()
    root.mainloop()

if __name__ == "__main__":
    simulate(60, 50, 25)
    