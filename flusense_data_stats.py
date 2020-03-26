from praatio import tgio
import os

def print_stats(duration_mp):

    duration_ls = [(y, x) for (x, y) in duration_mp.items()]

    duration_ls.sort()

    duration_ls.reverse()

    for labelStat in duration_ls:
        print("Label " + labelStat[1] + " ; Total duration: " + str(round(labelStat[0], 2)) + " seconds")

def main():

    original_folder = "flusense_data"

    files = os.listdir(original_folder)

    duration_mp = {}

    for file in files:

        if not file.endswith('.TextGrid'):
            continue

        full_path = os.path.join(original_folder, file)

        tg = tgio.openTextgrid(full_path)


        t_name = tg.tierNameList[0]

        entryList = tg.tierDict[t_name].entryList

        for entry in entryList:

            lab = entry.label

            if lab not in duration_mp:
                duration_mp[lab] = 0.0

            duration_mp[lab] += (entry.end - entry.start)

    print_stats(duration_mp)
if  __name__ == "__main__":
    main()