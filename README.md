# flam_assessment

<img width="795" height="762" alt="image" src="https://github.com/user-attachments/assets/95f827dd-6efc-4b29-b2b5-ab72a2ef9ad6" />

To solve for the unknown parameters θ, M and X in the given parametric equations from the data points, the problem can be approached as a parameter estimation or curve fitting task using optimization.
The parameter t should be sampled uniformly between 6 and 60 at the same points (or approximate) used to generate data. Let's implement the parametric equations as functions of t,θ,M,X. Convert θ from degrees to radians since trigonometric functions use radians.The objective is to minimize the L1 distance (sum of absolute differences) between the predicted points and the observed points:

<img width="602" height="70" alt="image" src="https://github.com/user-attachments/assets/9d9dc1d8-3c4c-4b4e-9101-36ead7f3db43" />

Let's use a nonlinear optimization method to find θ,M,X that minimize the loss. 
The curve parameters θ,M,X influence how the parametric equations generate points.

By feeding known t values and trying different parameters, the model produces estimated (x,y) points.
The optimizer searches parameter space to minimize the sum of absolute differences (L1 distance) between actual and estimated points.
Choosing L-BFGS-B method allows constrained optimization respecting the parameter bounds.
After optimization, the parameters that best fit the data according to L1 loss are reported.


