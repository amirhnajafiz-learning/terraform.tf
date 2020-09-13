import csv
import os


def dir_check(MAIN_DIR_PATH, MONTH_DIR_PATH):
    # this function checks the existance of directories
    if not os.path.exists(MAIN_DIR_PATH):
        os.mkdir(MAIN_DIR_PATH)
    if not os.path.exists(MAIN_DIR_PATH+MONTH_DIR_PATH):
         os.mkdir(MAIN_DIR_PATH+MONTH_DIR_PATH)


def create_csv(PATH, divisions, links, streams): # opening the csv output file
    with open(PATH, "w") as file:
        headers = ['Song', 'Artist', 'Download', 'View']
        # setting the headers of the file
        csv_writer = csv.DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()

        for i in range(0, len(divisions)): # a loop for managing the data
            division, link, stream = divisions[i], links[i], streams[i]
            csv_writer.writerow({
                'Song': division.strong.text,
                'Artist': division.span.text[3:],
                'Download': link.a["href"],
                'View': stream.text
                })
