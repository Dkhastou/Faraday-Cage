---
title: "Title"
author: "Daniel Khastou"
date: "9-14-26"
---

# Faraday cage simulation

## Background

### Motivation

This project was done in the winter of 2026 on the request of a friend currently working at a startup. The startup was planning on flying drones close to powerlines and needed to know how the electric and magnetic fields would affect the circuitry. The plan was to build a faraday cage around the circuitry, and he wanted a simulation to test out the viability of the faraday cage.

He sent me a CAD model of the faraday cage, and I went through the steps of meshing it and integrating it with ElmerGrid and ElmerSolver to produce a simulation

### End Result

The end result of the project is messy. By the time I was halfway through, I had made good progress, but was informed that the general direction the startup was taking was going to be different and that simulations like the one I was doing wouldn't be needed. The technical difficulties of flying these drones near intense electric and magnetic fields was too high. Around this same time I was also having issues with Elmer due to a lack of clear documentation, and decided I had made enough progress on the project for my own liking.

The result is a static simulation. I was unable to get timestepping to work despite repeated attempts and continually learning the .sif declarative language, which is heavily based on Fortran. 

## How to navigate this project

1. The notes.md contains all notes I wrote for myself in the process of learning the project workflow and all of the tools required, such as Elmer, gmsh, and more. This notes file is primarily for myself and is most likely not useful for someone else looking at the file, except that it documents my learning process in both Linux and the other tools as mentioned above.
2. I wrote some python scripts to try and automate storing the simulation results in a .db file using SQL. To my current memory, much of this is unfinished. The .db file is stored in the results, and the python scripts are stored in their own file. More updates will come
3. The .vtu file can be opened up in paraview. Display the potential gradient or the electric field of the model, and then reduce opacity to show the faraday cage inside the boundary. The electric field inside the faraday cage can be viewed by using a clipping filter. One can see that the electric field inside the faraday cage is 0 compared to everywhere outside the cage, implying that the faraday cage and simulation worked on some level. 
4. Work is still being done on reconfiguring Elmer on my current system to get this to run properly again.