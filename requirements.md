
# This specifies the data structures, extensibility structure, and implementation requirements for this workbench

## **Required Data**

There are 3 types of data required. (1) Geometry data - the Freecad objects
created/modified by this workbench.
(2) Path workbench data - the data for the Path job created, and its commands, etc. Hopefully
this is  complete enough to be exported as gCode and used directly to create the specified box.
(3) Internal data. There is a considerable amount of data needed to be able
to manipulate the above 2 data classes. Some of it will be global, to be usable
by any box variant, while other is working data for the common implementation
algorithms.

## **Extensibility**

Extensibility is implemented by having a base class ("basevariant")
 which provides the public interface, and 1 derived class for each type of box which can be generated. It is possible that common utility methods
 will be implemented in a class at the same level as the basevariant class
 and imported for separation of responsibilities.

 A box generator will consist of the derived class for the code, and a folder which goes inside the resources folder, for the icons, etc. that it needs
 to function. Thus, the 'fancybox' generator will consist of boxvariants/fancybox.py and resources/fancybox.
