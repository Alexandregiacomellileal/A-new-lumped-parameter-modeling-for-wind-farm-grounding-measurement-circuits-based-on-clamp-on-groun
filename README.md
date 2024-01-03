## A new lumped parameter modeling for wind farm grounding measurement circuits based on clamp-on ground meters.

![LPM_030124](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/assets/96079504/3421fd54-5b76-458d-a13e-525662ec4fb8)

### Overview

Welcome to the repository for the research article titled "A New Lumped Parameter Modeling for Wind Farm Grounding Measurement Circuits Based on Clamp-On Ground Meters," recently submitted to the Journal of Control, Automation and Electrical Systems - Springer Nature. This work delves into the impact of mutual impedance between grounding elements when measuring the grounding resistance of wind turbines using clamp-on ground meters. The repository provides files and resources related to the study, including simulation models, results, and visual representations.

### Article Highlights

The research article addresses:
- The impact of mutual impedance in measuring wind turbine grounding resistance.
- Proposal of a novel lumped parameter model for wind farm grounding.
- Simulation of turbine ground resistance readings through lumped parameter modeling and electromagnetic field modeling.
- Demonstration of the accuracy of the proposed solution in estimating the impedance of the measuring loop in a wind farm grounding system.

### Results

The table 1 compares the meter readings $Zmed_{LPM}$ obtained by means of lumped parameter modeling used in [^1], with those proposed in this paper. Table 1 also presents the values of the readings obtained through Computational Electromagnetic Modeling using COMSOL $Zmed_{EFM}$.

The measurement circuit was simulated under different homogeneous soil with a low-frequency resistivity of 100, 300, 5252, and 10240  $\Omega \cdot m$. A computer simulation was also carried out using a typical two-layer soil with a resistivity of 5252  $\Omega \cdot m$ in the first five meters of depth and 300  $\Omega \cdot m$ on the deeper layer. The results obtained by the computational simulation of the electromagnetic model of the case study were not significantly affected by the variation between 1 and 10 of the relative permittivity of the soil, so we assume that its value is constant and equal to 9 in this study. Taking $Zmed_{EFM}$ as a standard, the electric circuit modeling expected absolute percentage error ${APE}_{LPM} (\%)$ is calculated as:
\begin{equation}
{APE}_{LPM} = \left |\ \frac{{{Zmed}_{LPM}\ -\ \ Zmed}_{EFM}}{{Zmed}_{EFM}}  \right | \times 100,
\label{eq:eqrf6}
\end{equation}

Table 1 shows a good agreement of the results obtained between the proposed lumped-parameter model and the electromagnetic method. Considering homogeneous soil, the model could represent the behavior of the actual measurement circuit from the lowest to the highest apparent soil resistivity found in wind farms. The error was nearly zero for soils with high resistivities typically encountered in wind farms. For soil with a low resistivity of 100 $\Omega \cdot m$, the model yielded an Absolute Percent Error (APE) of 10.27\%, surpassing the performance of [^1] by 81.7\%. The simulation results demonstrate that the proposed solution can accurately estimate the low-frequency impedance of the measuring loop, with an average error of 85.8\% lower than the model used in [^1].

**Table 1**   
| $\rho \ (\Omega \cdot m)$ | $Zmed_{EFM} (\Omega)$ | $Zmed_{LPM} (\Omega)$ [^1]| $Zmed_{LPM} (\Omega)$ (Proposed) | $APE_{LPM}$ (%) [^1]| $APE_{LPM}$  (%) (Proposed)|
|---------------|------------------------|------------------------|----------------------------------|------------------|------------------------|
| 100             | 1.26              | 1.97                | 1.38                       | 56.25            | **10.27**              |
| 300             | 3.65                | 5.22                | 3.82                         | 42.84            | **4.70**               |
| 5252            | 59.92               | 76.08                | 60.09                          | 26.96            | **0.28**               |
| 10240           | 116.80            | 149.59              | 117.08                         | 28.07            | **0.24**               |
| 5252 (< 5m) and 300 (> 5m)            | 5.38           | 6.67               | 5.91                          | 24.08            | **9.88**               |


### Files

- [[Paper_results.xlsx](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/Paper_results.xlsx)]: Excel file comprising two spreadsheets: (i) "Results of Section 3" containing input parameters for both computer simulation models in the study case, along with the corresponding results, and (ii) "Results of Section 3.1" encompassing input and output data employed for investigating the parameter $k$ in the case study through electromagnetic modeling using COMSOL Multiphysics.

- [[case_study_COMSOL.mph](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/case_study_COMSOL.mph)] : COMSOL Multiphysics model file used for the computer simulation of the case study through its electromagnetic field modeling according to Section 2.3 of the associated research paper. Such file can also be used to survey the $k$ parameter according to Subsection 3.1, simply making changes to the electrodes' geometry and spacing between them. 

- [[fig1.pdf](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/fig1.pdf)] presents the equivalent circuit of the case study according to [^1] and the proposed model in the associated research paper.

- [[fig2.pdf](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/fig2.pdf)] shows the design schematic representation of the case study grounding system containing three groundings of wind turbines spaced 300 meters from their neighbors and interconnected by horizontal electrodes, as well as the clamp-on ground meter used to evaluate the grounding resistance of the turbine of interest.

- [[fig3.pdf](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/fig3.pdf)] presents the equivalent measurement circuit of the case study modeled by lumped parameters, in which, $R_f$ corresponds to the turbine grounding resistance (Ω), $Z_s$ is the horizontal electrodes' self-impedance (Ω), and $R_p$ is the horizontal electrodes grounding resistance (Ω). Furthermore, a resistance $R_c$ (Ω), a capacitance $C_c$ (F) and an adjustment parameter $k$ were added to the lumped-parameter model to represent the impact of mutual resistance between the grounding elements and mitigate distortions due to modeling.

- [[fig4.pdf](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/fig4.pdf)] shows the schematic representation of the grounding system electromagnetic model simulated in COMSOL Multiphysics to the $Zmed^∞_{wire}$ survey. The turbine grounding was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode was represented by a cylindrical geometry with a cross-sectional area of 95 mm2, buried at 1 m from the ground, and a length ranging from 80 to 800 m. All electrodes were inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test. The measurement circuit was energized through a feed-lumped port that connects the closest surface points between the turbine grounding and the horizontal electrode. To avoid the high reactance of the feed-lumped port being added to the measurement results, the simulation must be done in a stationary regime. The low-frequency soil resistivity values evaluated were from 20 to 10240 Ω.m. The relative permeability and permittivity of the soil were assumed to be constant and equal to 1 and 9, respectively. In this way, the values of the meter readings taken with a separation between electrodes of 10 times the horizontal length were estimated.

- [[fig5.pdf](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/fig5.pdf)] shows the schematic representation of the grounding system electromagnetic model simulated in COMSOL Multiphysics to the $Zmed^{short}_{lumped}$ survey. The turbine grounding was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode was represented by two hemispherical electrodes whose dimensions were calculated so that each one had twice the grounding resistance value of the real horizontal electrode under test. All these electrodes are inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test. The measurement circuit was energized through an 11.4 m long feed-lumped port that connects the turbine grounding to the nearest hemispherical electrode. This simulation was carried out in a stationary regime for the reasons already described. The low-frequency soil resistivity evaluated was from 20 to 10240 Ω.m. The relative permeability and permittivity of the soil were assumed to be constant and equal to 1 and 9, respectively. In this way, the meter reading taken with a separation of 11.4 m between the turbine and the horizontal electrode was estimated. 

- [[fig6.pdf](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/blob/main/fig6.pdf)] shows an image of the discretization mesh of the case study model built in COMSOL. In the discretization step of the finite element method used by COMSOL, extra-fine meshes with edge refinement are composed of tetrahedral elements.

[^1]: A.G. Leal, H.L. L ́opez-Salamanca, A.E. Lazzaretti, D.C. Marcilio, A new approach for ground resistance measurements in onshore wind farms based on clamp-on meters and artificial neural network, Electric Power Systems Research. 210 (2022) 108161.
________________________________________________________________________________________________________________________

### Contact us:
Please send an email to: alexgiacomelli@yahoo.com

________________________________________________________________________________________________________________________

### Contributors:
Federal University of Technology – Parana (UTFPR) and Institute of Technology for Development (LACTEC)
