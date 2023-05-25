A new lumped parameter modeling for wind farm grounding measurement circuits based on clamp-on ground meters.

This is the file folder for the article titled: A new lumped parameter modeling for wind farm grounding measurement circuits based on clamp-on ground meters
, recently submitted to the Electrical Power Systems Research journal (ELSEVIER).

This article addresses the impact of mutual impedance between grounding elements in measuring the grounding resistance of wind turbines using
the clamp-on ground meter. Furthermore, it proposes a new lumped parameter model for wind farm grounding to include the representation of such effects.
In this study, turbine ground resistance readings in a typical wind farm are taken by computer simulation using lumped parameter modeling and electromagnetic
field modeling. Taking the electromagnetic model as standard, the results demonstrate that the proposed solution was able to accurately estimate the wind turbine grounding resistance in a typical wind farm.

The attached file called "Paper_results.xlsx" contains two spreadsheets:
The first one, called "Results of Section 3", contains the input parameters of both computer simulation models for the study case, as well as the results obtained.
The second one, called "Results of Section 4", contains the input and output data used to survey the case study`s parameter k through electromagnetic modeling by COMSOL Multiphysics.

The attached file called "Fig1.pdf" presents the equivalent circuit of the case study according to [23] and the proposed model.

The attached file named "case_study_COMSOL.mph" is the COMSOL Multiphysics model file used for the computer simulation of the case study through its electromagnetic field modeling according to Section 3 of the article. This ".mph file" can also be used to survey the k parameter according to item 4 of the article, simply making changes to the electrodes' geometry and spacing between them. 

The attached file named "fig2" shows the design schematic representation of the case study grounding system containing three groundings of wind turbines spaced 300 meters from their neighbors and interconnected by horizontal electrodes, as well as the clamp-on ground meter used to evaluate the grounding resistance of the turbine of interest.

The attached file named "fig3" presents the equivalent measurement circuit of the case study modeled by lumped parameters, in which, Rf corresponds to the turbine grounding resistance (Ω), Zs is the horizontal electrodes' self-impedance (Ω), and Rp is the horizontal electrodes grounding resistance (Ω). Furthermore, a resistance Rc (Ω) and an adjustment parameter k were added to the lumped-parameter model to represent the impact of mutual resistance between the grounding elements and mitigate distortions due to modeling.

The attached file called "fig4" presents the case study electromagnetic model used in the COMSOL Multiphysics. The grounding of each one of the three turbines was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode has a cross-sectional area of 95 mm2, a length of 600 m, and is buried at 1 m from the ground. All electrodes are inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test.

The attached file named "fig5" shows the schematic representation of the grounding system electromagnetic model simulated in COMSOL Multiphysics to the Zmed_∞_wire survey. 
The turbine grounding was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode was represented by a cylindrical geometry with a cross-sectional area of 95 mm2, buried at 1 m from the ground, and a length ranging from 80 to 800 m. All electrodes were inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test. The low-frequency soil resistivity values evaluated were from 20 to 10240 Ω.m. The relative permittivity and permeability were considered as 1. These two electrodes were energized through a feed-lumped port that connects the closest surface points between the turbine grounding and the horizontal electrode. To avoid the high reactance of the feed-lumped port being added to the measurement results, the simulation must be done in a stationary regime. A constant current source of 1 A was used. In this way, the values of the meter readings taken with a separation between electrodes of 10 times the horizontal length were estimated.

The attached file named "fig6" shows the schematic representation of the grounding system electromagnetic model simulated in COMSOL Multiphysics to the Zmed_short_lumped survey. The turbine grounding was represented by a cylindrical copper electrode with a radius of 7.88 m and a height of 17.2 m. The horizontal electrode was represented by two hemispherical electrodes whose dimensions were calculated so that each one had twice the grounding resistance value of the real horizontal electrode under test. All these electrodes are inserted in a volume of soil with hemispherical geometry with a radius of 30 times the length of the horizontal electrode under test. The low-frequency soil resistivity evaluated was from 20 to 10240 Ω.m. The relative permittivity and permeability were considered as 1. The energizing of these two electrodes was carried out through an 11.4 m long feed-lumped port that connects the turbine grounding to the nearest hemispherical electrode. This simulation was carried out in a stationary regime for the reasons already described. A constant current source of 1 A was used. In this way, the meter reading taken with a separation of 11.4m between the turbine and the horizontal electrode was estimated. 

The attached file called "fig8.jpg" shows a detail of the discretization mesh of the case study model built in COMSOL. In the discretization step of the finite element method used by COMSOL, extra-fine meshes with edge refinement composed of tetrahedral elements.

End of this document.
