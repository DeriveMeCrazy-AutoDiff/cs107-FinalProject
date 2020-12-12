# cs107-FinalProject 
[![Build Status](https://travis-ci.com/DeriveMeCrazy-AutoDiff/cs107-FinalProject.svg?token=tjHxgXnrZQTw99nTC12g&branch=m1b)](https://travis-ci.com/DeriveMeCrazy-AutoDiff/cs107-FinalProject)
[![codecov](https://codecov.io/gh/DeriveMeCrazy-AutoDiff/cs107-FinalProject/branch/master/graph/badge.svg?token=G7FvPYxS2N)](https://codecov.io/gh/DeriveMeCrazy-AutoDiff/cs107-FinalProject)

### Group #21
John Alling \
Moriya Dechtiar \
Al-Muataz Khalil \
Tianen Liu

## Installing the Package
The package can be installed by making a pip install from PyPI:
```
pip install auto_diff_pkg
```
Alternatively, the package can be installed by navigating to the top level of the repository and running a pip install:
```
pip install .
```
## Usage
The package can then be imported and utilized.
```
import auto_diff_pkg.AutoDiff as AD
```
Please see `docs/demo.ipynb` for demonstrations of the AutoDiff class.

## Broader impact
We propose a method to perform differentiation conveniently and accurately. The automatic differentiation package is able to efficiently compute the derivatives of functions of any inputs, including integers, floats, single and multiple variables. Traditionally in finite differentiation, users need to select an epsilon value for the algorithm that calculates the difference of slope. The choice of epsilon will impact the accuracy of the derivative. Our package eliminates this process for users so that they can have an accurate calculation without worrying about the choice of epsilon.

While automatic differentiation is proven to be powerful in calculating accurate derivatives, such function does not prevail in common machine learning packages. In neural networks and regression based models, gradient descent is widely used to find the optimal parameters. Automatic differentiation assists this process so that any differentiation, even when the algebraic form is hard to compute, can be done easily. This broadens the range of models one can choose from without concerning the complexity of their derivatives. If used responsibly, the benefit of a wider range of models and increasing accuracy can be broadcast to many fields including public health and medicine, where models are rather complicated.

## Software Inclusivity
We strongly believe in the importance of inclusivity of our package. We worked to ensure that our package is accessible to all and includes documentation that is easy to understand regardless of cultural and language backgrounds. The creation of this package was conducted through teamwork where every member was respected and represented, and contributed to the outcome. The coding process was discussed among members of the team, and pull requests were reviewed by members of the team before merging.

Our purpose of this package is to construct a better method of differentiation, and potentially to increase efficiency in machine learning. We discourage any illegal and unethical use of our package in projects that harm a particular group based on attributes including (but not limited to) age, culture, ethnicity, gender identity or expression, national origin, physical or mental difference, politics, race, religion, sex, sexual orientation, socio-economic status, and subculture.

