

def smallest(lista, target):
  start = 0
  end = len(lista) - 1
  min_diff = float("inf")
  closest = None
  
  if len(lista) == 0:
    return None
  if len(lista) == 1:
    return lista[0]
  
  while start <= end:
    mid = (start + end)//2

    if lista[mid] == target:
      return lista[mid]
    
    if mid + 1 < len(lista):
      diff_right = target - lista[mid + 1]
      diff_right = abs(diff_right)
    if mid > 0:
      diff_left = target - lista[mid-1]
      diff_left = abs(diff_left)
    
    if diff_right < min_diff:
      min_diff = diff_right
      closest = lista[mid+1]
    if diff_left < min_diff:
      min_diff = diff_left
      closest = lista[mid-1]

    if lista[mid] < target:
      start = mid +1
    elif lista[mid] > target:
      end = mid - 1
  return closest

A = [1,4,5,6,9,10,34,56,100]

print(smallest(A,600))
