try {
	// Paths to your files
	var templatePsdPath = "/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/template.psd";
	var textFilePath = "/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/post_copy.txt";
	var exportPath = "/Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator/exports";

	// Function to read text from a file
	function readTextFile(filePath) {
		var file = new File(filePath);
		if (!file.exists) {
			throw "File not found: " + filePath;
		}
		file.open('r');
		var text = file.read();
		file.close();
		return text;
	}

	// Open template.psd
	var templatePsdFile = new File(templatePsdPath);
	if (!templatePsdFile.exists) {
		throw "Template PSD not found: " + templatePsdPath;
	}
	app.open(templatePsdFile);

	// Check if the active document is valid
	if (!app.activeDocument) {
		throw "No active document found.";
	}

	// Relink Smart Objects if needed
	var layers = app.activeDocument.layers;
	for (var i = 0; i < layers.length; i++) {
		if (layers[i].kind == LayerKind.SMARTOBJECT) {
			// Code to relink smart object goes here
			// Example: layers[i].smartObject.link = "new link";
		}
	}

	// Replace text in the 'content' layer
	var newText = readTextFile(textFilePath);
	var contentLayer = app.activeDocument.layers["content"];
	if (!contentLayer) {
		throw "Content layer not found.";
	}
	contentLayer.textItem.contents = newText;

	// Save the modified PSD
	var modifiedPsdFile = new File(exportPath + "/modified.psd");
	app.activeDocument.saveAs(modifiedPsdFile, new PhotoshopSaveOptions(), true, Extension.LOWERCASE);

	// Export as JPG
	var jpgFile = new File(exportPath + "/nieuws_post.jpg");
	var jpgSaveOptions = new JPEGSaveOptions();
	jpgSaveOptions.quality = 12;
	app.activeDocument.saveAs(jpgFile, jpgSaveOptions, true, Extension.LOWERCASE);

	// Close the template PSD without saving
	app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);

} catch (e) {
	alert("Error: " + e);
}
