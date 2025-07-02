import exifread

def get_exif(path):
    with open(path, "rb") as file_handle:
        tags = exifread.process_file(file_handle)
    return tags

def get_data(data, key):
    return data.get(key)

def convert_to_decimal(coord, ref):
    degrees = float(coord[0])
    minutes = float(coord[1])
    seconds = float(coord[2]) if isinstance(coord[2], (int, float)) else eval(str(coord[2]))
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if ref in ['S', 'W']:
        decimal *= -1
    return decimal

def map_print(path):
    exif_info = get_exif(path)

    lat = get_data(exif_info, 'GPS GPSLatitude')
    lat_ref = get_data(exif_info, 'GPS GPSLatitudeRef')
    lon = get_data(exif_info, 'GPS GPSLongitude')
    lon_ref = get_data(exif_info, 'GPS GPSLongitudeRef')

    if lat and lat_ref and lon and lon_ref:
        lat_values = [float(x.num) / float(x.den) for x in lat.values]
        lon_values = [float(x.num) / float(x.den) for x in lon.values]

        lat_decimal = convert_to_decimal(lat_values, lat_ref.values)
        lon_decimal = convert_to_decimal(lon_values, lon_ref.values)

        print(f"Lat/Lon: ({lat_decimal:.5f}) / ({lon_decimal:.5f})")
    else:
        print("Coordonnées GPS non trouvées dans l'image.")
