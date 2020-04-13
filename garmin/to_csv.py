from fitparse import *
from pandas import *
import os, fnmatch
import ntpath


class compile_list:
    #Returns a list of .FIT files that haven't already been converted using history log.txt file
    def find(pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result 

    def to_convert(path, find):
        to_convert = []
        already_csv = open(path,'r').read().splitlines()
        for fit_file_path in find:
            if ntpath.basename(fit_file_path) in already_csv:
                pass
            elif ntpath.basename(fit_file_path) not in already_csv:
                to_convert.append(fit_file_path)
        return to_convert


class export_csv:
    def output_path(filepath):
        path = r"{}".format(filepath[0]).split("/")
        path[path.index("raw")] = "converted"
        return "/".join(path)

    def update_log(filename):
        #update logs files
        already_csv = open("../data/converted/log.txt",'r').read().splitlines()
        already_csv.append(filename)
        with open("../data/converted/log.txt", 'w') as file_handler:
            for item in already_csv:
                file_handler.write(f"{item}\n")

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

    def export(filepath, output_path):
        try:
            fitfile = FitFile(filepath)
            fitfile.parse()
        except FitParseError as e:
            print("Error while parsing .FIT file: %s".format(e))
            sys.exit(1)
        df = DataFrame()
        export_csv.df_with_headers(export_csv.list_headers(fitfile), df)
        export_csv.data_entry(export_csv.list_headers(fitfile), df, fitfile)
        df.to_csv(output_path)
        export_csv.update_log()
        
        
if __name__ == "__main__":
    #l = compile_list.to_convert("../data/converted/log.txt", compile_list.find("*.FIT","../data/raw"))
    #export_csv.update_log("BLABLA")
    print(export_csv.output_path(compile_list.to_convert("../data/converted/log.txt", compile_list.find("*.FIT","../data/raw"))))