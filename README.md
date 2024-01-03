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

### Case study

A grounding section of the São Bento Wind Complex (SBC) located in northeastern Brazil was chosen to present and validate the proposed model. Figure 1 shows the grounding of the case study containing three wind turbines interconnected by horizontal electrodes of 300 m. Such a grounding represents a typical section of a conventional wind farm grounding system. The grounding of the turbine consists of a reinforced concrete foundation and bare copper wires and has an approximately cylindrical shape with a radius of 7.88 m and a height of 17.2 m. The horizontal electrodes consist of a 300 m long bare copper wire with a cross-section of $95 mm^2$, buried at a depth of 1 m. The horizontal electrode wires are drawn into the turbine tower through an insulated conduit and connected to the main earth bonding bar. The closest distance () between the turbine grounding edge and the horizontal electrodes is 11.4 m.

**Figure 1**      
<img src="https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding/assets/96079504/87161e42-e7d9-4699-a4cc-77c3864decb0" width="500" height="375">

The instrument chosen for the case study was a UT278A clamp-on meter whose induced voltage signal in the measurement circuit has a sinusoidal waveform with a constant amplitude of 0.028 V and a frequency of 1572 Hz. This work will consider that the case study grounding system can be installed in different homogeneous soils with a low-frequency resistivity $\rho$ of 100, 300, 5252, and 10240 $\Omega \cdot m$. Additionally, it will be evaluated its installation in a typical two-layer soil with a resistivity of 5252 $\Omega \cdot m$ in the first five meters of depth and 300 $\Omega \cdot m$ in the deepest layer. The relative permeability and permittivity of the soil were assumed to be constant and equal to 1 and 9, respectively. 

### Electrical Circuit and Grounding Resistance Calculation

The electrical circuit for the measurements was established and simulated in ATP to acquire the meter readings Zmed<sub>LPM</sub> following the procedures detailed in Section 2.2 of the associated research paper. Furthermore, the lumped parameter modeling used in [our previous work](https://github.com/Alexandregiacomellileal/A-New-Approach-Towards-Error-Reduction-in-Ground-Resistance-Measurements-Based-on-Clamp-on-Method) [^1] was also established and simulated in ATP for comparative purposes. The ATP files used by the authors are [[23_model_rod1.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/23_model_rod1.acp)], [[23_model.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/23_model.acp)], [[23_model_rod3.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/23_model_rod3.acp)], [[celulapi_COMSOL_k_RLC.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/celulapi_COMSOL_k_RLC.acp)], [[celulapi_COMSOL_k_RLC_rod1.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/celulapi_COMSOL_k_RLC_rod1.acp)], and [[celulapi_COMSOL_k_RLC_rod3.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/celulapi_COMSOL_k_RLC_rod3.acp)]. 

### $k$ Parameter Estimation

In our quest to mitigate the impact of mutual coupling in measurements and address distortions arising from the utilization of an equivalent semi-spherical representation of the horizontal electrode, we are engaged in refining the estimation process. Our focus is on enhancing accuracy and reliability by systematically assessing and adjusting the parameters involved in the measurement system.

According to Section 3.1 of the associated research article, the parameter k was estimated to be 0.7 for a distance between the turbine grounding and the adjacent horizontal electrode of 11.4 m (defined as $s$).

### Results

Table 1 compares the meter readings $Zmed_{LPM}$ obtained by means of lumped parameter modeling used in [^1], with those proposed in this paper. Table 1 also presents the values of the readings obtained through Computational Electromagnetic Modeling using COMSOL $Zmed_{EFM}$. The measurement circuit was simulated under different homogeneous soil with a low-frequency resistivity of 100, 300, 5252, and 10240  $\Omega \cdot m$. A computer simulation was also carried out using a typical two-layer soil with a resistivity of 5252  $\Omega \cdot m$ in the first five meters of depth and 300  $\Omega \cdot m$ on the deeper layer. The results obtained by the computational simulation of the electromagnetic model of the case study were not significantly affected by the variation between 1 and 10 of the relative permittivity of the soil, so we assume that its value is constant and equal to 9 in this study. In the context of electric circuit modeling, the expected absolute percentage error ($APE_{LPM}$) is calculated based on the standard $Zmed_{EFM}$. The formula for calculating $APE_{LPM}$ (%) is given by:

$\ APE_{LPM} = |\frac{{Zmed_{LPM} - Zmed_{EFM}}}{{Zmed_{EFM}}}| \times 100 \$

Where:
- $APE_{LPM}$ is the expected absolute percentage error for the electric circuit modeling.
- $Zmed_{EFM}$ is the standard value taken for comparison.
- $Zmed_{LPM}$ is the observed value from the electric circuit modeling.

This formula provides a measure of the percentage difference between the observed and standard values, allowing for an assessment of the accuracy of the electric circuit model.

**Table 1: Comparison of Meter Readings**   
| $\rho \ (\Omega \cdot m)$ | $Zmed_{EFM} (\Omega)$ | $Zmed_{LPM} (\Omega)$ [^1]| $Zmed_{LPM} (\Omega)$ (Proposed) | $APE_{LPM}$ (%) [^1]| $APE_{LPM}$  (%) (Proposed)|
|---------------|------------------------|------------------------|----------------------------------|------------------|------------------------|
| 100             | 1.26              | 1.97                | 1.38                       | 56.25            | **10.27**              |
| 300             | 3.65                | 5.22                | 3.82                         | 42.84            | **4.70**               |
| 5252            | 59.92               | 76.08                | 60.09                          | 26.96            | **0.28**               |
| 10240           | 116.80            | 149.59              | 117.08                         | 28.07            | **0.24**               |
| 5252/300          | 5.38           | 6.67               | 5.91                          | 24.08            | **9.88**               |

Table 1 illustrates a robust agreement in the outcomes obtained between the proposed lumped-parameter model and the electromagnetic method. When considering homogeneous soil, the model adeptly captures the behavior of the actual measurement circuit across a spectrum of apparent soil resistivity, spanning from the lowest to the highest values encountered in wind farms. Notably, the error approached zero for soils characterized by high resistivities, a common scenario in wind farm environments. The simulation results demonstrate that the proposed solution excels in accurately estimating the low-frequency impedance of the measuring loop. On average, the proposed model exhibits an error rate that is 85.8% lower compared to the model used in [^1].

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
