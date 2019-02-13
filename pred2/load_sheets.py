import pandas as pd
import os


def main():
    # List of studies to parse
    studies = os.listdir('..\sources')

    headers = ['site_name', 'start_year', 'start_month', 'start_day', 'end_year', 'end_month', 'end_date',
              'approximate_dates', 'spatial_extent_unit', 'spatial_extent_value', 'pulse_disturbance',
              'pulse_intensity', 'land_use', 'source_habitat_description', 'land_use_intensity',
              'managed_for_biodiversity', 'habitat_patch_area_unit', 'habitat_patch_area_value',
              'restoration_type', 'ff1', 'ff2', 'ff3', 'aes', 'organic', 'crop', 'fragmentation_layout',
               'study_text_id']

    df = pd.DataFrame(columns=headers)

    for study in studies:
        print(study)
        df = df.append(read(study))

    df.to_csv('merged_ph.csv', encoding='utf-8')


def read(filename):

    headers = ['site_name', 'start_year', 'start_month', 'start_day', 'end_year', 'end_month', 'end_date',
               'approximate_dates', 'spatial_extent_unit', 'spatial_extent_value', 'pulse_disturbance',
               'pulse_intensity', 'land_use', 'source_habitat_description', 'land_use_intensity',
               'managed_for_biodiversity', 'habitat_patch_area_unit', 'habitat_patch_area_value',
               'restoration_type', 'ff1', 'ff2', 'ff3', 'aes', 'organic', 'crop', 'fragmentation_layout']

    # Read in, ignoring unwanted rows and cols
    df = pd.read_excel(f'..\\sources\\{filename}', sheet_name='PressureHistory', names=headers, skiprows=4,
                       usecols=25, na_values=['No records', 'SELECT ONE', '-1'])

    # Truncate where data stops
    df.dropna(how='all', inplace=True)
    df['study_text_id'] = filename.replace('.xlsm', '')

    return df


if __name__ == '__main__':
    main()
