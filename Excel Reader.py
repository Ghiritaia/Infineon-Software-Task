try:
    import xlrd, datetime
except ImportError as i:
    print("dependency could not be found:", i)

print("Small Excel Reader - Alex Ghiriti")

wb = None
path = ""


# function to check if the month given is valid
def check_input_month(month):
    try:
        if int(month) > 12 or int(month) < 1:
            return 0
    except ValueError:
        return 0
    return int(month)


# function to check if the given year is valid
def check_input_year(year):
    if len(year) != 4:
        return 0
    try:
        int(year)
    except ValueError:
        return 0
    return year[-1] + year[-2]


# converting the read param into a more workable list
def convert_param(param):
    ret_list = [param[0]]
    if len(param[2]) == 1:
        param[2] = '0' + param[2]
    date = param[1] + "-" + param[2]
    ret_list.append(date)
    return ret_list


# loop thqt waits for a excel file path. only full paths are accepted
while True:
    try:
        path = input("Please specify the path to the File (or 'quit' to exit the program): ")
        if path == "quit":
            break
        wb = xlrd.open_workbook(path)
        print("File accepted")
        break
    except:
        pass
    print("No file found at Location:", path)

# loop awainting the command tu sum up the given values
while wb is not None:
    command = input("awaiting command <skill> <year> <month>")
    if command == "quit":
        exit(0)
    param = command.split(" ")
    if len(param) != 3:
        print("[ERR] Number of Parameter invalid, should be 3. Given: ", len(param))
        continue
    sheet = wb.sheet_by_index(0)

    if check_input_month(param[2]) == 0:
        print("Invalid input for month!")
        continue
    elif check_input_year(param[1]) == 0:
        print("invalid input for year")
        continue

    working_param = convert_param(param)
    total = 0

    # logic that looks for the searched values
    # fist for loop looks at the skills column
    # if the red cell value is matching the given one the second for loop starts
    # the second for loop looks at the date and searches for the given one
    # if the given date is found the value from that skill at that date
    # the datetime conversion also happens here

    for i in range(sheet.nrows):
        if sheet.cell_value(i, 1) == working_param[0]:
            for j in range(sheet.ncols):
                try:
                    read_date = float(sheet.cell_value(0, j))
                except ValueError:
                    continue
                converted_date = datetime.datetime(*xlrd.xldate_as_tuple(read_date, wb.datemode))
                if working_param[1] in str(converted_date):
                    try:
                        total += float(sheet.cell_value(i, j))
                    except ValueError:
                        continue

    print("Sum: ", round(total, 2))
