# Galaxy Scaling Relations from Public Survey Data

## Abstract
This project presents a reproducible analysis of galaxy scaling relations using publicly available survey data. 
The primary focus is on understanding the stellar mass–size relation and investigating the physical origin of scatter in the global relation.

By separating galaxies based on structural properties (Sérsic index), we demonstrate that galaxy morphology plays a dominant role in organizing scaling behavior.

This work is part of my preparation for PhD research in galaxy evolution and observational astrophysics.

---

## Scientific Motivation

Scaling relations encode fundamental information about galaxy formation and evolution.

The stellar mass–size relation reflects:

- Angular momentum acquisition
- Dissipative vs non-dissipative growth
- Structural transformation processes

A single global relation exhibits significant scatter.  
This project investigates whether structural classification explains that scatter.

---

## Data

- NASA-Sloan Atlas (NSA)
- Low-redshift galaxies (z < 0.15)
- Structural parameters (Sérsic index)
- Stellar masses and half-light radii

---

## Methodology

1. Data cleaning and redshift sanity checks
2. Log-space regression analysis
3. Structural separation:
   - Disk-dominated galaxies (low Sérsic index)
   - Bulge-dominated galaxies (high Sérsic index)
4. Linear fits in log(M*) – log(Re)
5. Scatter comparison

All steps are reproducible via the provided scripts.

---

## Key Results

- The global mass–size relation shows large intrinsic scatter.
- When separated by morphology:
  - Disk galaxies follow a shallow slope.
  - Bulge-dominated systems follow a steeper relation.
- Structural classification significantly reduces observed scatter.

This supports the interpretation that galaxy structure is a primary driver of scaling relations.

---

## Reproducibility

To reproduce the analysis:

```bash
git clone https://github.com/gnaneshwar46/galaxy-scaling-relations
cd galaxy-scaling-relations
pip install -r requirements.txt
python main.py

---

## Author

Gnaneshwar G S  
Physics Graduate | Aspiring PhD in Astrophysics  
Research Interests: Galaxy evolution, SMBH–host galaxy co-evolution, observational survey analysis  

