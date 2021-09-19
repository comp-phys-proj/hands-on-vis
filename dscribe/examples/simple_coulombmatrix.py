from ase.build import molecule
from dscribe.descriptors import CoulombMatrix

# Define atomic structures
samples_mol = [molecule("H2O"), molecule("NO2"), molecule("CO2")]

# Setup descriptor
cm_desc = CoulombMatrix(
    n_atoms_max=3,
    permutation="sorted_l2")

# Create descriptor
water = samples_mol[0]
coulomb_matrix = cm_desc.create(water)

print("Coulomb matrix for water:\n",coulomb_matrix)

# Create multiple descriptors
coulomb_matrices = cm_desc.create(samples_mol)

print("List of Coulomb matrices:\n", coulomb_matrices)
