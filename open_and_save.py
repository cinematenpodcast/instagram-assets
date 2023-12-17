import applescript

def run_photoshop_action(action_set, action_name):
	script = f'''
	tell application "Adobe Photoshop 2024"
		activate
		do action "{action_name}" from "{action_set}"
	end tell
	'''
	applescript.AppleScript(script).run()

# Replace with the actual names and path
run_photoshop_action('Default Actions', 'Open_and_save')
