---
title: "Title"
author: "Daniel Khastou"
date: "9-14-26"
---

# Faraday cage simulation

## Background

### Motivation

This project was done in the winter of 2026 at the request of a friend currently working at a startup. The startup was planning on flying drones close to powerlines and needed to know how the electric and magnetic fields would affect the circuitry. The plan was to build a faraday cage around the circuitry, and he wanted a simulation to test out the viability of the faraday cage.

He sent me a CAD model of the faraday cage, and I went through the steps of meshing it using gmsh and integrating it with ElmerGrid and ElmerSolver to produce a simulation

### End Result

By the time I was halfway through, I had made good progress, but was informed that the general direction the startup was taking was going to be different and that simulations like the one I was doing wouldn't be needed. The technical difficulties of flying these drones near intense electric and magnetic fields was too high, and the friend who I was in correspondance with told me that the calculations he did led him to the conclusion that it was basically impossible to get feasibly working. 

As a result, I did not end up simulating anything too complicated, at least for now, and focused on simple a simple electrostatics simulation. The simulation is succesful and shows the near lack of any electric field inside the cage.

### Images

#### 1. 

![transparent_result](images/transparent.png)

This shows the boundary surrounding the main Faraday cage, with a voltage gradient across it. The Faraday cage simply sits inside the boundary 

#### 2. 
![clipped_result](images/clip.png)

Here it is easy to see that the electric field outside the Faraday cage is non zero, while the electric field inside is either zero or significantly small. The apparent nonuniformity of the electric field due to non-uniform coloring is assumed to be due to the Faraday cage itself. This simulation was ran without the Faraday cage at all and the color map for the electric field in these cases was uniform in color. These results may be posted at a later date to provide clarity into this



## How to navigate this project

1. The notes.md contains all notes I wrote for myself in the process of learning the project workflow and all of the tools required, such as Elmer, gmsh, and more. This notes file is primarily for myself and is most likely not useful for someone else looking at the file, except that it documents my learning process in both Linux and the other tools as mentioned above.
2. I wrote some python scripts to try and automate storing the simulation results in a .db file using SQL. To my current memory, much of this is unfinished. The .db file is stored in the results, and the python scripts are stored in their own file. More updates will come
3. The results folder contains a .vtu file which can be opened up in ParaView, and the project also contains a folder with some .pvsm files which can be opened in ParaView to quickly view the end result visuals that are shown above
4. There is an output.log file, which is used primarily for troubleshooting