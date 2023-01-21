import PY.large_dataset as ld
from datetime import datetime
import sqlite3

db="large_dataset.sqlite"

def main():

    large_dataset = ld.Large_Dataset()

    con = sqlite3.connect(db)
    cur = con.cursor()

    create_simple_table(con, cur, "beijing_15")
    fill_simple_table(con, cur, "beijing_15", large_dataset.beijing[15])
    create_simple_table(con, cur, "beijing_87")
    fill_simple_table(con, cur, "beijing_87", large_dataset.beijing[87])
    
    create_simple_table(con, cur, "jacksonville_15")
    fill_simple_table(con, cur, "jacksonville_15", large_dataset.jacksonville[15])
    create_simple_table(con, cur, "jacksonville_87")
    fill_simple_table(con, cur, "jacksonville_87", large_dataset.jacksonville[87])

    create_simple_table(con, cur, "perth_15")
    fill_simple_table(con, cur, "perth_15", large_dataset.perth[15])
    create_simple_table(con, cur, "perth_87")
    fill_simple_table(con, cur, "perth_87", large_dataset.perth[87])

    create_complex_table(con, cur, "cambourne_15")
    fill_complex_table(con, cur, "cambourne_15", large_dataset.cambourne[15])
    create_complex_table(con, cur, "cambourne_87")
    fill_complex_table(con, cur, "cambourne_87", large_dataset.cambourne[87])

    create_complex_table(con, cur, "heathrow_15")
    fill_complex_table(con, cur, "heathrow_15", large_dataset.heathrow[15])
    create_complex_table(con, cur, "heathrow_87")
    fill_complex_table(con, cur, "heathrow_87", large_dataset.heathrow[87])

    create_complex_table(con, cur, "hurn_15")
    fill_complex_table(con, cur, "hurn_15", large_dataset.hurn[15])
    create_complex_table(con, cur, "hurn_87")
    fill_complex_table(con, cur, "hurn_87", large_dataset.hurn[87])

    create_complex_table(con, cur, "leeming_15")
    fill_complex_table(con, cur, "leeming_15", large_dataset.leeming[15])
    create_complex_table(con, cur, "leeming_87")
    fill_complex_table(con, cur, "leeming_87", large_dataset.leeming[87])

    create_complex_table(con, cur, "leuchars_15")
    fill_complex_table(con, cur, "leuchars_15", large_dataset.leuchars[15])
    create_complex_table(con, cur, "leuchars_87")
    fill_complex_table(con, cur, "leuchars_87", large_dataset.leuchars[87])

    con.close()
    print("Done")

def create_simple_table(con, cur, name : str):
    cur.execute(f'DROP TABLE IF EXISTS {name}') # delete table if it already exists
    cur.execute(
        f'''
        CREATE TABLE "{name}" (  
        "date" TEXT NOT NULL,
        "wind_speed_knots" REAL,
        "wind_speed_beaufort" TEXT NOT NULL,
        "temperature" REAL,
        "rainfall" REAL,
        "pressure" REAL
        );
        '''
    ) 
    con.commit() #   commits the changes to the database

def create_complex_table(con, cur, name: str):
    cur.execute(f'DROP TABLE IF EXISTS {name}') # delete table if it already exists
    cur.execute(
        f'''
        CREATE TABLE "{name}" (
        "date" TEXT NOT NULL,
        "temperature" REAL,
        "rainfall" REAL,
        "sun_hours" REAL,
        "wind_speed_knots" REAL,
        "wind_speed_beaufort" TEXT NOT NULL,
        "gust_speed" REAL,
        "humidity" REAL,
        "cloud_cover" INTEGER,
        "visibility" REAL,
        "pressure" REAL,
        "wind_direction_bearing" REAL,
        "wind_direction_heading" TEXT NOT NULL,
        "gust_direction_bearing" REAL,
        "gust_direction_heading" TEXT NOT NULL
        );
        ''')
    con.commit()

def fill_simple_table(con, cur, name, data):
    for row in data:
        cur.execute(f'''
        INSERT INTO {name} (date, wind_speed_knots, wind_speed_beaufort, temperature, rainfall, pressure)
        VALUES ("{row.date.strftime("%Y-%m-%d")}", {row.wind_speed.knots}, "{row.wind_speed.beaufort}", {row.temperature}, {row.pressure}, {row.rainfall});
        ''')
    con.commit()

def fill_complex_table(con, cur, name, data):
    for row in data:
        values = f'"{row.date.strftime("%Y-%m-%d")}", {row.temperature}, {row.rainfall}, {row.sun_hours}, {row.wind_speed.knots}, "{row.wind_speed.beaufort}", {row.gust_speed}, {row.humidity}, {row.cloud_cover}, {row.visibility}, {row.pressure}, {row.wind_direction.heading}, "{row.wind_direction.bearing}", {row.gust_direction.heading}, "{row.gust_direction.bearing}"'
        cur.execute(f'''
        INSERT INTO {name} (date, temperature, rainfall, sun_hours, wind_speed_knots, wind_speed_beaufort, gust_speed, humidity, cloud_cover, visibility, pressure, wind_direction_bearing, wind_direction_heading, gust_direction_bearing, gust_direction_heading)
        VALUES ("{row.date.strftime("%Y-%m-%d")}", {row.temperature}, {row.rainfall if row.rainfall != None else "NULL" }, {row.sun_hours if row.sun_hours != None else "NULL"}, {row.wind_speed.knots if row.wind_speed.knots != None else "NULL"}, "{row.wind_speed.beaufort}", {row.gust_speed if row.gust_speed != None else "NULL"}, {row.humidity}, {row.cloud_cover}, {row.visibility}, {row.pressure}, {row.wind_direction.bearing if row.wind_direction.bearing != None else "Null"}, "{row.wind_direction.heading}", {row.gust_direction.bearing if row.gust_direction.bearing != None else "NULL"}, "{row.gust_direction.heading}");
        ''')
        con.commit()

if __name__ == "__main__":
    main()
