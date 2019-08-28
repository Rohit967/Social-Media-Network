#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Eight employees at a small company were asked to choose 3 movies that 
#they would most enjoy watching for the upcoming company movie night. 
#These choices are stored in the file `Employee_Movie_Choices.txt`.
#
#A second file, `Employee_Relationships.txt`, has data on the relationships between different coworkers. 
#
#The relationship score has value of `-100` (Enemies) to `+100` (Best Friends). 
#A value of zero means the two employees haven't interacted or are indifferent.
#
# Both files are tab delimited
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# This is the set of employees
employees = set(['Pablo',
                 'Lee',
                 'Georgia',
                 'Vincent',
                 'Andy',
                 'Frida',
                 'Joan',
                 'Claude'])


# This is the set of movies
movies = set(['The Shawshank Redemption',
              'Forrest Gump',
              'The Matrix',
              'Anaconda',
              'The Social Network',
              'The Godfather',
              'Monty Python and the Holy Grail',
              'Snakes on a Plane',
              'Kung Fu Panda',
              'The Dark Knight',
              'Mean Girls'])


# you can use the following function to plot graphs
def plot_graph(G, weight_name):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    
    import matplotlib.pyplot as plt
    
    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    #weights = weight_name
    
    if weight_name:
        #weights = [int(G[u][v][weight_name]) for u,v in edges]
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G,weight_name)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=5);
    else:
        nx.draw_networkx(G, pos, edges=edges);


'''
# =============================================================================
# 
# Using NetworkX, load in the bipartite graph from Employee_Movie_Choices.txt and return that graph.
# 
# This function should return a networkx graph with 19 nodes and 24 edges
# =============================================================================
'''

def movie_choices_graph():
        
    #1. your code here
    movie_choices = nx.read_edgelist('Employee_Movie_Choices.txt', delimiter="\t")
    
    return movie_choices #2. your code here

#Please call plot_graph to draw your movie_choices_graph, set the weight_name to None
    
#3. your code here
plot_graph(movie_choices_graph(), weight_name = None)

'''
# =============================================================================
# 
# Using NetworkX, load in the weighted graph from Employee_Relationships.txt and return that graph.
# 
# This function should return a networkx weighted graph
# =============================================================================
'''

def employee_relation_graph():
    employee_relation = nx.read_edgelist('Employee_Relationships.txt', nodetype=str, data=(['weight', int],))
    plot_graph(employee_relation, weight_name = 'weight')
    
    #1. Your code here
    return employee_relation#2. Your code here

#Please call plot_graph to draw your employee_relation_graph, you need to set the weight_name here
    
#3. Your code here
plot_graph(employee_relation_graph(), weight_name=None)


'''
# =============================================================================
# 
# Using the graph from the question one, add nodes attributes named 'type' where movies have the value 'movie' 
# and employees have the value 'employee' and return that graph.
# 
# This function should return a networkx graph with node attributes {'type': 'movie'} or {'type': 'employee'}
# =============================================================================
'''


employee_movie_choices = pd.read_csv('Employee_Movie_Choices.txt', sep="\t")
employee_movie_choices.head()

movie_choices_add_nodes = nx.from_pandas_edgelist(employee_movie_choices, '#Employee', 'Movie')
movie_choices_add_nodes.edges()

for employee in employees:
    nx.set_node_attributes(movie_choices_add_nodes, {employee: {'type':'employee'}})
for movie in movies:
    nx.set_node_attributes(movie_choices_add_nodes, {movie: {'type':'movie'}})

nx.get_node_attributes(movie_choices_add_nodes, 'type')



'''
# =============================================================================
# 
# 
# Find a weighted projection of the graph from question three which tells us how many movies different pairs of 
# employees have in common.
# 
# This function should return a weighted projected graph.
# =============================================================================
'''

G = bipartite.weighted_projected_graph(movie_choices_add_nodes, employees)

plt.figure(figsize=(12, 6))
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

