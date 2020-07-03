Title: A Summary of Testing Your Game
Date: 2020-07-07
Category: Project Management
Tags: Planning, Testing

![2 unit tests, 0 integration tests](https://i.imgur.com/SvZiWS1.mp4)

# Why Test?

Of all the fun, interesting, exciting game development topics I could write about, I chose: testing.

Why?

Because testing is *essential* to shipping your game without bugs and without hours upon hours of manual effort. As we'll see shortly, there are well-known patterns and practices you can apply; some generic to softwre testing, and some specific to game testing. 

I discovered these practices after working more then a decade as a professional software developer, and applying them on and off for a decade as a hobbyist game developer. They take time, yes. They work, often and they're better (faster, more reliable, consistent) than manual testing.

# Overall Strategy

Your goal with software testing is to release your game at the highest possible quality: that means NO BUGS! Everything should work the way the designers intended, *without* us spending tons of manual hours play-testing the same parts over and over and over (yawn).

Your overall strategy needs to include the following categories:

- **Unit Testing:** So you know your methods/classes/scripts/objects work at a granular level.
- **System Testing:** Make sure cross-object workflows succeed, like "user last-shots an enemy and gets bonus gold." Sometimes called integration testing, functional testing, or end-to-end testing.
- **Exploratory Testing:** There's no substitute for playing your game and trying weird stuff. You'll find quirks and things that your automated tests won't catch.
- **Regression Testing:** Every bug you find and catch should be exploited by a unit test. If that test passes, it guarantees the bugs won't repeat.

Without these three, be prepared for lots of bugs and poor reviews! Above and beyond them, depending on your available time, skill, and interest, you may benefit from additional categories:

- **Balancing:** Write tests that make sure the game is balanced, e.g. each class has roughly the same DPS, or that dungeons generate with roughly the right progressive difficulty
- **Performance or Crash Testing:** Running previously-problematic code and making sure it's fast or doesn't crash. This includes running your game overnight to see if bad things happen.

I can't reasonably explain all those topics in a suitable depth without writing an essay. Hit me up [on Twitter](https://twitter.com/nightblade99) or [Discord](https://discord.gg/frKXYtG) if you want to discuss it further.

# Testing Process

