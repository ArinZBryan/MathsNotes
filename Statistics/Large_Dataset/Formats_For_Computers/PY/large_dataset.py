from datetime import datetime

class WindSpeed:
    def __init__(self, knots : float, beaufort : str):
        self.knots = knots
        self.beaufort = beaufort

class WindDirection:
    def __init__(self, bearing : int, heading : str):
        self.bearing = bearing
        self.heading = heading

class SimpleData:
    def __init__(self, date : datetime.date, temperature : float, rainfall : float, pressure : float, wind_speed : WindSpeed):
        self.date = date
        self.wind_speed = wind_speed
        self.temperature = temperature
        self.pressure = pressure
        self.rainfall = rainfall

class CompleteData:
    def __init__(self,
        date : datetime.date, # yyyy-mm-dd
        temperature : float, # celsius
        rainfall : float, # mm
        sun_hours : float, #0-24
        wind_speed : WindSpeed, # knots / beaufort
        gust_speed : float, # knots
        humidity : float, #0-100
        cloud_cover : int, # 0-8
        visibility : float, #dam
        pressure : float, # hpa
        wind_direction : WindDirection, # bearing / heading
        gust_direction : WindDirection # bearing / heading
        ):

        self.date = date
        self.temperature = temperature
        self.rainfall = rainfall
        self.sun_hours = sun_hours
        self.wind_speed = wind_speed
        self.gust_speed = gust_speed
        self.humidity = humidity
        self.cloud_cover = cloud_cover
        self.visibility = visibility
        self.pressure = pressure
        self.wind_direction = wind_direction
        self.gust_direction = gust_direction

class Large_Dataset:
    def __get_data_from_csv(self, filename : str):
        # Open the CSV file
        input_file = open(filename, newline = "")
        lines = input_file.readlines()
        input_file.close()

        if len(lines[0].split(',')) == 15:
            #complex data
            dataLines = lines[1:]
            data = []
            for line in dataLines:
                args = line.split(',')
                date = datetime.strptime(args[0], '%d/%m/%Y').date()
                temperature = float(args[1])

                try:
                    rainfall = float(args[2])
                except ValueError:
                    rainfall = None
                

                try:
                    sun_hours = float(args[3])
                except ValueError:
                    sun_hours = None
                
                try: 
                    w_spd_kn = float(args[4])
                except ValueError:
                    w_spd_kn = None
                wind_speed = WindSpeed(w_spd_kn, args[5])
                
                try: 
                    gust_speed = float(args[6])
                except ValueError:
                    gust_speed = None

                humidity = float(args[7])
                cloud_cover = int(args[8])
                visibility = float(args[9])
                pressure = float(args[10])

                try:
                    w_dir_bearing = int(args[11])
                except ValueError:
                    w_dir_bearing = None
                
                wind_direction = WindDirection(w_dir_bearing, args[12])
                
                try:
                    gust_dir_bearing = int(args[13])
                except ValueError:
                    gust_dir_bearing = None
                gust_direction = WindDirection(gust_dir_bearing, args[14])
                
                
                data.append(CompleteData(date, temperature, rainfall, sun_hours, wind_speed, gust_speed, humidity, cloud_cover, visibility, pressure, wind_direction, gust_direction))
            return data
        elif len(lines[0].split(',')) == 6:
            #simple data
            dataLines = lines[1:]
            data = []
            for line in dataLines:
                args = line.split(',')
                date = datetime.strptime(args[0], '%d/%m/%Y').date()
                temperature = float(args[1])
                rainfall = float(args[2])
                pressure = float(args[3])
                wind_speed = WindSpeed(float(args[4]), args[5])
                data.append(SimpleData(date, temperature, rainfall, pressure, wind_speed))
            return data
        else:
            print(f'Unknown format on file {input_file.name}')
            return

    def __init__(self, rel_path_to_csvs : str):
        beijing_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/beijing_15.csv')
        beijing_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/beijing_87.csv')

        jacksonville_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/jacksonville_15.csv')
        jacksonville_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/jacksonville_87.csv')

        perth_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/perth_15.csv')
        perth_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/perth_87.csv')

        cambourne_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/cambourne_15.csv')
        cambourne_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/cambourne_87.csv')

        heathrow_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/heathrow_15.csv')
        heathrow_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/heathrow_87.csv')

        hurn_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/hurn_15.csv')
        hurn_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/hurn_87.csv')

        leeming_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/leeming_15.csv')
        leeming_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/leeming_87.csv')

        leuchars_15 = self.__get_data_from_csv(f'{rel_path_to_csvs}/leuchars_15.csv')
        leuchars_87 = self.__get_data_from_csv(f'{rel_path_to_csvs}/leuchars_87.csv')

        self.beijing = {15 : beijing_15, 87 : beijing_87}
        self.jacksonville = {15 : jacksonville_15, 87 : jacksonville_87}
        self.perth = {15 : perth_15, 87 : perth_87}
        self.cambourne = {15 : cambourne_15, 87 : cambourne_87}
        self.heathrow = {15 : heathrow_15, 87 : heathrow_87}
        self.hurn = {15 : hurn_15, 87 : hurn_87}
        self.leeming = {15 : leeming_15, 87 : leeming_87}
        self.leuchars = {15 : leuchars_15, 87 : leuchars_87}

