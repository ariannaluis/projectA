# projectA

## `center_of_mass.py`

1. Imports libraries
   ```
   import numpy as np
   import matplotlib.pyplot as plt
   ```
   - `numpy` handles math and vectors. It makes the center of math calculation cleaner and more efficient
   - `matplotlib` generates plots and is based on MATLAB. Here it plots the objects and centers of mass.
  
2. Defines function
   ```
   def center_of_mass_2objects(m1, r1, m2, r2):
   ```
   - Takes masses (m1, m2) and 2D positions (r1, r2) of two objects. Positions are lists like `[x,y]`
   - Converts the positions to NumPy arrays for vector subtraction and division.
   - Computes the center of mass (COM) using:

     $$\overrightarrow{R_cm} = \frac{m_{1}\overrightarrow{r_1}+m_{2}\overrightarrow{r_2}}{m_1+m_2}$$

   - Computes the displacement of each object from the center of mass using:

     $$\overrightarrow{d_1} = \overrightarrow{r_1}-\overrightarrow{R_cm}~,~~ \overrightarrow{d_2} = \overrightarrow{r_2}-\overrightarrow{R_cm}$$

   - Returns `(R_cm, d1, d2)` to the main program

3. Main program takes input
   - User enters six values:
       - `m1` -- mass of Earth
       - `x1` -- x position of Earth (0)
       - `y1` -- y position of Earth (0)
       - `m2` -- mass of Moon
       - `x2` -- x position of Moon
       - `y2` -- y position of Moon
   - These values get passed into the function, which prints numerical results and returns displacement vectors.
   - Because only the x-positions change, we model the Earth-Moon system in one dimension.
4. Plots the system
   - Earth is represented as a blue circle, moon as an orange square, and center of mass as a green star.
   - Arrows show displacement vectors from COM to each object
   - Since Earth is more massive than the Moon, the center of mass appears very close to Earth
  
## Perigee and Apogee

Real astronomical distances are input into the program. We use km along the x-axis

### Perigee

**Perigee:** Point where Moon is closest to Earth

Average distance $\approx$ 363,300km

When we input this distance:
- Center of mass shifts toward the Moon.
- Earth displacement $\approx$ 4,400km
- Moon displacement $\approx$ 358,800km

The plot shows Earth near the origin, Moon to the far right, and the center of mass slightly to the right of Earth

### Apogee

**Apogee:** Point where Moon is farthest from Earth

Average distance $\approx$ 405,500km

When we input this distance:
- Center of mass moves slightly farther from Earth than at perigee.
- Earth displacement $\approx$ 4,930km
- Moon displacement $\approx$ 400,570km

### New Moon

The last new moon occurred on **December 20, 2025 at 1:43am**. 

Distance $\approx$ 403,493km

When entered:
- Center of mass $\approx$ 4905 from Earth's center, similar to apogee range

### Full Moon

The next full moon occurrs on **January 3, 2026 at 10:03**. 

Distance $\approx$ 362,311km

When entered:
- Center of mass $\approx$ 4405 from Earth's center, similar to perigee
