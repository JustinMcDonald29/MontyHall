import random as r
import copy

"""
Needed a break during a Stat 263 study session so I made this 

A program that simulates the Monty Hall Problem in a generalized way

Might later build a separate player class to more easily allow users to program their own playstyles
"""


class Door:
    """
    This is a class that represents a door in the Monty Hall Problem
    ...
    Attributes
    ----------
    prize : bool
        Shows whether this door instance has a prize behind it

    Methods
    -------
    prizeDoor(self)
        Set this door as having a prize behind it
    getPrize(self)
        Returns a copy of the prize attribute
    """

    def __init__(self):
        self.prize = False

    def prizeDoor(self):
        self.prize = True

    def getPrize(self):
        rval = copy.copy(self.prize)
        return rval


def game(playstyle, numDoors):
    """

    :param playstyle: int
        Either 0 or 1 (currently) representing the two basic playstyles for the monty hall problem.
        0 will always stay with their pick and 1 will always switch
    :param numDoors: int
        The number of doors for this given problem
    :return: bool
        Returns the 'result' variable which shows whether the player won the game
    """

    doorList = []  # Create an empty list
    for i in range(0, numDoors):  # Fill the empty list with numDoors amount of Door objects
        door = Door()
        doorList.append(door)
    doorNum = r.randint(0, numDoors - 1)  # Randomly select which door has the prize behind it

    doorList[doorNum].prizeDoor()  # Assign the prizeDoor

    firstPick = r.randint(0,
                          numDoors - 1)  # This variable represents the original door selected at random by the player

    if firstPick != doorNum:  # If the player didn't pick the prize door first assign closedDoor to the prize door index

        closedDoor = doorNum

    else:  # If the player did pick the prize door select a random door to remain closed

        closedDoor = firstPick
        while doorNum == firstPick and closedDoor == firstPick:
            closedDoor = r.randint(0, numDoors - 1)

    if playstyle == 0:  # If the player is playstyle 0 check the prize attribute of the door they first picked

        result = doorList[firstPick].getPrize()

    else:  # If the player is playstyle 1 check the prize status of the closed door (the door they didn't pick first)

        result = doorList[closedDoor].getPrize()

    return result


def monty(plays, playstyle, numDoors):
    """

    :param plays: int
        How many times the simulation will run
    :param playstyle: int 0 or 1
        Whether the player stays or switches, to be passed onto the game function
    :param numDoors: int
        How many doors in problem, passed to the game function
    :return: List(int)
        record[0] represents how many wins the player had and record[1] represents losses
    """
    wins = 0
    losses = 0
    record = []
    for i in range(0, plays):
        if game(playstyle, numDoors):
            wins += 1
        else:
            losses += 1
    record.append(wins)
    record.append(losses)
    return record


def play(plays, doorNum):
    recStrings = []

    player0record = monty(plays, 0, doorNum)
    p0win = (player0record[0] / plays) * 100
    p0String = "The record of the player who stays is " + str(player0record[0]) + " wins and " + str(
        player0record[1]) + " losses for a winning percentage of " + "{:.2f}".format(p0win) + "%"

    player1record = monty(plays, 1, doorNum)
    p1win = (player1record[0] / plays) * 100
    p1String = "The record of the player who switches is " + str(player1record[0]) + " wins and " + str(
        player1record[1]) + " losses for a winning percentage of " + "{:.2f}".format(p1win) + "%"

    recStrings.append(p0String)
    recStrings.append(p1String)

    return recStrings


def main():

    print("")
    print("Welcome to the Monty Hall Simulator, please only enter integers in the following fields")

    again = True
    while again != "n":
        print("")
        plays = int(input("How many times would you like to run the simulation?: "))
        doorNum = int(input("How many doors would you like to simulate?: "))
        recStrings = play(plays, doorNum)

        print("------------------------------------------------------------------------------------")
        print(recStrings[0])
        print("------------------------------------------------------------------------------------")
        print(recStrings[1],"\n")

        again = str(input(
            "If you would like to simulate again press any button, "
            "if you would like to stop the simulation press 'n': ")).lower()


main()
