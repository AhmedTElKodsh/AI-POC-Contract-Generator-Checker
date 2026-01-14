# Research Story RS-18: Civil Engineering Glossary - Structures

## Glossary (100+ Terms)

1. Structure - Built construction
2. Building - Enclosed structure
3. Superstructure - Above-ground portion
4. Substructure - Below-ground portion
5. Foundation - Supporting base
6. Structural System - Load-bearing framework
7. Load - Applied force
8. Dead Load - Permanent load
9. Live Load - Temporary load
10. Environmental Load - Weather-induced load
11. Seismic Load - Earthquake-induced load
12. Wind Load - Wind-induced load
13. Snow Load - Snow-induced load
14. Temperature Load - Thermal-induced load
15. Impact Load - Sudden load application
16. Static Load - Constant load
17. Dynamic Load - Varying load
18. Distributed Load - Spread load
19. Concentrated Load - Point load
20. Uniform Load - Evenly distributed load
21. Point Load - Applied at point
22. Line Load - Applied along line
23. Area Load - Applied over area
24. Reaction - Support response
25. Axial Force - Force along member axis
26. Shear Force - Perpendicular force
27. Bending Moment - Rotational force
28. Torsion - Twisting force
29. Compression - Squeezing force
30. Tension - Stretching force
31. Stress - Force per area
32. Strain - Deformation per length
33. Deflection - Bending displacement
34. Deformation - Shape change
35. Displacement - Position change
36. Rotation - Angular displacement
37. Stiffness - Resistance to deformation
38. Flexibility - Ease of deformation
39. Elasticity - Ability to return to shape
40. Plasticity - Permanent deformation
41. Ductility - Ability to deform before failure
42. Brittleness - Sudden failure
43. Yield - Beginning of permanent deformation
44. Ultimate Strength - Maximum load capacity
45. Buckling - Compression instability
46. Slenderness - Length to thickness ratio
47. Span - Distance between supports
48. Clear Span - Unobstructed span
49. Cantilever - Unsupported end
50. Beam - Horizontal member
51. Column - Vertical member
52. Wall - Vertical plane element
53. Slab - Horizontal plane element
54. Plate - Thin plane element
55. Shell - Curved surface
56. Frame - Structural skeleton
57. Truss - Triangular framework
58. Arch - Curved compression structure
59. Dome - Curved roof structure
60. Cable - Tension member
61. Tension Member - Carrying tension
62. Compression Member - Carrying compression
63. Axial Member - Carrying axial force
64. Flexural Member - Carrying bending
65. Shear Wall - Resisting lateral forces
66. Bracing - Lateral support
67. Diagonal Bracing - Diagonal support
68. Cross Bracing - X-shaped support
69. K-Bracing - K-shaped support
70. V-Bracing - V-shaped support
71. Moment Frame - Rigid frame
72. Rigid Frame - Joint rigidity
73. Pin Connection - Rotation-free connection
74. Fixed Connection - Restrained connection
75. Simple Support - Roll/rotation free
76. Fixed Support - Fully restrained
77. Roller Support - One degree free
78. Hinge - Pin connection
79. Joint - Member connection
80. Connection - Member joining
81. Splice - Member extension
82. Weld - Fusion connection
83. Bolt - Threaded fastener
84. Rivet - Permanent fastener
85. Anchor - Holding connection
86. Reinforcement - Strengthening addition
87. Reinforcing Steel - Tension reinforcement
88. Rebar - Reinforcing bar
89. Stirrup - Shear reinforcement
90. Concrete - Cementitious material
91. Cement - Binding material
92. Aggregate - Inert filler
93. Fine Aggregate - Sand
94. Coarse Aggregate - Gravel
95. Admixture - Chemical additive
96. Water-Cement Ratio - Water to cement ratio
97. Curing - Moisture retention
98. Hydration - Chemical hardening
99. Compressive Strength - Resistance to compression
100. Tensile Strength - Resistance to tension
101. Flexural Strength - Resistance to bending
102. Modulus of Elasticity - Stress-strain ratio
103. Creep - Time-dependent deformation
104. Shrinkage - Volume reduction
105. Steel - Iron-carbon alloy
106. Structural Steel - Construction steel
107. Carbon Steel - Iron-carbon alloy
108. Stainless Steel - Corrosion-resistant steel
109. Aluminum - Lightweight metal
110. Timber - Construction wood
111. Masonry - Brick/block construction
112. Concrete Masonry Unit (CMU) - Concrete block
113. Brick - Clay block
114. Precast - Factory-made elements
115. Cast-in-Place - Site-cast elements
116. Prestressed - Pre-compressed concrete
117. Post-tensioned - Post-compression
118. Composite - Combined materials
119. Composite Beam - Steel-concrete beam
120. Composite Slab - Steel-concrete slab

---

## Integration Guide

```python
def extract_structure_specs(contract_text):
    """
    Extract structural specifications
    """
    specs = {
        'structure_type': extract_value(contract_text, r'(frame|truss|arch|wall)'),
        'materials': extract_values(contract_text, r'(concrete|steel|timber|masonry)'),
        'concrete_grade': extract_value(contract_text, r'C(\d{2})/\d{2}'),
        'steel_grade': extract_value(contract_text, r'S(\d{3})'),
        'floor_system': extract_value(contract_text, r'(flat slab|ribbed slab|waffle slab|precast)')
    }
    return specs
```

---

**Research Story RS-18: COMPLETE**