
Non string arguments can be given with or without caps. I.E. direct or Direct. There is no difference

The 'Name' keyword is for the user, and it can be set to anything. 
Elmer does not interpret this

Simualtion types are either transient or steady state

IMPORTANT
DO NOT USE PHYSICAL AND SURFACE GROUPS NUMBERS FROM THE .geo FILE!
USE THE NUMBERS LOCATED IN mesh.headers in the mesh directory that ElmerGrid creates

The (1) after Target Boundaries tells Elmer how many boundaries there are. 
For example, Target Boundaries(2) = 2 3 or TargetBoundaries(3) = 2 3 4

IMPORTANT:
The keyword "Variable" under the solver section indicates the the variable the solver is solving for. For example:
Variable = Potential indicates the variable the solver is solving for the potential
