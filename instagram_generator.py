import subprocess
import time
import os

# Define file paths
image_path = "/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/assets"
text_path = "/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/post_copy.txt"
figma_file_path = "/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/template.fig"

# GitHub repository details
github_repo_url = "https://github.com/cinematenpodcast/instagram-assets.git"
github_username = "cinematenpodcast"
repository_name = "instagram-assets"
branch_name = "main"  # replace with your branch name if different

# Function to run shell commands
def run_command(command):
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	if process.returncode != 0:
		return stderr.decode().strip()
	return stdout.decode().strip()

# Function to push files to GitHub
def push_files_to_github():
	# Copy the files to the repository
	run_command(f"cp '{image_path}' .")
	run_command(f"cp '{text_path}' .")
	run_command(f"cp '{figma_file_path}' .")

	# Git add, commit, and push
	run_command("git add .")
	run_command('git commit -m "Update files for Photopea processing"')
	push_result = run_command("git push")

	return push_result

# Function to construct GitHub raw content URLs
def construct_github_raw_urls():
	base_url = f"https://raw.githubusercontent.com/{github_username}/{repository_name}/{branch_name}/"
	image_url = os.path.join(base_url, os.path.basename(image_path))
	text_url = os.path.join(base_url, os.path.basename(text_path))
	figma_url = os.path.join(base_url, os.path.basename(figma_file_path))

	return image_url, text_url, figma_url

# Push files to GitHub
push_result = push_files_to_github()
print(push_result)

# Wait for a few seconds to ensure GitHub has processed the files
time.sleep(10)  # Adjust the time as needed

# Construct and print the URLs
image_url, text_url, figma_url = construct_github_raw_urls()
print("Image URL:", image_url)
print("Text URL:", text_url)
print("Figma File URL:", figma_url)

# Implement retry logic if URLs are not accessible
retry_count = 0
max_retries = 3
retry_delay = 10  # seconds
while retry_count < max_retries:
	# Check if URLs are accessible (implement your own check here)
	# If URLs are not accessible, wait and retry
	retry_count += 1
	time.sleep(retry_delay)
