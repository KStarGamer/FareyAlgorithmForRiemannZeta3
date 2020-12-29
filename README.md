# Farey Algorithm For The Riemann Zeta Function at 3

A Python script that is able to produce more accurate approximations to a potential closed form of the Riemann Zeta Function at 3, with any user-specified form, using the Farey Algorithm. This is done essentially through brute-force.

ALL MATHEMATICAL OPERATIONS MUST BE DONE USING MPMATH OR SOME OTHER PACKAGE THAT USES MPF!
The documentation can be found here: https://mpmath.org/doc/current/general.html
This is to stop any limitations of precision with floats or doubles.

Pip installations will be required.

In the script uploaded, the form zeta(3) = p/q * pi^3 is used, where p and q are integers, and can produce correct results within errors such as 10^-3000, and decreasing.

If the user wishes to experient with a different form, e.g using ln(2), they must first define ln(2) in some form, such as infinite sum, that will increase in precision per iteration, as it gets a better approximation. Furthermore, "g" is the variable that is used to describe the division between Zeta(3) and the form being tested, e.g. Zeta(3)/(Pi^3 + ln(2)) = P/Q. A current limitation of this setup is that the coefficient that is produced by the Farey Algorithm applies to all of the terms involved in the formed, e.g. Zeta(3) = P/Q * (Pi^3 + ln(2)), where P/Q is produced by the Farey Algorithm and not instead, Zeta(3) = A/B * Pi^3 + C/D * ln(2). Thus, the coefficient is applied to both the terms and separate coefficients can not be calculated with this current setup. If anyone has any recommendations of how to do this and any potential optimisations, then I'd be more than happy to make any implementations. 

In the Farey Function, "x" is the decimal that is produced by the division of Zeta(3) and what is being tested, e.g Zeta(3) = Pi^3 = "g" => "x" in the algorithm. "N" is the maximum integer value that can be produced by either the numerator or denominator values. "h" is used as the vairable used to specify this limit into the function.

I also have a newer version of this script that involves both the Farey Algorithm and Gradient Descent to allow for faster error calculations. I have also used this setup to allow me to produce individual coefficients for the terms being tested, as I have mentioned above instead of just a collective coefficient that is multiplied to everything, however, there are currently bugs in it that I have not been able to fix as of yet but I will upload it when it is ready.



Remark: I was inspired to do this script from the following paper: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.487.9293&rep=rep1&type=pdf It has potential closed forms that can also be experiemented with using my algorithm instead which is several times faster from my testing.
