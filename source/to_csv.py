from fitparse import *
from pandas import *
import os, fnmatch
import ntpath


ntpath.basename("a/b/c")

try:
    fitfile = FitFile('data/raw/ACTIVITY/A2OJ1736.FIT')
    fitfile.parse()
except FitParseError as e:
    print("Error while parsing .FIT file: %s" % e)
    sys.exit(1)

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

class export_csv:
    def list_headers(fitfile):
        headers_list = []
        for record in fitfile.get_messages():
            headers_list.append("type")
            for record_data in record:
                headers_list.append(record_data.name)
        return headers_list

    def df_with_headers(list_headers, dataframe): 
        #Creates a Dataframe and enlists all the headers
        for header in list_headers:
            if header in df.columns:
                pass
            elif header is not df.count:
                dataframe[header] = None
        return 
    
    def data_entry(list_headers, dataframe, fitfile):
        #Enters Data into Dataframe
        count = 0 
        for record in fitfile.get_messages():
            dataframe.loc[count, "type"] = record.name
            for record_data in record:
                dataframe.loc[count, record_data.name] = record_data.value
            count += 1
        
if __name__ == "__main__":
    df = DataFrame()
    export_csv.df_with_headers(export_csv.list_headers(fitfile), df)
    export_csv.data_entry(export_csv.list_headers(fitfile), df, fitfile)
    df.to_csv('test.csv')