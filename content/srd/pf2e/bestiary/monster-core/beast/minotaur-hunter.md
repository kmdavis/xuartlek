---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Minotaur Hunter"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Minotaur Hunter"
level: 4
source: "Monster Core"
aon_id: "creature-3099"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3099"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Minotaur Hunter"
level: "Creature 4"
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [6, 0, 3, -2, 2, -1]
abilities_top:
  - name: "Perfect Orienteering"
    desc: "A minotaur automatically critically succeeds at [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Direction|Sense Direction]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Track]]."
  - name: "Items"
    desc: "Greataxe"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +8; __Will__: +10"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d12+8 slashing"
  - name: "Melee"
    desc: "⬻ horn +14 __Damage__ 1d8+8 piercing"
abilities_bot:
  - name: "Axe Swipe"
    desc: "⬺ The minotaur swings their axe in a wide arc, making greataxe Strikes against any two foes who are adjacent to each other and within the minotaur's reach. The multiple attack penalty does not increase until after both attacks are resolved."
  - name: "Hunted Fear"
    desc: "⬻ The minotaur snorts and clomps as they hunt their prey, inspiring terror. The minotaur makes an [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] all living creatures within 60 feet that can hear the minotaur but not see them. Roll once and apply the result to all creatures. If the targets are in a maze or similarly difficult-to-navigate structure, the minotaur gains a +4 circumstance bonus to this check. Creatures that become [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] as a result also take a –2 circumstance penalty to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks to avoid getting lost for 1 minute. Each target is temporarily immune for 1 minute."
  - name: "Powerful Charge"
    desc: "⬺ The minotaur Strides twice, then makes a horn Strike. If they moved at least 20 feet from their starting position, the Strike's damage is increased to 2d8+10. Variant Minotaurs Most minotaurs are a simple blend of muscular humanoid and raging bull, but unusual variants and unique minotaurs may have different physical features and abilities. Great-horned minotaurs can impale foes if they critically succeed on a charge, but they do not have the Hunted Fear ability. Shaggy minotaurs are covered in thick hair form head to toe, allowing them to live in freezing environments with ease and giving them resistance to cold damage, but their hooves are broad and heavy, making it impossible for them to charge."
sourcebook: "_Monster Core_, page 232."
```

```encounter-table
name: Minotaur Hunter
creatures:
  - 1: Minotaur Hunter
```
