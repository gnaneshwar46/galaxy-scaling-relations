"""
Load the NASA-Sloan Atlas (NSA) catalog from a local FITS file.

Expected columns :
- MSTAR
- SERSIC_TH50
- Z
- BA
- SERSIC_N
"""

from pathlib import Path

def load_nsa_catalog(fits_path):
    """
    Load the NSA FITS catalog.

    Parameters
    ----------
    fits_path : str or Path
        Path to the NSA FITS file.

    Returns
    -------
    table 
        Astropy Table containing NSA data.
    """
    raise NotImplementedError("NSA FITS loading not implemented yet.")

def main():
    data_path = Path("data")/ "nsa_catalog.fits"
    print(f"NSA catalog expected at: {data_path}")
    print("Data loading logic to be implemented.")

if __name__ == "__main__":
    main()