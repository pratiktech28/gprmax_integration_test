import numpy as np
# Ek dummy array banao (GPR wave ki tarah)
data = np.sin(np.linspace(0, 10, 100)) 
# Inhe save kar lo
np.save('golden_reference.npy', data)
np.save('current_simulation.npy', data)
print("Files Created Successfully!")