import numpy as np

def normalized_points(w, h, fx, fy, cx, cy):
  """
  w: image width
  h: image height
  fx, fy, cx, cy are camera intrinsic parameters
  """
  u, v = np.meshgrid(np.arange(w), np.arange(h))

  x = (u-cx)/fx
  y = (v-cy)/fy

  return x, y

