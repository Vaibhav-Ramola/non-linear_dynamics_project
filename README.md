
# 1-D NLD Plotter

This program can be used to plot 1-D non-linear dynamics equation with stable and
unstable points being displayed on the graph


## Demo

To run the script open the terminal where the script is and enter

```bash
python ./1d_nld.py
```
The script will run and following will be displayed:

```bash
x1: -10                 // the lower limit of x
x2: 10                  // the upper limit of x
x_dot: np.sin(x)/x      // make sure to give the function in numpy format
```

#### For Example :
```bash
x_dot = f(x) = exp(x)*sin(x)*x^2 + 5        // normal mathematical format
x_dot: np.exp(x)*np.sin(x)*(x**2) + 5       // equivalent numpy format, acceptable by sscript
```

## Table

| Mathematical expression | Numpy equivalent |
| ----------------------- | ---------------- |
| sin(x)                  | np.sin(x)        |
| cos(x)                  | np.cos(x)        |
| tan(x)                  | np.tan(x)        |
| cosin(x)                | np.arcsin(x)     |
| sec(x)                  | np.arccos(x)     |
| cot(x)                  | np.arctan(x)     |
| sinh(x)                 | np.sinh(x)       |
| cosh(x)                 | np.cosh(x)       |
| tanh(x)                 | np.tanh(x)       |
| e^x                     | np.exp(x)        |
| ln(x)                   | np.log(x)        |

For further details head to [numpy docs](https://numpy.org/doc/stable/])
## Screenshots

![Graph Screenshot](https://github.com/Vaibhav-Ramola/non-linear_dynamics_project/blob/master/Graph.jpg)

![Terminal Screenshot](https://github.com/Vaibhav-Ramola/non-linear_dynamics_project/blob/master/Terminal%20input.png)