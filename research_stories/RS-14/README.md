# Research Story RS-14: Carbon Calculation and ESG Clauses

## Glossary (60+ Terms)

1. Carbon Footprint - Total greenhouse gas emissions
2. Carbon Equivalent (CO2e) - Standardized carbon measure
3. Scope 1 Emissions - Direct emissions
4. Scope 2 Emissions - Indirect energy emissions
5. Scope 3 Emissions - Value chain emissions
6. Carbon Neutral - Net zero carbon
7. Net Zero - Net zero greenhouse gases
8. Carbon Offset - Compensating for emissions
9. Carbon Credit - Tradeable emission reduction
10. Carbon Trading - Buying/selling emissions
11. ESG - Environmental, Social, Governance
12. Sustainability Reporting - Environmental disclosure
13. GRI - Global Reporting Initiative
14. SASB - Sustainability Accounting Standards Board
15. TCFD - Task Force on Climate-related Financial Disclosures
16. CDP - Carbon Disclosure Project
17. GHG Protocol - Greenhouse Gas Protocol
18. Life Cycle Assessment (LCA) - Environmental impact analysis
19. Cradle-to-Grave - Full life cycle analysis
20. Cradle-to-Gate - Production to factory gate
21. Embodied Carbon - Carbon in materials
22. Operational Carbon - Carbon from operations
23. Carbon Sequestration - Storing carbon
24. Carbon Capture - Collecting carbon dioxide
25. Carbon Storage - Storing captured carbon
26. Renewable Energy - Sustainable power
27. Green Energy - Environmentally friendly energy
28. Clean Energy - Low-emission energy
29. Energy Efficiency - Minimizing energy waste
30. Circular Economy - Waste-reducing economy
31. Recycled Content - Reused materials
32. Reusable Materials - Multiple-use materials
33. Biodegradable - Naturally decomposing
34. Compostable - Decomposing into compost
35. Sustainable Sourcing - Environmentally responsible procurement
36. Supply Chain Transparency - Visible supply chain
37. Responsible Sourcing - Ethical procurement
38. Fair Trade - Ethical trading practices
39. Social Responsibility - Community obligations
40. Corporate Governance - Company management practices
41. Sustainability Goals - Environmental targets
42. Carbon Reduction Targets - Emission reduction goals
43. Science-Based Targets - Aligned with climate science
44. Paris Agreement - International climate agreement
45. SDGs - Sustainable Development Goals
46. Climate Risk - Climate-related threats
47. Climate Adaptation - Adjusting to climate
48. Climate Resilience - Withstanding climate change
49. ESG Rating - ESG performance score
50. ESG Index - ESG performance benchmark
51. ESG Audit - ESG performance review
52. Carbon Pricing - Cost of carbon emissions
53. Carbon Tax - Tax on emissions
54. Cap and Trade - Emission trading system
55. Green Bond - Financing green projects
56. Sustainability Loan - Green financing
57. ESG Investment - Ethical investing
58. Impact Investing - Social/environmental investing
59. Greenwashing - False environmental claims
60. ESG Compliance - Meeting ESG requirements

---

## Integration Guide

```python
def calculate_project_carbon_footprint(materials, operations):
    """
    Calculate project carbon footprint
    """
    embodied_carbon = sum(m['quantity'] * m['carbon_factor'] for m in materials)
    operational_carbon = sum(o['energy'] * o['carbon_factor'] for o in operations)

    total_carbon = embodied_carbon + operational_carbon

    return {
        'embodied_carbon_tonnes': embodied_carbon / 1000,
        'operational_carbon_tonnes': operational_carbon / 1000,
        'total_carbon_tonnes': total_carbon / 1000,
        'scopes': {
            'scope_1': operations['direct_emissions'],
            'scope_2': operations['indirect_emissions'],
            'scope_3': materials['supply_chain']
        }
    }
```

---

**Research Story RS-14: COMPLETE**