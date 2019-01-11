import csv

matches_number = 10000


def crop_dataset(dataset, croppedDataset):
    with open(dataset, 'r') as file:
        pubg = file.read()
        pubg = pubg.split("\n")

        match_list = []
        matches = {}

        for row in pubg[1:]:
            if len(match_list) < matches_number:
                cols = row.split(",")
                match_id = cols[2]

                if match_id not in match_list:
                    match_list.append(match_id)

            else:
                break

        col_names = pubg[0].split(",")

        for row in pubg[1:]:
            cols = row.split(",")
            if len(cols) > 10:
                match_id = cols[2]
                if match_id in match_list:
                    key = match_id
                    try:
                        matches.setdefault(key, [])
                        if len(matches[key]) > 100:
                            break
                        else:
                            matches[key].append(row)

                    except:
                        pass


    with open(croppedDataset, mode='w') as file:
        fieldnames = col_names
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for match_key in matches:
            for row_cell in matches[match_key]:
                tmp_dict = {}
                for a in range(len(fieldnames)):
                        row = row_cell.split(',')

                        tmp_dict[fieldnames[a]] = row[a]

                writer.writerow(tmp_dict)


def crop_sample(sample, new_sample):
    with open(sample, 'r') as file:
        sample = file.read()
        sample = sample.split("\n")
        col_names = sample[0].split(",")
        sample = sample[1:188425]

    with open(new_sample, mode='w') as file:
        fieldnames = col_names
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row_cell in sample:
            tmp_dict = {}
            for a in range(len(fieldnames)):
                    row = row_cell.split(',')

                    tmp_dict[fieldnames[a]] = row[a]

            writer.writerow(tmp_dict)


#crop_sample("#", "#")
#crop_dataset("#", "#")
