# This is a sample Python script.
import csv


def clean_csv(f_name):
    with open(f_name, 'r') as input:
        csv_reader = csv.reader(input, delimiter=',')
        with open("cleaned_pop_file.csv", 'w') as output:
            output.write("County, Population\n")
            line_count = 0
            for row in csv_reader:
                if line_count >= 5 and line_count < 3147:
                    county = row[0].split(',')[0]
                    county_removed = county.split('.')[1]
                    county_removed_final = county_removed.split(' ')[0]
                    output.write("\""+ county_removed_final + "\"" + "," + "\"" + row[1] + "\"\n")
                line_count += 1
        print(f'Processed {line_count} lines.')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clean_csv('all-pop-data-2.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
