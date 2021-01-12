/*
 * Macro template to process multiple open images
 */

#@ File(label = "Output directory", style = "directory") output
#@ String(label = "Title contains") pattern

processOpenImages();

/*
 * Processes all open images. If an image matches the provided title
 * pattern, processImage() is executed.
 */
function processOpenImages() {
	n = nImages;
	setBatchMode(true);
	for (i=1; i<=n; i++) {
		selectImage(i);
		imageTitle = getTitle();
		imageId = getImageID();
		if (matches(imageTitle, "(.*)"+pattern+"(.*)"))
			processImage(imageTitle, imageId, output);
	}
	setBatchMode(false);
}

/*
 * Processes the currently active image. Use imageId parameter
 * to re-select the input image during processing.
 */
function processImage(imageTitle, imageId, output) {
setMinAndMax(400, 500);

run("8-bit");
setAutoThreshold("Default");
setThreshold(1, 255);
run("Convert to Mask");
run("Watershed");
run("Analyze Particles...", "size=200-Infinity pixel show=Outlines display clear include summarize in_situ");

	print("Processing: " + imageTitle);
	pathToOutputFile = output + File.separator + imageTitle + ".png";
	print("Saving to: " + pathToOutputFile);
}
