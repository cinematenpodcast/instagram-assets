import os

# Define the file to be deleted and the new name
file_to_delete = 'written_article.md'
new_name = 'written_article.md'

# Delete the file if it exists
if os.path.exists(file_to_delete):
	os.remove(file_to_delete)
	print(f"Deleted the file: {file_to_delete}")
else:
	print(f"No file named {file_to_delete} found.")

# Rename the first .md file found
for file in os.listdir('.'):
	if file.endswith('.md') and file != new_name:
		os.rename(file, new_name)
		print(f"Renamed {file} to {new_name}")
		break
else:
	print("No other .md files found to rename.")
