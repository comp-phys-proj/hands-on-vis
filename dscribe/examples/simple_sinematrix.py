from ase.build import bulk
from ase.spacegroup import crystal
from dscribe.descriptors import SineMatrix

# Define atomic structures

skutterudite = crystal(('Co', 'Sb'), basis=[(0.25, 0.25, 0.25), (0.0, 0.335, 0.158)], spacegroup=204, cellpar=[9.04, 9.04, 9.04, 90, 90, 90])
nacl = bulk("NaCl", "rocksalt", a=5.64)
al = bulk("Al", "fcc", a=4.046)
fe = bulk("Fe", "bcc", a=2.856)

samples_bulk = [skutterudite, nacl, al, fe]

# Setup descriptor
sm_desc = SineMatrix(
    n_atoms_max=35,
    permutation="sorted_l2",
    sparse=False,
    flatten=True)

# Create single descriptor
sine_matrix = sm_desc.create(skutterudite)

print("Sine matrix for skutterudite:\n",sine_matrix)

# Create multiple descriptors
sine_matrices =  sm_desc.create(samples_bulk)

print("List of Sine matrices:\n", sine_matrices)
