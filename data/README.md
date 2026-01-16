# Data

This project uses publicly available data from the Sloan Digital Sky Survey (SDSS).

## Dataset
Stellar masses and effective radii will be obtained from published SDSS-based value-added catalogs commonly used in the literature.

## Acquisition
The data will be accessed via SDSS public query services or downloaded from the corresponding catalog release pages.

Raw data files are not stored in this repository.

## Column Definitions (NASA-Sloan Atlas)

The following NSA columns are used in this project:

- 'MSTAR'
   Total stellar mass (log10 solar masses).

- 'SERSIC_TH50'
   Half-light radius from Sersic fit (kpc), used as the galaxy size.

- 'Z' 
   Redshift, used to restrict the analysis to the local universe.

Optional diagnostics and quality checks:
- 'BA' - axis ratio
- 'SERSIC_N' - Sersic index