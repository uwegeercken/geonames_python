from feature import Feature
import time, logging

# program reads the geonames features file
# program converts string fields to integer or float where applicable
# program constructs additional fields from the source data
# program maps the code of the feature to its name from the feature code file
#
# result is stored in a dictionary hwere the key is the geonameid of the feature
# and the value is a feature class containing the processed of the rows.
#
# last update: uwe geercken - 2019-12-24
#

# function to read the feature codes file
def readFeatureCodesFile(filename):

    linecounter_feature_codes = 0

    # contains the feature code to name mapping
    feature_codes = {}

    # read the feature codes file into dictionary
    # will be mapped to the code of the feature
    logging.debug("processing feature codes file")
    feature_codes_file = open(filename, "r")
    for line in feature_codes_file.readlines():
        linecounter_feature_codes += 1
        # skip the header row
        if linecounter_feature_codes > 1:
            row = line.split("\t")
            feature_codes.update({row[0]: row[1]})
    feature_codes_file.close()
    return feature_codes

# function to process the geonames main file containing
# all geographical features
def readGeonamesFile(filename, feature_codes):
    linecounter = 0

    # contains the features from the file
    features = {}

    # contains the field names from the header row
    fields = {}

    # read the geonames file into dictionary
    logging.debug("processing geonames file")
    geonames_file = open(filename, "r")
    for line in geonames_file.readlines():
        linecounter += 1
        row = line.split("\t")
        # assign first row to the header
        if linecounter == 1:
            # dictionary of field names and their position - from the header row
            logging.debug("processing geonames file header row")
            for i in range(len(row)):
                # strip newline from the field name (last field)
                fields.update({row[i].strip(): i})
        else:
            # construct the feature object
            feature = Feature(fields, row)
            # lookup the name of corresponding to the feature code and class
            feature.featureName = feature_codes.get(feature.featureClassCode)
            features.update({feature.geonameid : feature})
    geonames_file.close()
    return features

def main():

    # configure logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    # file with geonames features
    filename = "/home/uwe/data/allCountries_2019-03-03_1000.txt"

    # file with feature code to name mappings
    filename_feature_codes = "/home/uwe/data/feature_codes.csv"

    # get the start time
    start_time = time.time()

    # feature codes for mapping codes to name
    feature_codes = readFeatureCodesFile(filename_feature_codes)

    # holds the processed rows
    features = readGeonamesFile(filename, feature_codes)

    # get total processing time
    processing_time = round(time.time() - start_time, 2)

    logging.info("processed file in " + str(processing_time) +" seconds. lines processed (incl. header): " + str(len(features)+1))


# run the main method
main()

