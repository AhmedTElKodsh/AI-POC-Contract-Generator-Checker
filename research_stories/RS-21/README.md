# Research Story RS-21: Hydrological Modeling Guides

## Glossary (70+ Terms)

1. Hydrological Model - Water simulation
2. Model Calibration - Parameter adjustment
3. Model Validation - Verification
4. Simulation - Running model
5. Scenario Analysis - Testing conditions
6. Deterministic Model - Fixed outcomes
7. Stochastic Model - Probabilistic outcomes
8. Lumped Model - Simplified model
9. Distributed Model - Spatially detailed
10. Semi-Distributed Model - Hybrid approach
11. HEC-HMS - Hydrologic model
12. HEC-RAS - Hydraulic model
13. SWMM - Stormwater model
14. MODFLOW - Groundwater model
15. GSSHA - Distributed hydrologic model
16. RHESSys - Ecosystem hydrologic model
17. VIC Land Surface - Macroscale model
18. HBV - Hydrological model
19. Sacramento - Soil moisture model
20. TOPMODEL - Topographic model
21. SWAT - Watershed model
22. MIKE SHE - Integrated model
23. MIKE 11 - River model
24. SOBEK - River model
25. HEC-1 - Watershed model
26. TR-20 - Watershed model
27. TR-55 - Peak runoff model
28. NRCS Curve Number - Runoff estimation
29. Rational Method - Peak flow method
30. Time of Concentration - Travel time
31. Travel Time - Movement duration
32. Flow Path - Water route
33. Flow Accumulation - Contributing area
34. Flow Direction - Water movement direction
35. Digital Elevation Model (DEM) - Topographic grid
36. DEM Resolution - Grid cell size
37. Digital Terrain Model (DTM) - Terrain surface
38. Digital Surface Model (DSM) - Including features
39. LiDAR - Laser elevation data
40. Topographic Survey - Ground measurement
41. Rainfall-Runoff Model - Precipitation to flow
42. Snowmelt Model - Snow to water
43. Infiltration Model - Water entry
44. Groundwater Model - Subsurface flow
45. Surface Water Model - Surface flow
46. Combined Model - Integrated systems
47. One-Dimensional Model - 1D flow
48. Two-Dimensional Model - 2D flow
49. Three-Dimensional Model - 3D flow
50. Finite Difference - Numerical method
51. Finite Element - Numerical method
52. Finite Volume - Numerical method
53. Grid - Numerical mesh
54. Mesh - Numerical network
55. Cell - Grid element
56. Node - Grid point
57. Boundary Condition - Model edges
58. Initial Condition - Model start
59. Time Step - Simulation increment
60. Model Output - Simulation results
61. Model Performance - Accuracy measure
62. Model Uncertainty - Result variability
63. Sensitivity Analysis - Parameter importance
64. Model Calibration - Parameter adjustment
65. Model Verification - Code testing
66. Model Validation - Data testing
67. Goodness of Fit - Accuracy metric
68. Nash-Sutcliffe - Model efficiency
69. RMSE - Root mean square error
70. MAE - Mean absolute error
71. Bias - Systematic error
72. Model Scenario - Test condition
73. Extreme Event - Rare condition
74. Climate Change Scenario - Future climate
75. Land Use Change Scenario - Development impact
76. Flood Forecast - Predicting floods
77. Flood Warning System - Alert system
78. Real-Time Monitoring - Continuous observation
79. Data Assimilation - Updating models
80. Ensemble Forecast - Multiple models
81. Probabilistic Forecast - Probability-based
82. Model Uncertainty Quantification - Error estimation

---

## Integration Guide

```python
def setup_hydrological_model(model_type, input_data):
    """
    Setup hydrological model based on contract requirements
    """
    if model_type == 'HEC-HMS':
        model = setup_hms_model(input_data)
    elif model_type == 'HEC-RAS':
        model = setup_ras_model(input_data)
    elif model_type == 'SWMM':
        model = setup_swmm_model(input_data)

    return model
```

---

**Research Story RS-21: COMPLETE**