import sqlite3
from app.models.api_well_data import APIWellData


class APIWellDataRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS api_well_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operator TEXT,
                    status TEXT,
                    well_type TEXT,
                    work_type TEXT,
                    directional_status TEXT,
                    multi_lateral TEXT,
                    mineral_owner TEXT,
                    surface_owner TEXT,
                    surface_location TEXT,
                    gl_elevation REAL,
                    kb_elevation REAL,
                    df_elevation REAL,
                    single_multiple_completion TEXT,
                    potash_waiver TEXT,
                    spud_date TEXT,
                    last_inspection TEXT,
                    tvd REAL,
                    api TEXT UNIQUE,
                    latitude REAL,
                    longitude REAL,
                    crs TEXT
                )
            ''')
            conn.commit()

    def insert(self, api_well_data: APIWellData):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO api_well_data (
                    operator, status, well_type, work_type, directional_status,
                    multi_lateral, mineral_owner, surface_owner, surface_location,
                    gl_elevation, kb_elevation, df_elevation, single_multiple_completion,
                    potash_waiver, spud_date, last_inspection, tvd, api,
                    latitude, longitude, crs
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                api_well_data.operator, api_well_data.status, api_well_data.well_type,
                api_well_data.work_type, api_well_data.directional_status,
                api_well_data.multi_lateral, api_well_data.mineral_owner,
                api_well_data.surface_owner, api_well_data.surface_location,
                api_well_data.gl_elevation, api_well_data.kb_elevation,
                api_well_data.df_elevation, api_well_data.single_multiple_completion,
                api_well_data.potash_waiver, api_well_data.spud_date,
                api_well_data.last_inspection, api_well_data.tvd,
                api_well_data.api, api_well_data.latitude,
                api_well_data.longitude, api_well_data.crs
            ))
            conn.commit()

    def update(self, api_well_data: APIWellData):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE api_well_data
                SET operator = ?, status = ?, well_type = ?, work_type = ?,
                    directional_status = ?, multi_lateral = ?, mineral_owner = ?,
                    surface_owner = ?, surface_location = ?, gl_elevation = ?,
                    kb_elevation = ?, df_elevation = ?, single_multiple_completion = ?,
                    potash_waiver = ?, spud_date = ?, last_inspection = ?,
                    tvd = ?, latitude = ?, longitude = ?, crs = ?
                WHERE api = ?
            ''', (
                api_well_data.operator, api_well_data.status, api_well_data.well_type,
                api_well_data.work_type, api_well_data.directional_status,
                api_well_data.multi_lateral, api_well_data.mineral_owner,
                api_well_data.surface_owner, api_well_data.surface_location,
                api_well_data.gl_elevation, api_well_data.kb_elevation,
                api_well_data.df_elevation, api_well_data.single_multiple_completion,
                api_well_data.potash_waiver, api_well_data.spud_date,
                api_well_data.last_inspection, api_well_data.tvd,
                api_well_data.latitude, api_well_data.longitude,
                api_well_data.crs, api_well_data.api
            ))
            conn.commit()

    def get(self, filter_func=None):
        """
        ### Example usage:
        `repository = APIWellDataRepository("path/to/db")`

        ### Get all wells
        `all_wells = repository.get()`

        ### Get wells with specific API
        `wells = repository.get(lambda x: x.api == "30-045-35432")`

        ### Get wells by operator
        `wells = repository.get(lambda x: x.operator == "ACME Oil")`

        ### Get wells with elevation above 1000
        `wells = repository.get(lambda x: x.gl_elevation > 1000)`

        ### Multiple conditions
        `wells = repository.get(lambda x: x.operator == "ACME Oil" and x.status == "ACTIVE")`
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM api_well_data')
            rows = cursor.fetchall()

            # Convert rows to APIWellData objects
            # Fairly memory intensive for large datasets
            # TODO: Consider adding pagination.
            wells = [APIWellData(
                operator=row['operator'],
                status=row['status'],
                well_type=row['well_type'],
                work_type=row['work_type'],
                directional_status=row['directional_status'],
                multi_lateral=row['multi_lateral'],
                mineral_owner=row['mineral_owner'],
                surface_owner=row['surface_owner'],
                surface_location=row['surface_location'],
                gl_elevation=row['gl_elevation'],
                kb_elevation=row['kb_elevation'],
                df_elevation=row['df_elevation'],
                single_multiple_completion=row['single_multiple_completion'],
                potash_waiver=row['potash_waiver'],
                spud_date=row['spud_date'],
                last_inspection=row['last_inspection'],
                tvd=row['tvd'],
                api=row['api'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                crs=row['crs']
            ) for row in rows]

            # Apply filter if provided
            if filter_func:
                wells = list(filter(filter_func, wells))

            return wells

    def delete(self, filter_func):
        """
        Delete wells based on a filter function.

        ### Example usage:
        ```python
        # Delete a specific well by API
        repository.delete(lambda x: x.api == "30-045-35432")

        # Delete all wells by a specific operator
        repository.delete(lambda x: x.operator == "ACME Oil")

        # Delete wells matching multiple conditions
        repository.delete(lambda x: x.status == "ABANDONED" and x.tvd < 1000)
        ```

        Args:
            filter_func (callable): Required filter function to specify which wells to delete

        Returns:
            int: Number of records deleted
        """
        if not filter_func:
            raise ValueError(
                "Filter function is required. For deleting all records, use delete_all() instead.")

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            # Get wells matching the filter
            wells = self.get(filter_func)
            # Delete matching wells by their APIs
            apis = [well.api for well in wells]
            if apis:
                placeholders = ','.join('?' * len(apis))
                cursor.execute(
                    f'DELETE FROM api_well_data WHERE api IN ({placeholders})', apis)

            conn.commit()
            return cursor.rowcount

    def delete_all(self):
        """
        Deletes all wells from the database.

        ### WARNING: This is a destructive operation that cannot be undone.
        Make sure you have a backup before proceeding.

        Returns:
            int: Number of records deleted
        """
        user_input = input(
            "WARNING: This will delete ALL wells from the database. Type 'DELETE ALL' to confirm: ")
        if user_input != "DELETE ALL":
            print("Operation cancelled.")
            return 0

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM api_well_data')
            conn.commit()
            return cursor.rowcount
