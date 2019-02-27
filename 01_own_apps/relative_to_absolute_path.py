from pathlib import Path

app_dir = Path.cwd().parent
# data_dir = Path.parent
print(app_dir)

relative_data_path = 'data'
data_path = (app_dir / relative_data_path).resolve()

print(data_path)
