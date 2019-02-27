from pathlib import Path

work_dir = Path(__file__).parent
relative_data_path = '../data'
zodiacs_en_filename = 'zodiacs_en.txt'
zodiacs_ru_filename = 'zodiacs_ru.txt'
zodiacs_en = (work_dir / relative_data_path / zodiacs_en_filename).resolve()
zodiacs_ru = (work_dir / relative_data_path / zodiacs_ru_filename).resolve()
