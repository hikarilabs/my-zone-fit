import os
from pathlib import Path

class MyZoneFileProcessor:

    WORKOUT_HEADER = ''
    HR_HEADER = 'Time,hr'

    def __init__(self):
        pass

    def process(self, file_path: Path):
        try:
            with open(file = file_path, mode= "r") as f:
                lines = f.readlines()
                return lines[:2], lines[3:]
        except FileNotFoundError:
            raise(f"File not found at file path: {file_path}")
    
    def _validate_workout_header(self, workout_header):
        return MyZoneFileProcessor.WORKOUT_HEADER == workout_header

    def _validate_hr_header(self, hr_header):
        return MyZoneFileProcessor.HR_HEADER == hr_header



if __name__ == '__main__':

    file_processor = MyZoneFileProcessor()
    workout, hr = file_processor.process('data/MYZONE_Activity-13-01-2025.csv')

    print(workout)
    print(hr)

    
