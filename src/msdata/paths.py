from utils4plans.paths import StaticPaths

import pyprojroot


BASE_PATH = pyprojroot.find_root(pyprojroot.has_dir(".git"))
static_paths = StaticPaths("", BASE_PATH)


class DynamicPaths:
    msd_stats = static_paths.temp / "msd_stats"
    valid_ids_csv = msd_stats / "valid_ids.csv"
    case_data = static_paths.temp / "snakemake/0_50"
