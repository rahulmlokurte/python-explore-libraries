from pathlib import Path
cwd = Path.cwd()
print(cwd)

home = Path.home()
print(home)

join_directory = Path.home() / 'Desktop' / 'pathlib-library' / 'test.py'
print(join_directory)

join_directory_using_join_path = Path.home().joinpath('Desktop', 'pathlib-library', 'test.py')
print(join_directory_using_join_path)


