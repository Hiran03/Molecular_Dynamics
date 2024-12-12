# Molecular Dynamics Simulation for Tensile Test of Polymers 

Molecular Dynamics (MD) is a computational simulation technique employed in various scientific disciplines to investigate the behaviour and properties of molecular systems at the atomic level. Molecular Dynamics (MD) simulations function by numerically integrating Newton's equations of motion to predict the time evolution of a molecular system. At the core of MD lies the principle that the behaviour of a system can be determined by tracking the positions and velocities of its constituent atoms or molecules over time. 

Our objective encompasses conducting a tensile test under a constant strain rate through molecular dynamics simulation using LAMMPS, generating stress-strain plots for hydrated PVA. 

Model - PVA is a linear polymer with the formula [CH2CH(OH)]n. Using Materials Studio 2020, polymeric chains of length n were constructed. Packmol facilitated the packing of 20 such chains along with 35% (by weight) of water molecule

**File Specifications**

1. report - A detailed report of the entire project.
2. settings - Conntains all the ForceField parameters
3. Big35.data - Lammps data file specifying the coordinates of each atom in the system read from the PDB file generated earlier.
4. Big35.inp - Lammps input file to perform equilibration and tensile test. THe outputs will be saved as a log file.
5. plotting.py - Auxillary file for plotting
