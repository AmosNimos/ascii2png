<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>ascii2png</title>
</head>
<body>
	<h1>ascii2png</h1>
	<p>A command line tool for converting ASCII art to PNG images.</p>
	<h2>Author</h2>
	<p>Author: amosnimos</p>
	<h2>Date</h2>
	<p>Date: Mon 10 Apr 2023 08:05:09 PM EDT</p>
	<h2>Usage</h2>
	<p>Usage: python ascii_to_image.py &lt;ascii_file&gt; &lt;output_file&gt; [OPTIONS]</p>
	<h2>Options</h2>
	<ul>
		<li>-f, --font-size&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Font size of the text (default: 14)</li>
		<li>-t, --font-type&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Font type of the text (default: LiberationMono-Regular.ttf)</li>
		<li>-c, --text-color&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text color in RGB format (default: 255 255 255)</li>
		<li>-b, --bg-color&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Background color in RGB format (default: 0 0 0)</li>
		<li>-h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show help message and exit</li>
	</ul>
	<h2>Examples</h2>
	<ul>
		<li>Convert ASCII art to image with default options:</li>
		<p>python ascii_to_image.py my_ascii_art.txt my_image.png</p>
		<li>Convert ASCII art to image with custom font size and text color:</li>
		<p>python ascii_to_image.py my_ascii_art.txt my_image.png -f 20 -c 255 0 0</p>
	</ul>
</body>
</html>
