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
from astropy.table import Table

def load_nsa_catalog(fits_path):
    """
    Load the NSA FITS catalog.

    Parameters
    ----------
    fits_path : str or Path
        Path to the NSA FITS file.

    Returns
    -------
    table: astropy.table.Table
        NSA catalog table.
    """
    fits_path = Path(fits_path)
    if not fits_path.exists():
        raise FileNotFoundError("NSA FITS loading not implemented yet.")
    table = Table.read(fits_path, format = "fits")
    return table

def main():
    data_path = Path("data")/ "nsa_catalog.fits"
    print(f"Attempting to load NSA catalog from: {data_path}")

    table = load_nsa_catalog(data_path)
    print(f"Loaded NSA catalog with {len(table)} rows.")

if __name__ == "__main__":
   main()