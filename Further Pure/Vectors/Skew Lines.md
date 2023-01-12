# Skew Lines

Two lines are skew if they are not parallel, and do not intersect. They can only exist in space with more spatial dimensions than two.

## Proving two lines are skew

$ L_1 = \underline {r_1} + \lambda \underline{d_1} $  
$ L_2 = \underline {r_2} + \mu \underline{d_2} $

### Part 1 - The direction vectors
If $\underline{d_1} = k*\underline{d_2}$ where $k \in \mathbb{N}$, then lines are parallel, and thus, not skew, to prove that the lines are skew, prove that no scale factor exists that can scale the first direction vector, $\underline{d_1}$ to become $\underline{d_2}$.

### Part 2 - Intersection
The next thing to prove is that the lines do not intersect.  
To do this, set up the following simultaneous equations:   

$ r_{x1} + \lambda d_{1x} = r_{2x} + \mu d_{2x} $  
$ r_{1y} + \lambda d_{1y} = r_{2y} + \mu d_{2y} $  
$ r_{1z} + \lambda d_{1z} = r_{2z} + \mu d_{2z} $  

Using the first two equations to solve for $\lambda$ and $\mu$, substitute those values into the third equation. If the lines are skew, this should result in an invalid equation. Else, the lines intersect at the $\lambda$ and $\mu$ values computed earlier.