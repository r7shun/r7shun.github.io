---
title: Computer Assisted Surgery
tags: Lecture-notes
status: ongoing
---

## Morphology

Opening: Erosion + Dilation  (with the same structuring element)
    - the opening of A by B is the union of all translations of B that it entirely within A
    - **idempotent**: repeated operations has no further effects
    - somewhat like erosion in that it tends to remove some of the foreground(bright) pixels from the edges of the regions of foreground pixels. However it is *less destructive than erosion* in general.

Closing: Dilation + Erosion  (with the same structuing element)
    - the closing of A by B is the complement f union of all translations of B that do not overlap A
    - idempotent
    - similar in some ways to dilation in that it tends to enlarge the boundaries of foreground(bright) regions in an image(and shrink background color holes in such regions), but it is less destructive of the original boundary shape.


Opening is the dual of closing, i.e. opening the foreground pixels with a particular structuring element is equivalent to closing the background pixels with the same element.