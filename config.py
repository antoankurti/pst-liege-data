# ROOT

from pathlib import Path

ROOT = Path(__file__).resolve().parent

# DOSSIERS

RAW_DIR = ROOT / "data" / "01 raw"
STAGING_DIR = ROOT / "data" / "02 staging"
DWH_DIR = ROOT / "data" / "03 dwh"

# DUCKDB  FILE

DUCKDB_FILE = DWH_DIR / "pst_liege.duckdb"


# POPULATION

POPULATION_COMMUNE_RAW = (RAW_DIR / "population/TF_SOC_POP_STRUCT_2025.txt")

POPULATION_SECTEUR_RAW = (RAW_DIR / "population/OPENDATA_SECTOREN_2025_NEW.txt")

SECTEURS_GEO_RAW =(RAW_DIR / "secteurs_geo/sh_statbel_statistical_sectors_3812_20250101.geojson")

MIGRATIONS_API =(https://spi-digitalwallonia.opendatasoft.com/api/explore/v2.1/catalog/datasets/migrations/records?limit=100)
                 