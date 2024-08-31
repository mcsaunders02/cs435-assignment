This program uses the xml.etree.ElementTree and the PIL libraries for Python 3. Use `python3 -m pip install --upgrade Pillow` to install PIL. 

To run the program, place the extracted Programming-Assignment-Data folder in the same folder as `main.py`, and run `python3 main.py`. It will produce an Output directory containing the annotated screenshots.

You may need to open up `Programming-Assignment-Data/Programming-Assignment-Data/com.apalon.ringtones.xml` and add another `</node>` closing tag after line 18, otherwise the program won't work because the XML is malformed.

For the natural language description, check `description.txt`.