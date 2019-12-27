import numpy as np

def p1_has_cycle(sets):
  sets = np.array(sets)
  # print(sets, 0)
  for i in range(sets.shape[0]):
    for j in range(sets.shape[1]):
      if sets[0][j] == 1:
        row = 1
        while row < sets.shape[0]:
          if sets[row][j] == -1:
            sets = np.vstack((sets, (sets[0] + sets[row])))
            if np.count_nonzero(sets[-1]) == 0:
              return True
          row += 1
    sets = np.delete(sets, 0, 0)
    # print(sets, f'{i} to {i+1}')
  return False