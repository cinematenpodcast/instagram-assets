tell application "Adobe Photoshop 2024"
	activate
	do script "Replaced_placeholder" from "Default Actions"

	-- Read the contents of the JSX file into a string
	set jsxFilePath to "/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/edit_template.jsx"
	set fileHandle to open for access (POSIX file jsxFilePath as string)
	set jsxContent to read fileHandle
	close access fileHandle

	-- Run the JavaScript content
	do javascript jsxContent
end tell
