meta-id: 81a38d0c17fcd1d023de42d84e1a8605d652825d

meta-title: Pattern Warrior, Week 4: N-Back
meta-publishedOn: 2017-05-05
meta-tags: devlog

This week, we moved forward with Pattern Warrior. The goal is to create a small, polished web game that imrpoves players' memory as a side-effect of playing. (We walk the fine line of being "game"-like and not "memory-exercise" like.)

This week, we finalized the two modes of gameplay we wanted to prototype: listing items from memory, and n-back.

You can see the initial idea, regurgitating items from memory, using chunking:

![listing items screenshot](http://i.imgur.com/aznuqs8.gif)

While somewhat interesting to play, this game mode suffered from a critical flaw: [some research](https://bradylab.ucsd.edu/pdfs/BradyKonkleAlvarez2009.pdf) shows that, unless linked items are related to each other, chunking itself doesn't really benefit memory. In other words, teaching players to chunk items won't improve their memory.

Instead, we switched to a second prototype of a well-known memory-improvement technique called [n-back](https://en.wikipedia.org/wiki/N-back). In a nutshell, with n-back, you try to remember *N* (or in our case, all) previously-seen items.

![n-back screenshot](http://i.imgur.com/7fiMJD9.gif)

While more visually boring (we used letters here because it's quicker to prototype), this game mode held up much better after balance-tweaking than the memorize-these-lists gameplay.  After play-testing, it looks like this will make up the final gameplay.

Next week, the goal is to finalize the theme of the game (something that matches the core game loop), and add extra "gameification" features. (For these prototypes, we took the model of a simple one-on-one RPG-like battle.)