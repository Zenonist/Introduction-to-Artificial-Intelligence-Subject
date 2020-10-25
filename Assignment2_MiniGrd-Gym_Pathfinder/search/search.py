"""Version 1.2"""
# * Phonarnun Tatiyamaneekul 6188062 Sec 2
from typing import Tuple, List
from copy import deepcopy
import time

from gym_minigrid.minigrid import MiniGridEnv
import numpy as np
import math #import math to use sqrt for eculidean distance
from search import graph as G



def heuristic(state: G.MiniGridState) -> float:
    # TODO: 1
    image = state.obs['image'][:, :, 0]
    direction = state.obs['direction']
    #Initialize the variable to store position of agent and goal
    agentx = -1;
    agenty = -1;
    goalx = -1;
    goaly = -1;
    for x in range(0,image.shape[0]): # loop to find position of agent and goal
        for y in range(0,image.shape[1]):
            if (image[x][y] == 10):
                agentx = x;
                agenty = y;
            if (image[x][y] == 8):
                goalx = x;
                goaly = y;
    #Formula = |x1 - x2| + |y1 - y2| -> Manhattan Distance
    #Formula = sqrt((x2-x1)^2 + (y2-y1)^2) -> Eculidean Distance
    #result = abs(agentx - goalx) + abs(agenty - goaly);
    result = math.sqrt(pow(goalx - agentx,2)+pow(goaly - agenty,2));
    return 0


def search(
        init_state: G.MiniGridState,
        frontier: G.DataStructure) -> Tuple[List[int], int]:
    # TODO: 2
    # * I comment after the code because my vs code doesn't show change the color of comment to grey if i comment on the new line
    root = G.SearchTreeNode(init_state, None, -1,  0)
    frontier.add(root, heuristic(root.state)) 
    num_explored_nodes = 0
    explored_set = [] # initialize the explored set to be empty
    pathlists = [] # initialize the path to store nodes
    plan = [] # Store the action that agent should do
    finished = False # Use to break the while loop
    while (not finished):
        if frontier.is_empty(): #if the frontier is empty then return failure
            finished = True # return failure [Error]
        else:
            Leaf_node = frontier.remove() # Choose a leaf node by removing it from the frontier
            #print(Leaf_node.state.obs['image'][:, :, 0]) #uncomment to check the process of searching
            if Leaf_node.state.is_goal(): # if the node contains a goal state
                pathlists = Leaf_node.get_path() #return the path [solution]
                for node in pathlists: # loop for each node in pathlists
                    if node.action > -1 and node.action < 4: # we want only 0,1,2 which is left,right,forward [We don't want action of root node <the action of root node = -1>]
                        plan.append(node.action) # add action to the plan that agent will act [agent will follow this list to reach the goal]
            else:
                num_explored_nodes = num_explored_nodes + 1 # increase the value every time that we explored new node
                explored_set.append(Leaf_node.state) #I try to append only Leaf_node but it can't check that node is already in list 
                for x in range(3): # loop for [0,1,2 - > left,right,forward]
                    Tempnode = Leaf_node.state.successor(x) # get the state from each action [the result of action that agent will do]
                    Extended_Node = G.SearchTreeNode(Tempnode,Leaf_node,x,0) # Create new node from state
                    if not (frontier.is_in(Tempnode)) and not (Extended_Node.state in explored_set): # add the resulting nodes to the frontier if it is not in the frontier or explored_set [It help to avoid duplicated states]
                        frontier.add(Extended_Node, heuristic(Extended_Node.state)) # add new node [heuristic is not used in this code <I tried do it with heuristic but i causes a huge bug in my code>]
    
    return plan, num_explored_nodes


def execute(init_state: G.MiniGridState, plan: List[int], delay=0.5) -> float:
    env = deepcopy(init_state.env)
    env.render()
    sum_reward = 0
    for i, action in enumerate(plan):
        print(f'action no: {i} = {action}')
        time.sleep(delay)
        _obs, reward, done, _info = env.step(action)
        sum_reward += reward
        env.render()
        if done:
            break
    env.close()
    return sum_reward
