# java2uml

This script converts java files to UML diagrams.  Relationships parsed include:

  * extends
  * implements
  * uses

Usage Example:

 sudo python3 java2uml.py .
 
When done, copy to your graphviz folder and do:

dot -Tpng output.gv -Tpng -Gsize=4000,4000\! > output.png

to generate the bitmap for viewing.
