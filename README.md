# A-new-lumped-parameter-modeling-to-evaluate-the-performance-of-wind-farm-grounding-systems
A new lumped parameter modeling to evaluate the low-frequency performance of wind farm grounding systems

This is the file folder for the article titled: A new lumped parameter modeling to evaluate the low-frequency performance of wind farm grounding systems
, recently submitted to the Electrical Power Systems Research journal (ELSEVIER).

This article addresses the impact of mutual impedance between grounding elements in measuring the grounding resistance of wind turbines using
the clamp-on ground meter. Furthermore, it proposes a new lumped parameter model for wind farm grounding to include the representation of such effects.
In this study, turbine ground resistance readings in a typical wind farm are taken by computer simulation using lumped parameter modeling and electromagnetic
field modeling. Taking the electromagnetic model as standard, the results demonstrate that the proposed solution was able to accurately estimate
the performance of a wind farm grounding system.

The attached file called "EPSR_article.xls" contains two spreadsheets:
The first one, called Section 3 Results, contains the input parameters of both computer simulation models for the study case, as well as the results obtained.
The second one, called Results of Section 4, contains the input and output data used to survey the case study`s parameter k through electromagnetic modeling by COMSOL Multiphysics.

The attached file named "case_study_simulation.mph" is the COMSOL Multiphysics model file used for the computer simulation of the case study through its electromagnetic field modeling referring to Section 3 of the article. This .mph file can also be used to survey the k parameter according to item 4 of the article, simply making changes to the electrodes' geometry and spacing between them.

The attached file named "fig2" shows the grounding of the case study containing three wind turbines interconnected by horizontal electrodes spaced 300 meters from their neighbors. 

The attached file named "fig3" shows two model nodes, in which, Rf corresponds to the turbine grounding resistance (Ω), Zs is the horizontal electrodes self-impedance (Ω), and Rp the horizontal electrodes grounding resistance (Ω). Furthermore, a resistance Rc (Ω) and an adjustment parameter k were added to the lumped-parameter model to
adequately represent the impact of mutual resistance between the grounding elements and mitigate distortions due to modeling.

The attached file named "fig4" shows the schematic representation of the grounding system simulated in COMSOL Multiphysics. The grounding of each one of the three turbines was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode was represented by a cylindrical electrode with a radius of 0.0055 m, length of 600 m, and buried at 1 m from the ground. All electrodes are inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test.

The attached file named "fig5" shows the schematic representation of the grounding system simulated in COMSOL Multiphysics to the Zmed∞ wire survey. 
The turbine grounding was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode was represented by a cylindrical electrode with a radius of 0.0055 m, buried at 1 m from the ground, and a length ranging from 80 to 800 m. All electrodes were inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test. The low-frequency soil resistivity values evaluated were from 20 to 10240 Ω.m. The relative permittivity and permeability were considered as 1. These two electrodes were energized through a feed-lumped port that connects the closest surface points between the turbine grounding and the horizontal electrode. To avoid the high reactance of the feed-lumped port being added to the measurement results, the simulation must be done in a stationary regime. A constant current source of 1 A was used. In this way, the values of the meter readings taken with a separation between electrodes of 10 times the horizontal length were estimated.

The attached file named "fig6" shows the schematic representation of the grounding system simulated in COMSOL Multiphysics to the Zmedshort lumped survey. 
The turbine grounding was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode was represented by two hemispherical electrodes whose dimensions were calculated so that each one had twice the grounding resistance value of the real horizontal electrode under test. All these electrodes are inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test. The low-frequency soil resistivity evaluated was from 20 to 10240 Ω.m. The relative permittivity and permeability were considered as 1. The energizing of these two electrodes was carried out through an 11.4 m long feed-lumped port that connects the turbine grounding to the nearest hemispherical electrode. This simulation was carried out in a stationary regime for the reasons already described. A constant current source of 1 A was295 used. In the discretization step of the FEM method, extra-fine meshes with edge refinement composed of tetrahedral elements were used in all domains of the case study in order to obtain more accurate results. In this way, the meter reading taken with a separation of 11.4m between the turbine and the horizontal electrode was estimated. 



End of this document.
