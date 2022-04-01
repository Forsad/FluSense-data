import os
import pandas as pd
from praatio import tgio


def print_stats(duration_mp):

    duration_ls = [(y, x) for (x, y) in duration_mp.items()]

    duration_ls.sort()

    duration_ls.reverse()

    for label_stat in duration_ls:
        print(
            "Label "
            + label_stat[1]
            + " ; Total duration: "
            + str(round(label_stat[0], 2))
            + " seconds"
        )


def main():

    original_folder = "flusense_data"

    files = os.listdir(original_folder)

    duration_mp = {}

    final_df = pd.DataFrame()

    for file in files:

        if not file.endswith(".TextGrid"):
            continue

        full_path = os.path.join(original_folder, file)

        tg_instance = tgio.openTextgrid(full_path)

        t_name = tg_instance.tierNameList[0]

        entry_list = tg_instance.tierDict[t_name].entryList

        data_frame = pd.DataFrame(entry_list)
        filename_df = pd.DataFrame(
            dict(filename=[file.split(".")[0] + ".wav"] * len(entry_list))
        )

        concatted = pd.concat([data_frame, filename_df], axis=1)
        final_df = pd.concat([final_df, concatted], ignore_index=True)

        for entry in entry_list:

            lab = entry.label

            if lab not in duration_mp:
                duration_mp[lab] = 0.0

            duration_mp[lab] += entry.end - entry.start

    print_stats(duration_mp)
    final_df.to_csv("metadata.csv", index=False)


if __name__ == "__main__":
    main()
