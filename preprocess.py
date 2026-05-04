#!/usr/bin/env python3

def load_file(filename):
    data = {}
    with open(filename) as f:
        next(f)  #skip header
        for line in f:
            parts = line.strip().split("\t")
            probe = parts[0]
            value = parts[7]  #Assay_Normalized_Signal is last column
            try:
                data[probe] = float(value)
            except:
                continue
    return data


def main():

    #NOTE: use looping here instead of fixed paths
    f1 = load_file("../22118_project_data/GSM266996.txt")
    f2 = load_file("../22118_project_data/GSM266997.txt")
    f3 = load_file("../22118_project_data/GSM266998.txt")

    #keep only probes present in all files
    common = set(f1) & set(f2) & set(f3)

    #NOTE: added probe_id to the resultant data file
    with open("data.txt", "w") as out:
        out.write("Probe_ID\trep1\trep2\trep3\n")

        for probe in sorted(common):
            out.write(f"{probe}\t{f1[probe]}\t{f2[probe]}\t{f3[probe]}\n")

if __name__ == "__main__":
    main()