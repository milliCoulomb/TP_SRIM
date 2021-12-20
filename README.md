# TP SRIM

Results of [SRIM](http://www.srim.org/) simulations for different projectiles on an uranium dioxide target. ***Python scripts*** are provided in each folder to analyse
and get the plots of the *energy to recoil*, *range*, *collision events* and *ionization*. Use the booleans in the script to change the ordinate axis of *collision events* from
*number/angstroms* to *DPA*. *range* can also be modified to display the concentration of projectiles in the target.

Provided in this repository:

* Data of a 4.2 MeV Helium, 70 KeV Thorium, and two fissions fragments (95 MeV Krypton and 67 MeV Barium) on a UO2 target. Calculations are done in ***full cascade*** mode.
* Python scripts in each folders, using Pysrim, to convert and analyse the outputs of SRIM.

Use an old version of ***yaml***, type:

>``$ pip install PyYaml==5.1``
