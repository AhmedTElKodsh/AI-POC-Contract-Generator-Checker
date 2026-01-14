# Research Story RS-20: Hydrological Detailed Glossary

## Glossary (100+ Terms)

1. Hydrology - Water science
2. Hydrological Cycle - Water circulation
3. Precipitation - Rain, snow, hail
4. Rainfall - Water droplets falling
5. Snowfall - Frozen precipitation
6. Snowmelt - Melting snow
7. Infiltration - Water entering soil
8. Percolation - Water moving downward
9. Runoff - Surface water flow
10. Surface Runoff - Water flowing over surface
11. Subsurface Flow - Underground flow
12. Interflow - Lateral subsurface flow
13. Baseflow - Groundwater flow to streams
14. Streamflow - Water flow in streams
15. Discharge - Volume flow rate
16. Flood - Overflow
17. Floodplain - Inundation area
18. Flood Frequency - Probability of flood
19. Return Period - Average interval between events
20. Design Flood - Flood for design
21. Probable Maximum Flood (PMF) - Theoretical maximum
22. Flood Routing - Flood wave movement
23. Flood Routing Model - Flood simulation
24. Hydrograph - Flow vs time
25. Unit Hydrograph - Rainfall-runoff relationship
26. S-Curve - Cumulative hydrograph
27. Infiltration Rate - Rate of water entry
28. Infiltration Capacity - Maximum infiltration rate
29. Infiltration Excess - Runoff from saturated soil
30. Saturation Excess - Runoff from water table
31. Horton Infiltration - Infiltration equation
32. Green-Ampt - Infiltration model
33. Curve Number - Runoff estimation
34. Soil Moisture - Water in soil
35. Soil Water Content - Water fraction
36. Field Capacity - Water retained after drainage
37. Wilting Point - Minimum usable water
38. Available Water - Usable water range
39. Porosity - Void fraction
40. Permeability - Water flow ability
41. Hydraulic Conductivity - Water flow rate
42. Transmissivity - Layer transmission
43. Specific Yield - Drainable water
44. Specific Retention - Retained water
45. Groundwater - Underground water
46. Water Table - Groundwater surface
47. Aquifer - Water-bearing formation
48. Confined Aquifer - Pressurized aquifer
49. Unconfined Aquifer - Atmospheric pressure aquifer
50. Artesian Well - Flowing well
51. Well - Groundwater extraction
52. Pumping Test - Aquifer testing
53. Slug Test - Quick aquifer test
54. Groundwater Recharge - Water entering aquifer
55. Groundwater Discharge - Water leaving aquifer
56. Dewatering - Water removal
57. Drainage - Water removal
58. Stormwater Drainage - Rainwater removal
59. Urban Drainage - City drainage
60. Culvert - Drainage pipe
61. Drainage Basin - Watershed
62. Watershed - Drainage area
63. Catchment Area - Water collection area
64. Drainage Area - Contributing area
65. River Basin - Large drainage basin
66. Subbasin - Smaller drainage unit
67. Divide - Watershed boundary
68. Watershed Boundary - Drainage divide
69. Channel - Water course
70. River Channel - Flow path
71. Stream - Natural channel
72. Creek - Small stream
73. Tributary - Stream joining main
74. Confluence - Stream junction
75. Stream Order - Stream classification
76. Channel Slope - Stream gradient
77. Channel Geometry - Cross-section shape
78. Channel Roughness - Flow resistance
79. Manning's n - Roughness coefficient
80. Chezy Coefficient - Flow coefficient
81. Froude Number - Flow regime
82. Reynolds Number - Flow type
83. Critical Flow - Unstable flow
84. Supercritical Flow - Fast flow
85. Subcritical Flow - Slow flow
86. Hydraulic Jump - Flow transition
87. Flow Regime - Flow classification
88. Laminar Flow - Smooth flow
89. Turbulent Flow - Chaotic flow
90. Open Channel Flow - Surface water flow
91. Pipe Flow - Enclosed flow
92. Pipe Diameter - Pipe width
93. Pipe Slope - Pipe gradient
94. Pipe Capacity - Maximum flow
95. Design Flow - Intended flow
96. Peak Flow - Maximum flow rate
97. Average Flow - Mean flow
98. Low Flow - Minimum flow
99. Flow Duration - Flow time series
100. Flood Stage - Water level
101. Flood Depth - Water height
102. Flood Velocity - Water speed
103. Flood Duration - Flood time
104. Flood Damage - Flood impact
105. Flood Risk - Flood probability
106. Flood Mitigation - Reducing flood impact
107. Flood Control - Managing floods
108. Levee - Flood embankment
109. Flood Wall - Flood barrier
110. Detention Pond - Temporary storage
111. Retention Pond - Permanent storage
112. Dam - Water barrier
113. Reservoir - Water storage
114. Spillway - Dam overflow
115. Diversion - Flow redirection
116. Channelization - Channel modification
117. River Training - Flow control
118. Flood Warning - Alert system
119. Emergency Response - Disaster response
120. Evacuation - Moving people

---

## Integration Guide

```python
def extract_hydrological_specs(contract_text):
    """
    Extract hydrological specifications
    """
    specs = {
        'design_flood': extract_value(contract_text, r'design\s+flood.*?(\d+)-year'),
        'drainage_area': extract_value(contract_text, r'drainage\s+area.*?(\d+\.?\d*)\s*km'),
        'rainfall_intensity': extract_value(contract_text, r'rainfall.*?(\d+)\s*mm/hour'),
        'flood_elevation': extract_value(contract_text, r'flood\s+elevation.*?([\d.]+)\s*m')
    }
    return specs
```

---

**Research Story RS-20: COMPLETE**