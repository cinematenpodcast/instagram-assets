import applescript

def open_psd_and_run_jsx(psd_file_path, jsx_file_path):
	script = f'''
	tell application "Adobe Photoshop 2024"
		activate
		-- Convert POSIX path to Mac-style path for Photoshop
		set macPsdPath to POSIX file "{psd_file_path}" as text
		set macJsxPath to POSIX file "{jsx_file_path}" as text

		-- Open the PSD file
		open file macPsdPath

		-- Wait for Photoshop to open the file, adjust delay as needed
		delay 5

		-- Run the JSX script
		do javascript file macJsxPath
	end tell
	'''
	applescript.AppleScript(script).run()

# Paths to your PSD and JSX files
psd_file_path = '/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/template.psd'
jsx_file_path = '/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/edit_template.jsx'

# Run the function
open_psd_and_run_jsx(psd_file_path, jsx_file_path)
