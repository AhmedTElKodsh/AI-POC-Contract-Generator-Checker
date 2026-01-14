# Research Story RS-16: Civil Engineering Glossary - Roads and Highways

## Glossary (100+ Terms)

1. Road - Thoroughfare for vehicles
2. Highway - Main road connecting regions
3. Expressway - Controlled-access highway
4. Freeway - High-speed controlled-access road
5. Motorway - UK term for freeway
6. Arterial Road - Major connecting road
7. Collector Road - Distributes traffic to local roads
8. Local Road - Minor street
9. Lane - Marked path for vehicles
10. Shoulder - Road edge
11. Median - Central reservation
12. Pavement - Road surface
13. Subgrade - Prepared soil base
14. Subbase - Layer below base
15. Base Course - Load-bearing layer
16. Surface Course - Wearing layer
17. Asphalt - Bituminous pavement
18. Concrete Pavement - Cement pavement
19. Flexible Pavement - Asphalt road
20. Rigid Pavement - Concrete road
21. Hot Mix Asphalt (HMA) - Heated asphalt mix
22. Cold Mix Asphalt - Unheated asphalt mix
23. Aggregate - Crushed stone/gravel
24. Bitumen - Asphalt binder
25. Binder - Glue material
26. Thickness - Layer depth
27. Compaction - Density increase
28. Density - Mass per volume
29. Moisture Content - Water content
30. California Bearing Ratio (CBR) - Subgrade strength
31. Modulus of Resilience - Material rebound characteristic
32. Fatigue Life - Load cycles before failure
33. Rutting - Pavement deformation
34. Cracking - Pavement splits
35. Pothole - Surface depression
36. Alligator Cracking - Pattern of cracks
37. Transverse Cracking - Cracks across road
38. Longitudinal Cracking - Cracks along road
39. Edge Failure - Pavement edge breakdown
40. Roughness - Surface irregularity
41. International Roughness Index (IRI) - Roughness measure
42. Skid Resistance - Tire grip capability
43. Friction - Surface resistance
44. Drainage - Water removal
45. Crown - Road slope
46. Cross Slope - Transverse slope
47. Gradient - Road slope
48. Grade - Vertical slope
49. Vertical Curve - Vertical road curve
50. Horizontal Curve - Horizontal road curve
51. Superelevation - Curve banking
52. Sight Distance - Visible distance ahead
53. Stopping Sight Distance - Brake distance
54. Passing Sight Distance - Overtaking distance
55. Design Speed - Intended speed
56. Posted Speed - Legal speed limit
57. Capacity - Maximum traffic volume
58. Level of Service (LOS) - Traffic quality measure
59. Volume - Traffic count
60. Traffic Flow - Vehicle movement
61. Traffic Density - Vehicles per distance
62. Speed - Travel velocity
63. Headway - Time between vehicles
64. Gap - Time/space between vehicles
65. Intersection - Road crossing
66. Intersection Capacity - Vehicle throughput
67. Signalized Intersection - Traffic light control
68. Unsignalized Intersection - No traffic light
69. Roundabout - Circular intersection
70. Traffic Signal - Traffic light
71. Cycle Length - Signal cycle time
72. Green Time - Signal green duration
73. Phase - Signal movement
74. Left Turn Lane - Dedicated turn lane
75. Right Turn Lane - Dedicated turn lane
76. Deceleration Lane - Speed reduction lane
77. Acceleration Lane - Speed increase lane
78. Weaving - Lane changing
79. Weaving Section - Lanes allow changing
80. Lane Drop - Reduced lane count
81. Lane Addition - Increased lane count
82. Ramp - Highway entry/exit
83. On-Ramp - Entry ramp
84. Off-Ramp - Exit ramp
85. Diamond Interchange - Ramp configuration
86. Cloverleaf Interchange - Loop ramp configuration
87. Trumpet Interchange - T-shaped interchange
88. Grade Separation - Vertical separation
89. Overpass - Road over road
90. Underpass - Road under road
91. Bridge Crossing - Bridge over obstacle
92. Culvert - Drainage pipe under road
93. Guardrail - Safety barrier
94. Barrier - Protective barrier
95. Crash Cushion - Impact absorber
96. Median Barrier - Central barrier
97. Road Marking - Pavement markings
98. Striping - Painted lines
99. Pavement Markings - Road surface markings
100. Signage - Traffic signs
101. Traffic Sign - Regulatory sign
102. Warning Sign - Advisory sign
103. Guide Sign - Informational sign
104. Illumination - Street lighting
105. Street Light - Roadside light
106. Pedestrian Crossing - Crosswalk
107. Sidewalk - Pedestrian walkway
108. Curb - Road edge
109. Curb and Gutter - Drainage structure
110. Pavement Edge - Road boundary

---

## Integration Guide

```python
def extract_road_specifications(contract_text):
    """
    Extract road specifications from contract
    """
    specs = {
        'road_type': extract_value(contract_text, r'(expressway|highway|arterial|local)'),
        'surface_type': extract_value(contract_text, r'(asphalt|concrete)'),
        'lane_count': extract_value(contract_text, r'(\d+)\s*lanes'),
        'design_speed': extract_value(contract_text, r'design\s*speed.*?(\d+)\s*km/h'),
        'pavement_thickness': extract_value(contract_text, r'thickness.*?(\d+)\s*mm')
    }
    return specs
```

---

**Research Story RS-16: COMPLETE**