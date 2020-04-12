from fitparse import FitFile


fitfile = FitFile('data/ACTIVITY/A2OJ1736.FIT')

# Get all data messages that are of type record
for record in fitfile.get_messages('unknown_22'):#'record'):
    # Go through all the data entries in this record
    for record_data in record:
        # Print the records name and value (and units if it has any)
        if record_data.units:
            print(" * {}: {} {}".format(record_data.name, record_data.value, record_data.units))
        else:
            print(" * {}: {}".format(record_data.name, record_data.value))