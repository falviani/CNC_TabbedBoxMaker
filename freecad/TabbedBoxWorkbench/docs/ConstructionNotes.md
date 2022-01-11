# Construction Process Notes

## Choice of base components

It looks like there are 2 choices of component groups to use for constructing objects in the Sketcher:  


- The very fundamental classes in Base
- The classes in Part and PartGui

Most of the code fragments I see use the Part classes, so I will also.

## Class choices
Part.Vertex  (3D Vector instead?)

Part.LineSegment

Part.Edge

Part.Shape

Part.Feature ?? appears to be directly COIN related

??.constraint

## Construction outline

This appears to be the overall process to use, since most of my structures are rectangles or some variation on them. These are generally collected in lists, which are later iterated over as needed.

It looks like moving and rotating shapes is best done using the Draft workbench tools.

- Construct needed vertices
- Construct needed LineSegments from those vertices
- Construct edge from linesegments (?)
- Construct shape. (Add to document now or later??)
- Add constraints: coincident points
- Add constraints: vertical and horizontal
- Stock Placement:

	-- Move shape to position relative to active stock rectangle

	-- If shape is not totally enclosed within stock rectangle, can it be rotated to fit?

	-- If shape still can't fit:

		--- create new stock rectangle and move to a
		 location relative to last created rectangle.
		 This is now the 'active' stock rectangle

		--- Go through placement process again

## Path considerations
Need to have enum for inside/on/outside path alignment specification.

Need **user setting** for grouping paths **per stock piece**:

- All plates in a single job (1 body per stock piece, multiple plates)

- One job per plate. (1 body per plate)

Use may want to do 1 plate / job as a test, then switch to all plates / 1 job for 'production'. This implies the ability to save a setup. If the user does change this it will be necessary to re-layout the geometry completely.

Use dogbone dressup should be user choice (default on). Applies to all plates.

In globals, **add a setting** for "fit tolerance". Range 0.0 - 1.0 mm (inclusive). At 0, shape is set for exact fit (a tight press fit), while larger values make the fit of tab into slot looser. Default probably 0.1, so there's a very small amount of slop.

For stock rectangle, in globals **add a user setting** for a margin, range 0-10mm. Default is 0. This is an inset from the physical outline of the stock, so no plate will intersect it. Origin of paths will still be at 0,0,0 regardless of margin.****
