from fitparse import *
from pandas import *



try:
    fitfile = FitFile('data/raw/ACTIVITY/A2OJ1736.FIT')
    fitfile.parse()
except FitParseError as e:
    print("Error while parsing .FIT file: %s" % e)
    sys.exit(1)

df = DataFrame()


for record in fitfile.get_messages():#'record'):
    df
    print(record.name)
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