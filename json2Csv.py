import csv, json

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

jsonFile = open('jsonSample.json')
jsonData = json.load(jsonFile)
    
numberElementsList = (len(jsonData['result']['list']))
    
for row in range(numberElementsList):
    picture = jsonData['result']['list'][row]['pic']
    updateTime = jsonData['result']['list'][row]['update_time']
    attId = jsonData['result']['list'][row]['att_id']
    profileId = jsonData['result']['list'][row]['profile_id']
    title = jsonData['result']['list'][row]['summary'][0]
    company = jsonData['result']['list'][row]['summary'][1]
    city = jsonData['result']['list'][row]['summary'][2]
    category = jsonData['result']['list'][row]['summary'][3]
    
    #email = jsonData['result']['list'][row]['email']

    name = jsonData['result']['list'][row]['name']
        
    print('Row #' + str(row) + ' of ' + str(numberElementsList) + 
          ' added to CSV...')
    
    # removed 'email'. Some rows don't have this key
    # it gives KeyError
    # pending fix
    outputWriter.writerow([picture, updateTime, attId, profileId,
                           title, company, city, category, name])
outputFile.close()
jsonFile.close()
