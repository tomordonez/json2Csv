# json2Csv

This is a JSON to CSV python script.

It has a JSON sample file and the result is `output.csv`.

## Usage

    $ git clone https://github.com/tomordonez/json2Csv.git
    $ cd json2Csv
    $ virtualenv -p /usr/bin/python3 env
    $ source env/bin/activate
    (env) $ python json2Csv.py

## Modifying the script

This script obviously doesn't work for any JSON file. See `jsonSample.json` for sample data and structure.

If you have your own JSON file. Review the data that you want to extract and modify the variables in the `for` loop to match that data.

## JSON to CSV in plain English

For experts. The script is not optimal. It just works. If you have advise on making improvements. Please send a message.

For newbies. Here is more info about this script:

    import csv, json

Importing the libraries for `csv` and `json`.

    outputFile = open('output.csv', 'w', newline='')

Open the `output.csv` file in write mode. Without using the `newline=''` it will add data in every other row. One row has data, the next is an empty row, the next data. Use `newline=''` to avoid this behavior. Then create an object `outputFile`.

    outputWriter = csv.writer(outputFile)

Create a `Writer` object. (You cannot pass a file name directly into the `csv.writer` function).

Something similar happens with opening the JSON file:

    jsonFile = open('jsonSample.json')
    jsonData = json.load(jsonFile)

Use `json.load` to open a JSON file. If you have seen `json.loads` with an `s` at the end. It means `load string`. That one is used when you are an opening a JSON string in this example:

    stringJson = '{"name": "Homer", "last": "Simpson"}'
    jsonData = json.loads(stringJson)

Use the following to calculate the number of elements on a list. For instance, the JSON sample has a list with 2 elements. This number will be used in the `for` loop to build the rows for the CSV file.

    numberElementsList = (len(jsonData['result']['list']))

Use a `for` loop to get each element on the list up to the total number of elements.

    picture = jsonData['result']['list'][row]['pic']

Then create variables for data extracted from an element.

    print('Row #' + str(row) + ' of ' + str(numberElementsList) + ' added to CSV...')

When you run the script it will print to the output something like:

    Row #1 of 2 added to CSV...

Then write the JSON data to the CSV Writer object:

    outputWriter.writerow([picture,...,name])

Then close both files JSON and CSV.

## Issues

I created a variable to capture the data `email`. But the program breaks when this key is not found on one of the elements of the list. I haven't fixed this so this line is commented out.

I tried a `try` and `except` around the `email` variable. And added the variable to `writerow`. When it tries to write the row. I get a:

    NameError: name 'email' is not defined

## Share/Comment

Tweet me at:

[Tom Ordonez](https://twitter.com/tomordonez)

Read my website:

[Data Science, Analytics, Growing Teams](https://www.tomordonez.com/)

Connect with me on:

[Linkedin](https://www.linkedin.com/in/tomordonez/)
