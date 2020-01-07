import datetime as dt
import json
import re
import requests
import pandas as pd
import numpy as np
import urllib3

from requests.auth import HTTPBasicAuth

from src.AesLib.DataEngineering import Azure

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getDatetimeAsString(timeStamp: dt.datetime.timestamp, stringFormat="%Y_%m_%d_%H_%M_%S") -> str:
    timeStampAsDateTime = dt.datetime.fromtimestamp(timeStamp / 1000)
    return timeStampAsDateTime.strftime(stringFormat)

def reduceDataFrameSize(dataFrame) -> pd.DataFrame:
    dataFrame.loc[:, dataFrame.select_dtypes(include=np.float64).columns] \
        = dataFrame.select_dtypes(include=np.float64).astype(np.float32)
    return dataFrame

def getBazefieldAuthenticationFromKeyVault(keyVaultName: str) -> HTTPBasicAuth:
    apiKey = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-api-key')
    return HTTPBasicAuth(apiKey, '')

def getBazefieldHeaders() -> dict:
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               'Accept': 'application/json, text/plain, */*'}
    return headers

def getFullTagListFromBazefield(keyVaultName: str):
    auth = getBazefieldAuthenticationFromKeyVault(keyVaultName)
    tagListUrl = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-tagid-url')
    tagList = requests.get(url=tagListUrl, verify=False, auth=auth)
    return json.loads(tagList.text)

def getTransformedTagListFromBazefield(keyVaultName: str):
    tagList = getFullTagListFromBazefield(keyVaultName)

    currentsReString = 'DOW-WFO-F000-33kV-30H\d{2}\+R01-H\d{2}-Feeder-(Current|Voltage|ActivePower)-*'
    turbinesReString = 'DOW-[a-zA-Z_]\d{2}-(StateRun|ActivePower|ActivePowerLimit|Current|Voltage|ReactivePower|NacelleDirection|WindSpeed|ActualWindDirection_mean|AmbientTemp|BladeAngle|BladeAngleRef)(U|V|W|$|A|B|C)'
    meteorologicalReString = 'DOW-F000-Met-THP-AirTemp$'



    tagIdsCurrents = [t["tagId"] for t in tagList
                      if re.match(currentsReString, t["tagName"])
                      and "IEC" not in t["tagName"]]
    tagIdsTurbines = [t["tagId"] for t in tagList
                      if re.match(turbinesReString, t["tagName"])]
    tagIdsMeteorological = [t["tagId"] for t in tagList
                            if re.match(meteorologicalReString, t["tagName"])]

    tagIds = tagIdsCurrents + tagIdsTurbines + tagIdsMeteorological

    data = {"tagIds": str(tagIds)[1:-1].replace(" ", "")}

    data['dateTimeFormat'] = "dd-MM-yyyy HH:mm:ss.fff"
    data["calenderUnit"] = "Minute"
    data["useAssetTitle"] = False
    data["useInterval"] = True
    return json.dumps(data)

def prepareDownload(fromTimeStamp: int,
                    keyVaultName: str,
                    downloadFileResolution=1000*3600*24):

    fromTimeStampAsString = getDatetimeAsString(fromTimeStamp)
    endTimeStamp = fromTimeStamp + downloadFileResolution

    print("Downloading " + fromTimeStampAsString)

    url = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-data-export-url')
    auth = getBazefieldAuthenticationFromKeyVault(keyVaultName)
    headers = getBazefieldHeaders()
    proxy = {'https': Azure.getSecretFromKeyVault(keyVaultName, secretName='equinor-proxy')}
    data = getTransformedTagListFromBazefield(keyVaultName)

    interval = '10'
    aggregates = 'End'

    res = requests.post(url=url.format(fromTimeStamp, endTimeStamp, interval, aggregates),
                        auth=auth,
                        headers=headers,
                        verify=False,
                        proxies=proxy,
                        data=data)

    filename = res.text
    nextTimeStamp = endTimeStamp

    return filename, nextTimeStamp, fromTimeStampAsString

def downloadFile(filename: str, fromTimeStampAsString: str, keyVaultName: str):
    csvName = fromTimeStampAsString + '.csv'
    filename = filename.replace(".txt", "")

    url = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-get-file-url')
    auth = getBazefieldAuthenticationFromKeyVault(keyVaultName)
    proxy = {'https': Azure.getSecretFromKeyVault(keyVaultName, secretName='equinor-proxy')}

    res = requests.get(url=url.format(filename),
                       auth=auth, verify=False, proxies=proxy)

    file = res.content.decode()

    destination = './Data/'
    filePath = destination + csvName

    with open(filePath, 'w') as f:
        f.write(file)
        print("Finished.")
        print("Downloaded to "+ str(filePath))

    dataFrame = pd.read_csv(filePath, sep=';')
    dataFrame = reduceDataFrameSize(dataFrame)

    dataFrame.to_csv(filePath, sep=';')

    return True


def downloadDataFromBazefieldAsCSV(fromTimeStamp: dt.datetime, toTimeStamp: dt.datetime):
    fromTimeStampInt = int(fromTimeStamp.timestamp()) * 1000
    toTimeStampInt = int(toTimeStamp.timestamp())

    keyVaultName = 'arnts-keyvault'

    while True:
        try:
            filename, nextTimeStamp, fromTimeStampAsString = prepareDownload(fromTimeStampInt,
                                                                             keyVaultName)
            print('Downloading ' + fromTimeStampAsString)
            print(filename)
            _ = downloadFile(filename, fromTimeStampAsString, keyVaultName)
        except Exception as e:
            print(e)
            fromTimeStampInt = nextTimeStamp
            continue
        
        if dt.datetime.fromtimestamp(nextTimeStamp / 1000) \
           > dt.datetime.fromtimestamp(toTimeStampInt):
            return
        else:
            fromTimeStampInt = nextTimeStamp


    
if __name__ == '__main__':
    fromTimeStamp = dt.datetime(year=2018, month=1, day=1)
    toTimeStamp = dt.datetime(year=2018, month=1, day=1)

    downloadDataFromBazefieldAsCSV(fromTimeStamp, toTimeStamp)
