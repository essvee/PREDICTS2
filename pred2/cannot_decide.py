import pandas as pd
import os


def main():
    # List of studies to parse
    studies = os.listdir('..\sources')

    # Read in, ignoring unwanted rows and cols
    df = pd.read_excel('..\sources\AD1_1999__Ohtsuka_ACI_1.xlsm', sheet_name='PressureHistory', skiprows=4,
                       usecols=25)

    # Rename headers
    header = {'Unnamed: 0': 'site_name',
              'YYYY': 'start_year',
              'MM': 'start_month',
              'DD': 'start_day',
              'YYYY.1': 'end_year',
              'MM.1': 'end_month',
              'DD.1': 'end_date',
              'Unnamed: 7': 'approximate_dates',
              'Unit': 'spatial_extent_unit',
              'Value': 'spatial_extent_value',
              'Unnamed: 10': 'pulse_disturbance',
              'Unnamed: 11': 'pulse_intensity',
              'Unnamed: 12': 'land_use',
              'Unnamed: 13': 'source_habitat_description',
              'Unnamed: 14': 'land_use_intensity',
              'Unnamed: 15': 'managed_for_biodiversity',
              'Unit.1': 'habitat_patch_area_unit',
              'Value.1': 'habitat_patch_area_value',
              'Unnamed: 18': 'restoration_type',
              'For agricultural sites only!': 'ff1',
              'For agricultural sites only!.1': 'ff2',
              'For agricultural sites only!.2': 'ff3',
              'For agricultural sites only!.3': 'aes',
              'For agricultural sites only!.4': 'organic',
              'For agricultural sites only!.5': 'crop',
              'Unnamed: 25': 'fragmentation_layout'}

    df.rename(columns=header, inplace=True)

    # Truncate where data stops
    df = df[df.site_name != 'No records']

    print(df)


if __name__ == '__main__':
    main()