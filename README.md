# PointCloudGeneration
point-cloud generation in python

How to use:

```python
x, y = normalized_points(w, h, fx, fy, cx, cy) #call only once


for depth in depth_list:
  X =  x * depth
  Y =  y * depth
  Z =  depth
```
