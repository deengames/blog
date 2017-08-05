meta-id: ebee115eb0f9d1cb93056fc3ef4afaa0e37e8283

meta-title: Talha's Migration, Week 3: Upgrades!
meta-publishedOn: 2017-07-21
meta-tags: devlog

![screenshot](http://i.imgur.com/JuNPgsR.gif)

This week, we settled the question of "should we create a separate currency, or reuse food as the currency, for in-game updates?" We decided to re-use food; relevant Reddit game-design discussion is [here](https://www.reddit.com/r/gamedesign/comments/6nhsxo/infinite_runner_additional_currency_or_food/).

We also made some changes to how speed works. The full list of changes this week includes:

- Decision not to have a "win" state, but to continue perpetually
- Capping velocity so you can't go too fast
- You speed up relative to how far you travel, not how much food you collect
- Food collected persists between games and sessions
- Performance optimizations (object pools for reusing objects)
- Shop button takes you to the shop
- You can buy starting-health upgrade at the shop, which persists across games and sessions
- You can buy up to six starting health in total
- Internationalization: app is now localizable
- Localization fail for Urdu and Arabic

While we succeeded in internationalizing our app, we only have the English localization. 

The two others that we can reasonably achieve (Urdu and Arabic) both use right-to-left languages. Unfortunately, HaxeFlixel doesn't yet support right-to-left-languages; the letters are disjointed (instead of connected) and left-to-right:

![screenshot of L10N](http://i.imgur.com/gtWMQDm.png)

While the results are disappointing, we at least made our app localizable. In the future, may look to the game development community to help add some localizations prior to launch.

With that, the plan for next week is to break out more features: what else do we need before we can ship the MVP of our game? Once we complete those, we can look into adding polish (better art, tutorial, etc.) and shipping the first version of our game in the next few weeks.