# Research Story RS-17: Civil Engineering Glossary - Utilities

## Glossary (80+ Terms)

1. Utility - Public service infrastructure
2. Water Supply - Water distribution system
3. Water Distribution - Network delivering water
4. Water Main - Primary water pipe
5. Water Service - Connection to main
6. Water Meter - Water flow measurement
7. Fire Hydrant - Water source for firefighting
8. Wastewater - Used water
9. Sewer - Wastewater transport
10. Sanitary Sewer - Domestic wastewater pipe
11. Storm Sewer - Stormwater drainage pipe
12. Combined Sewer - Mixed wastewater pipe
13. Sewer Main - Primary sewer pipe
14. Manhole - Sewer access point
15. Lift Station - Pumping station
16. Pump Station - Pumping facility
17. Treatment Plant - Wastewater treatment
18. Wastewater Treatment - Cleaning wastewater
19. Primary Treatment - Initial treatment
20. Secondary Treatment - Biological treatment
21. Tertiary Treatment - Advanced treatment
22. Disinfection - Killing pathogens
23. Effluent - Treated wastewater
24. Sludge - Waste solids
25. Biosolids - Treated sludge
26. Drainage - Water removal
27. Storm Drainage - Rainwater drainage
28. Surface Drainage - Above-ground drainage
29. Subsurface Drainage - Underground drainage
30. French Drain - Gravel-filled trench
31. Drainage Pipe - Water removal pipe
32. Culvert - Drainage structure
33. Ditch - Open drainage channel
34. Swale - Vegetated drainage channel
35. Catch Basin - Stormwater inlet
36. Inlet - Drainage entry
37. Outlet - Drainage exit
38. Outfall - Discharge point
39. Detention Basin - Temporary storage
40. Retention Basin - Permanent storage
41. Infiltration - Water entering ground
42. Permeation - Water movement through material
43. Permeable Surface - Water-penetrable surface
44. Impervious Surface - Water-resistant surface
45. Electrical Utility - Power supply
46. Power Distribution - Electricity distribution
47. Power Line - Electrical transmission line
48. Transmission Line - High-voltage line
49. Distribution Line - Lower-voltage line
50. Transformer - Voltage changer
51. Substation - Transformer facility
52. Underground Cable - Buried electrical line
53. Overhead Line - Aerial electrical line
54. Utility Pole - Support for lines
55. Gas Utility - Natural gas supply
56. Gas Distribution - Gas piping network
57. Gas Main - Primary gas pipe
58. Gas Service - Connection to main
59. Gas Meter - Gas flow measurement
60. Gas Regulator - Pressure control
61. Telecommunication - Communication systems
62. Fiber Optic Cable - Optical communication line
63. Coaxial Cable - Communication cable
64. Conduit - Protective pipe
65. Duct - Protective channel
66. Utility Corridor - Shared utility space
67. Right-of-Way (ROW) - Legal access corridor
68. Easement - Legal right to use land
69. Utility Mapping - Recording utility locations
70. Utility Locating - Finding buried utilities
71. Utility Marking - Surface utility marks
72. Vacuum Excavation - Safe excavation
73. Trench - Narrow excavation
74. Trenching - Excavating trenches
75. Trenchless Installation - No-dig installation
76. Horizontal Directional Drilling (HDD) - Underground drilling
77. Pipe Bursting - Replacing underground pipe
78. Cured-in-Place Pipe (CIPP) - Pipe lining
79. Slip Lining - Pipe insertion
80. Pipe Jacking - Pipe pushing
81. Microtunneling - Small tunneling
82. Excavation - Removing earth
83. Backfill - Refilling excavation
84. Compaction - Density increase
85. Bedding - Pipe support layer
86. Haunching - Pipe side support
87. Cover - Soil above pipe
88. Pipe Material - Pipe construction material
89. PVC Pipe - Polyvinyl chloride pipe
90. HDPE Pipe - High-density polyethylene pipe
91. Ductile Iron Pipe - Flexible iron pipe
92. Concrete Pipe - Cement pipe
93. Steel Pipe - Metal pipe
94. Pipe Diameter - Pipe width
95. Pipe Length - Pipe extent
96. Joint - Pipe connection
97. Coupling - Connector
98. Flange - Pipe end connection
99. Gasket - Sealing ring
100. Valve - Flow control device

---

## Integration Guide

```python
def extract_utility_specifications(contract_text):
    """
    Extract utility specifications from contract
    """
    utilities = {
        'water': {
            'main_size': extract_value(contract_text, r'water\s+main.*?(\d+)\s*mm'),
            'material': extract_value(contract_text, r'water\s+pipe.*?(PVC|HDPE|ductile|concrete|steel)'),
            'pressure': extract_value(contract_text, r'water\s+pressure.*?(\d+)\s*bar')
        },
        'sewer': {
            'main_size': extract_value(contract_text, r'sewer\s+main.*?(\d+)\s*mm'),
            'material': extract_value(contract_text, r'sewer\s+pipe.*?(PVC|concrete|clay|corrugated)'),
            'slope': extract_value(contract_text, r'sewer\s+slope.*?([\d.]+)%')
        },
        'electrical': {
            'voltage': extract_value(contract_text, r'voltage.*?(\d+)\s*kV'),
            'method': extract_value(contract_text, r'(underground|overhead)\s+lines')
        }
    }
    return utilities
```

---

**Research Story RS-17: COMPLETE**