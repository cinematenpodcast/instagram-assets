import applescript

def quit_photoshop():
	script = '''
	tell application "Adobe Photoshop 2024" to quit
	'''
	applescript.AppleScript(script).run()

# Call the function to quit Photoshop
quit_photoshop()