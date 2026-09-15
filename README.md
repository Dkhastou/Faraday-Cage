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

By the time I was halfway through, I had made good progress, but was informed that the general direction the startup was taking was going to be different and that simulations like the one I was doing wouldn't be needed. The technical difficulties of flying these drones near intense electric and magnetic fields was too high, and my engineer friend who I was in correspondance with told me that the math he did led him to the conclusion that it was basically impossible to get feasibly working. 

As a result, I did not end up simulating anything too complicated (that will come later), and focused on simple a simple electrostatics simulation. The simulation is succesful and shows the near lack of any electric field inside the cage.

## How to navigate this project

1. The notes.md contains all notes I wrote for myself in the process of learning the project workflow and all of the tools required, such as Elmer, gmsh, and more. This notes file is primarily for myself and is most likely not useful for someone else looking at the file, except that it documents my learning process in both Linux and the other tools as mentioned above.
2. I wrote some python scripts to try and automate storing the simulation results in a .db file using SQL. To my current memory, much of this is unfinished. The .db file is stored in the results, and the python scripts are stored in their own file. More updates will come
3. The results folder contains a .vtu file which can be opened up in paraview, and the project also contains a folder with some .pvsm files which can be opened in paraview to quickly view a visual of the results of the simulation
4. There is an output.log file, which is used primarily for troubleshooting