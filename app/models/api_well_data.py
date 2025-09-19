class ApiWellData:
    # Operator, Status, Well Type, Work Type, Directional Status, Multi-Lateral, Mineral Owner, Surface Owner, Surface Location, GL Elevation, KB Elevation, DF Elevation, Single/Multiple Completion, Potash Waiver, Spud Date, Last Inspection, TVD (*), API, Latitude, Longitude, CRS (*)
    def __init__(self, operator, status, well_type, work_type, directional_status, multi_lateral, mineral_owner, surface_owner, surface_location, gl_elevation, kb_elevation, df_elevation, single_multiple_completion, potash_waiver, spud_date, last_inspection, tvd, api, latitude, longitude, crs):
        self.operator = operator
        self.status = status
        self.well_type = well_type
        self.work_type = work_type
        self.directional_status = directional_status
        self.multi_lateral = multi_lateral
        self.mineral_owner = mineral_owner
        self.surface_owner = surface_owner
        self.surface_location = surface_location
        self.gl_elevation = gl_elevation
        self.kb_elevation = kb_elevation
        self.df_elevation = df_elevation
        self.single_multiple_completion = single_multiple_completion
        self.potash_waiver = potash_waiver
        self.spud_date = spud_date
        self.last_inspection = last_inspection
        self.tvd = tvd
        self.api = api
        self.latitude = latitude
        self.longitude = longitude
        self.crs = crs

    def to_dict(self):
        return {
            "operator": self.operator,
            "status": self.status,
            "well_type": self.well_type,
            "work_type": self.work_type,
            "directional_status": self.directional_status,
            "multi_lateral": self.multi_lateral,
            "mineral_owner": self.mineral_owner,
            "surface_owner": self.surface_owner,
            "surface_location": self.surface_location,
            "gl_elevation": self.gl_elevation,
            "kb_elevation": self.kb_elevation,
            "df_elevation": self.df_elevation,
            "single_multiple_completion": self.single_multiple_completion,
            "potash_waiver": self.potash_waiver,
            "spud_date": self.spud_date,
            "last_inspection": self.last_inspection,
            "tvd": self.tvd,
            "api": self.api,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "crs": self.crs
        }