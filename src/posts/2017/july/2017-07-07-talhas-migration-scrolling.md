meta-id: ebee115eb0f9d1cb93056fc3ef4afaa0e37e8283

meta-title: Talha's Migration, Week 1: Scrolling!
meta-publishedOn: 2017-07-07
meta-tags: devlog

![screenshot](http://i.imgur.com/zRW6Z6m.gif)

This week, we made major strides on our new infinite runner project, tentatively titled "Talha's Migration." We themed the game around a loggerhead sea turtle's migration from Japan to the western coast of America.

The screenshot above shows two things we implemented:

- An infinite scrolling ground
- The player constantly moves forward.

You can see that when we press the left arrow, the player slows, but still moves forward; when we press right, the player accelerates.

We spent a ton of time upgrading our entity-component system to handle automatic velocity and collision detection. Ultimately, the code proved to be unmanageable, and we ended up scrapping it. (We spent, literally, hours upon hours troubleshooting one collision-detection bug after another.)

In the end, we chose to employ a much simpler approach: use HaxeFlixel directly, without any intervening entity-component system. The resulting code is cleaner, clearer, and easier to write and maintain.

Going forward, we expect to implement (prototype) the major core features of our infinite runner ("infinite swimmer" is more like it) by next week.

If you're one of our [Patreon supporters](https://www.patreon.com/DeenGames), you can also expect a playable version of the prototype next week.