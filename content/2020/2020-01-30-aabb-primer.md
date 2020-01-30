Title: A Primer on AABB Collision Resolution
Date: 2020-01-30
Category: Technical
Tags: Physics

This blog post includes a discussion about AABB collision resolution: what it is and isn't, it's strengths and weaknesses, some common pitfalls, and how you can (hopefully) implement it in your low-level gaming tool of choice, if needed.

I learned all this (the second time) as part of adding fast/stable collision resolution to [Puffin](https://nightblade9.github.io/puffin), a fast, lightweight 2D game engine built on top of MonoGame.

## AABB, Collision Detection, and Collision Resolution

Some quick definitions to start:

- AABB (Axis Aligned Bounding Boxes) means two non-rotated boxes, that are aligned on one axis. In 2D, everything on the same "layer" or "z" is on the same axis; in 3D, it means your boxes are on the same plane.
- Collsiion detection means detecting if there is a collision (two AABBs overlapping) or will be a collision (eg. in 0.3s these two will start colliding).
- Collision resolution means resolving the collision. Broadly, there are two approaches to this: prevention or pre-collision resolution (stop just at the onset of collision when the two AABBs touch), and post-collision resolution (once two AABBs overlap, move them backward in time until they no longer overlap).

My approach to AABB uses pre-collision resolution, because it tends to be less complex and more stable.

## Pros and Cons of AABB

Why should you use AABB collision resolution? There are many other options, such as collision points, sphere/line collsion algorithms, polygons, etc.

The strengths of AABB include:

- It works well in most cases. Most games can do well enough with just bounding boxes on their entities.
- It's relatively simple to code (math-wise), because it's just boxes.
- It's quite cheap computationally (eg. doesn't have an expensive square-root calculation, unlike spherical checks)

However, it includes some drawbacks:

- It doesn't work with rotated boxes
- It doesn't work well with non-box shapes
- It requires extra work for it to work well with multi-entity collisions
- It's succeptible to "tunnelling" (high-speed objects move through solid objects because of their velocity)

If you can live with those limitations, I recommend AABB, primarily because it is computationally cheap (works well with a high number of colliding entities).

## Collision Resolution is Complex, like Physics

While AABB collision resolution is *relatively* easier to code, it doesn't mean it's *easy* to code. Many game frameworks don't include collision resolution, because this is part of the physics engine.

Read that again: it's often part of the *physics engine*. Physics engines are notoriously difficult to get right, and require lots of fiddling and corner-case evaluation. Even high-quality physics engines have limitations, such as tunneling.

It took me around 10 hours to discover all the caveats and get this to work right. And it works well, including with multi-entity collisions. Test thoroughly.

That said, my implementation includes a few bonus features:

- It's resistant to collision tunneling (but not impervious)
- It works with multiple objects colliding at the same time
- It allows an object to optionally "collide and slide" along the object it collides with

With that out of the way, let's dive into the actual theory of how to make a stable AABB resolution, and then some code.

## High-Level Description of AABB

AABB collision resolution works by looking at the X and Y component resolutions of your velocity. Simply put:

- Look at the distance `dx` to travel before we collide on the X-axis and `dy` for the Y-axis
- Divide these by your component X-velocity and Y-velocity respectively (`vx` and `vy`) to figure out how long before each axis collision takes place (`tx` and `ty`)
- Resolve the collision on the axis that collides first

![AABB sweep test with velocity](https://i.imgur.com/gCtzUeJ.png)

This excellent diagram (credit: LaroLaro on [GameDev.SE](https://gamedev.stackexchange.com/questions/28577/2d-aabb-vs-aabb-sweep-how-to-calculate-hit-normal)) shows a moving object (A) that will collide with a second object (B). Based on the component velocities, you can see from the projected A box that the faster collision will be on the Y-axis first.

Because collision resolution takes place on a single axis at a time, you may end up having to resolve the same collision multiple times to get a stable resolution. I find that running the collision resolution twice suffices.

