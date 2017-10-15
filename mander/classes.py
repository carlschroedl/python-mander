from pandas import Series
from geopandas import GeoSeries, GeoDataFrame

class District:
    def __init__(self, geodata, total_votes=0, dem_votes=0, rep_votes=0):
        self.geo = geodata

        self.total_votes = int(total_votes)
        self.dem_votes = int(dem_votes)
        self.rep_votes = int(rep_votes)

        self.area = self.geo.area.sum()
        self.perimeter = self.geo.boundary.length.sum()

class Plan:
    def __init__(self, district_list):
        self.districts = Series(district_list)

    def get_districts(self):
        return self.districts

