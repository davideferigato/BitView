#!/usr/bin/env python3
"""Advanced validation of Minecraft world files."""

import os
import sys
import glob

def check_file_exists_and_non_empty(path, description):
    if not os.path.exists(path):
        print(f"❌ {description}: {path} not found")
        return False
    if os.path.getsize(path) == 0:
        print(f"❌ {description}: {path} is empty")
        return False
    print(f"✅ {description}: {path} exists and non-empty")
    return True

def main():
    base = "00-99_Display/world/BitView_00-99_Display"
    level_dat = os.path.join(base, "level.dat")
    ok = check_file_exists_and_non_empty(level_dat, "level.dat")

    region_dir = os.path.join(base, "region")
    if not os.path.isdir(region_dir):
        print(f"❌ Region directory missing: {region_dir}")
        sys.exit(1)
    mca_files = glob.glob(os.path.join(region_dir, "*.mca"))
    if not mca_files:
        print(f"❌ No .mca files found in {region_dir}")
        sys.exit(1)
    non_empty_mca = 0
    for mca in mca_files:
        if os.path.getsize(mca) > 0:
            non_empty_mca += 1
        else:
            print(f"⚠️ Warning: {mca} is empty (may be fine)")
    print(f"✅ {non_empty_mca} non-empty .mca files found in region folder")

    # Check playerdata for .dat_old files (warnings only)
    playerdata_dir = os.path.join(base, "playerdata")
    if os.path.isdir(playerdata_dir):
        old_files = glob.glob(os.path.join(playerdata_dir, "*.dat_old"))
        if old_files:
            for old in old_files:
                print(f"⚠️ Warning: old playerdata backup found: {old}")
        else:
            print("✅ No .dat_old files in playerdata")
    else:
        print("ℹ️ playerdata folder not present (no players yet)")

    # Final exit code
    if ok and non_empty_mca > 0:
        print("\n✅ World validation passed (all critical checks OK)")
        sys.exit(0)
    else:
        print("\n❌ World validation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
