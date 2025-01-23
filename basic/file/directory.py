import os
import shutil
import tempfile

# 1. Create a directory
os.mkdir('example_dir')

# 2. Create nested directories
os.makedirs('example_dir/nested_dir')

# 3. List contents of a directory
print(os.listdir('example_dir'))

# 4. Change current working directory
os.chdir('example_dir')

# 5. Get current working directory
print(os.getcwd())

# 6. Remove a directory
os.rmdir('nested_dir')

# 7. Remove nested directories
os.chdir('..')
shutil.rmtree('example_dir')

# 8. Check if a directory exists
print(os.path.exists('example_dir'))

# 9. Rename a directory
os.mkdir('old_dir')
os.rename('old_dir', 'new_dir')

# 10. Copy a directory
shutil.copytree('new_dir', 'copied_dir')

# 11. Move a directory
shutil.move('copied_dir', 'moved_dir')

# 12. Get directory statistics
print(os.stat('new_dir'))

# 13. Walk through directory tree
for dirpath, dirnames, filenames in os.walk('new_dir'):
    print(f'Found directory: {dirpath}')
    for file_name in filenames:
        print(f'\t{file_name}')

# 14. Create a temporary directory
with tempfile.TemporaryDirectory() as tmpdirname:
    print('Created temporary directory:', tmpdirname)

# 15. Get absolute path of a directory
print(os.path.abspath('new_dir'))

# 16. Get directory name from a path
print(os.path.dirname('/path/to/some/file'))

# 17. Get base name from a path
print(os.path.basename('/path/to/some/file'))

# 18. Split a path into directory and file
print(os.path.split('/path/to/some/file'))

# 19. Join paths
print(os.path.join('example_dir', 'nested_dir'))

# 20. Check if a path is a directory
print(os.path.isdir('new_dir'))

# 21. Check if a path is a file
print(os.path.isfile('new_dir/some_file.txt'))