from fitparse import *
from pandas import *



try:
    fitfile = FitFile('data/raw/ACTIVITY/A2OJ1736.FIT')
    fitfile.parse()
except FitParseError as e:
    print("Error while parsing .FIT file: %s" % e)
    sys.exit(1)


df = DataFrame()


'''

for header in headers:
    if header in df.columns:
        pass
    elif header is not df.count:
        df[header] = None

df.info()
'''

class create_df:
    def list_headers(fitfile):
        headers_list = []
        for record in fitfile.get_messages():
            headers_list.append("type")
            for record_data in record:
                headers_list.append(record_data.name)
        return headers_list

headers = create_df.list_headers(fitfile)
print(len(headers))

    # Go through all the data entries in this record
    #for record_data in record:
        #print(count)
        #count += 1
        # Print the records name and value (and units if it has any)
        #if record_data.units:
            #print(" * {}: {} {}".format(record_data.name, record_data.value, record_data.units))
        #else:
            #print(" * {}: {}".format(record_data.name, record_data.value))

            #'''