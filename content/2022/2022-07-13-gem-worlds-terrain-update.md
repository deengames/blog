Title: Gem Worlds Terrain Update
Date: 2022-07-13
Category: Devlog
Tags: Gem Worlds

![demo screenshot](https://i.imgur.com/nRbaVgu.png)

Hello! I made lots of changes to Gem Worlds over the last couple of months, based on player feedback that the game could use more interesting interactions between things in-world.

Based on that, I added a few terrain types to the game; they generate in each world:

- Teleporters: previously existed, but now exist in every world
- Light Stars: they move back and forth, even through dirt tiles
- Receeding blocks traps: once you step on them, they pop up into walls for a few turns, then reset

I also added, then scrapped, a couple of terrain:

- Pipes, which move you from one spot to another (inspired by Supaplex's pipes)
- Conveyor belts, which constantly move everything on them

Conveyor belts added a lot of interesting dynamics to the game. Unfortunately, they also contributed a disproportionately huge amount of bugs. In the end, I scrapped them.

Meanwhile, they also exposed a huge performance issue, where moving caused a drop of ~130ms (roughly ten frames). Fixing this required ripping out and rewriting the main collision-detection system, which resulted in an explosion of bugs, and took way too many weeks to fix. Alhamdulillah, those are all fixed now.

I also added (again based on played feedback) keys and locks! In every 5th and 10th level of each world, the exit appears from the start, but lock blocks surround it; you need to find one (or three) keys to unlock them and exit.

I'm looking forward to shipping a new v0.5.0 demo soon inshaAllah, and getting (and integrating) more feedback and features into the game. When that ships, I would really appreciate it if you could give it a quick play-through, and let me know your thoughts.

