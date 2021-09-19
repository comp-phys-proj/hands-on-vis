* This is a fork of the [official dscribe](https://singroup.github.io/dscribe/latest/) GitHub repository at: https://github.com/SINGROUP/dscribe

* **IMPORTANT: THIS VERSION HAS BEEN MODIFIED TO BE USED IN SPECIFIC EDUCATIONAL ACTIVITIES!
  IT IS NOT INTENDED FOR GENERAL USE! DO NOT USE THIS CODE FOR ANY OTHER PURPOSES,
  USE THE OFFICIAL REPOSITORY INSTEAD AT: https://github.com/SINGROUP/dscribe**

* The code has been modified for use in a *Computational Physics Project* course at Linköping University.
  Dscribe was selected because it is a not overly large code with source code in good shape (docstrings, tests, documentation, etc.)

  - The code has been modified so it can run a few simple examples without dependencies directly out of the git repository.
    What has been verified to work is creating `CoulombMatrix` or `SineMatrix` instances and use them.

  - To keep the size of the repository down for student downloads, the git history has been removed.

  - Things have been removed out of the docs folder to save space! (go here for documentation: https://singroup.github.io/dscribe/latest/ )

DScribe is a python package for creating machine learning descriptors for
atomistic systems.

# Homepage
For more details and tutorials, visit the homepage at:
[https://singroup.github.io/dscribe/](https://singroup.github.io/dscribe/)

# Quick Examples
```python
import numpy as np
from ase.build import molecule
from dscribe.descriptors import CoulombMatrix

# Define atomic structures
samples_mol = [molecule("H2O"), molecule("NO2"), molecule("CO2")]

# Setup descriptors
cm_desc = CoulombMatrix(
    n_atoms_max=3,
    permutation="sorted_l2")

# Create descriptors as numpy arrays or scipy sparse matrices
water = samples_mol[0]
coulomb_matrix = cm_desc.create(water)

# Easy to use also on multiple systems, can be parallelized across processes
coulomb_matrices = cm_desc.create(samples_mol)
coulomb_matrices = cm_desc.create(samples_mol, n_jobs=3)
oxygen_indices = [np.where(x.get_atomic_numbers() == 8)[0] for x in samples_mol]
```

```python
from ase.build import bulk
from dscribe.descriptors import SineMatrix

# Define atomic structures
samples_bulk = [bulk("NaCl", "rocksalt", a=5.64),  bulk("Al", "fcc", a=4.046)]

# Setup descriptors
sm_desc = SineMatrix(
    n_atoms_max=6,
    permutation="sorted_l2",
    sparse=False,
    flatten=True)

# Create descriptors as numpy arrays or scipy sparse matrices
nacl = samples_bulk[0]
sine_matrix = sm_desc.create(nacl)

# Easy to use also on multiple systems, can be parallelized across processes
sine_matrices =  cm_desc.create(samples_bulk)
```

# Currently implemented descriptors
 * Coulomb matrix
 * Sine matrix
 * Ewald matrix
 * Atom-centered Symmetry Functions (ACSF)
 * Smooth Overlap of Atomic Positions (SOAP)
 * Many-body Tensor Representation (MBTR)
 * Local Many-body Tensor Representation (LMBTR)

# Installation
The newest versions of the package are compatible with Python 3.X (tested on
3.5, 3.6 and 3.7). DScribe versions <= 0.2.7 also support Python 2.7. We
currently only support Unix-based systems, including Linux and macOS. For
Windows-machines we suggest using the [Windows Subsystem for Linux (WSL)](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux).
The exact list of dependencies are given in setup.py and all of them will be
automatically installed during setup.

The latest stable release is available through pip: (add the -\-user flag if
root access is not available)

```sh
pip install dscribe
```

To install the latest development version, clone the source code from github
and install with pip from local file:

```sh
git clone https://github.com/SINGROUP/dscribe.git
cd dscribe
pip install .
```
