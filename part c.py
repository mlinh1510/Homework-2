
def find(read_date):
    months = {"January": 1, "February": 2,  "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
              "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    try:
        year = read_date.split(",")[-1].strip()
        month = read_date.split(",")[0].split()[0]
        day = read_date.split(",")[0].split()[-1]
        mm = months[month]
        int(year)
        int(day)
        return str(mm) + "/" + day + "/" + year
    except ValueError:
        return


with open("inputDates.txt") as f:
    for j in f.readline():
        if j.strip() != "-1":
            res = find(j.strip())
            if res != "":
                with open("parsedDates.txt", 'w') as w:
                    w.write(res)
                    w.write("\n")
                    w.close()
f.close()
