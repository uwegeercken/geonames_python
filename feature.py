class Feature:
    def __init__(self, fields, row):
        self.geonameid = int(row[fields['geonameid']])
        self.name = row[fields['name']]
        self.asciiname = row[fields['asciiname']]
        self.alternatenames = row[fields['alternatenames']]
        try:
            self.latitude = float(row[fields['latitude']])
        except ValueError:
            self.latitude = None
        try:
            self.longitude = float(row[fields['longitude']])
        except ValueError:
            self.longitude = None
        self.featureClass = row[fields['feature_class']]
        self.featureCode = row[fields['feature_code']]
        # feature class code is not part of the row but concatenated from the fields
        self.featureClassCode = self.featureClass + "." + self.featureCode
        # name will be determined later - not part of the row
        self.featureName = None
        self.countryCode = row[fields['country_code']]
        self.cc2 = row[fields['cc2']]
        self.admin1Code = row[fields['admin1_code']]
        self.admin2Code = row[fields['admin2_code']]
        self.admin3Code = row[fields['admin3_code']]
        self.admin4Code = row[fields['admin4_code']]
        try:
            self.population = int(row[fields['population']])
        except ValueError:
            self.population = None
        try:
            self.elevation = int(row[fields['elevation']])
        except ValueError:
            self.elevation = None
        self.dem = row[fields['dem']]
        self.timezone = row[fields['timezone']]
        # strip newline from the field - because it's the last field
        self.modificationDate = row[fields['modification_date']].strip()

    @property
    def geonameid(self):
        return self.__geonameid

    @geonameid.setter
    def geonameid(self,value):
        self.__geonameid = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def asciiname(self):
        return self.__asciiname

    @asciiname.setter
    def asciiname(self, value):
        self.__asciiname = value

    @property
    def alternatenames(self):
        return self.__alternatenames

    @alternatenames.setter
    def alternatenames(self,value):
        self.__alternatenames = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self,value):
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self,value):
        self.__longitude = value

    @property
    def featureClass(self):
        return self.__featureClass

    @featureClass.setter
    def featureClass(self,value):
        self.__featureClass = value

    @property
    def featureCode(self):
        return self.__featureCode

    @featureCode.setter
    def featureCode(self,value):
        self.__featureCode = value

    @property
    def featureClassCode(self):
        return self.__featureClassCode

    @featureClassCode.setter
    def featureClassCode(self, value):
        self.__featureClassCode = value

    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self,value):
        self.__featureName = value

    @property
    def countryCode(self):
        return self.__countryCode

    @countryCode.setter
    def countryCode(self,value):
        self.__countryCode = value

    @property
    def cc2(self):
        return self.__cc2

    @cc2.setter
    def cc2(self,value):
        self.__cc2 = value

    @property
    def admin1Code(self):
        return self.__admin1Code

    @admin1Code.setter
    def admin1Code(self,value):
        self.__admin1Code = value

    @property
    def admin2Code(self):
        return self.__admin2Code

    @admin2Code.setter
    def admin2Code(self,value):
        self.__admin2Code = value

    @property
    def admin3Code(self):
        return self.__admin3Code

    @admin3Code.setter
    def admin3Code(self,value):
        self.__admin3Code = value

    @property
    def admin4Code(self):
        return self.__admin4Code

    @admin4Code.setter
    def admin4Code(self,value):
        self.__admin4Code = value

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self,value):
        self.__population = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self,value):
        self.__elevation = value

    @property
    def dem(self):
        return self.__dem

    @dem.setter
    def dem(self,value):
        self.__dem = value

    @property
    def timezone(self):
        return self.__timezone

    @timezone.setter
    def timezone(self,value):
        self.__timezone = value

    @property
    def modificationDate(self):
        return self.__modificationDate

    @modificationDate.setter
    def modificationDate(self,value):
        self.__modificationDate = value
