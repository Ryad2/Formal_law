# batch_utils.py

import os
import pandas as pd


def get_valid_pairs(root_folder):
    """
    Scan subfolders and return valid MIDI pairs.
    Only folders with exactly 2 MIDI files are used.
    """
    pairs = []

    for subfolder in sorted(os.listdir(root_folder)):
        subfolder_path = os.path.join(root_folder, subfolder)

        if not os.path.isdir(subfolder_path):
            continue

        midi_files = [f for f in os.listdir(subfolder_path) if f.endswith(".mid")]

        # Only accept exactly 2 files
        if len(midi_files) == 2:
            file1 = os.path.join(subfolder_path, midi_files[0])
            file2 = os.path.join(subfolder_path, midi_files[1])

            pairs.append((subfolder, file1, file2))
        else:
            print(f"⚠️ Skipping {subfolder}: contains {len(midi_files)} MIDI files")

    return pairs


def save_results(results, output_file):
    df = pd.DataFrame(results)
    df.to_excel(output_file, index=False)
    print(f"\n✅ Results saved to {output_file}")