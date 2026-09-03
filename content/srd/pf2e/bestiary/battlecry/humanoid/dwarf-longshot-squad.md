---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dwarf Longshot Squad"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Dwarf Longshot Squad"
level: 10
source: "Battlecry!"
aon_id: "creature-3914"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3914"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Dwarf Longshot Squad"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Dwarf"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Dwarven|Dwarven]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +22"
abilityMods: [1, 7, 5, 3, 1, 0]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +19; __Ref__: +22; __Will__: +16"
hp: 180
health:
  - name: "HP"
    desc: "180 (4 segments); __Weaknesses__ area damage 12, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 12"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet; troop movement"
abilities_bot:
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "Using blades attached to their crossbows, the dwarven longshots engages in a coordinated melee attack against enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]], with a DC 26 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. ⬻ 1d8+2 piercing damage ⬺ 2d8+11 piercing damage ⬽ 3d8+13 piercing damage"
  - name: "Hampering Fusillade"
    desc: "⬺ The dwarven longshots fire dozens of bolts in quick succession to slow down advancing enemies. Each creature in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] within 120 feet must attempt a DC 26 Fortitude saving throw. On a failure, a creature takes a –10-foot circumstance penalty to its Speed for 1 minute. Spending an Interact action to remove the bolts ends this penalty."
  - name: "Bolts from the Blue"
    desc: "⬺ The dwarven longshots reload their crossbows, then launch a ranged attack in the form of a volley. This volley is a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] within 120 feet that deals 6d6 piercing damage with a DC 26 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex saving throw. When the dwarven longshot squad is reduced to 2 segments, this area decreases to a 10-foot burst. Longshots With Guns Dwarves from Dongun Hold and similar places have access to firearms, and you might choose to reflect this by giving the dwarf longshot squad rifles. Adjust the stat block to have the uncommon trait and replace mentions of “[[srd/pf2e/compendium/equipment/weapons/crossbow/crossbow|crossbows]]” to “rifles” and “bolts” to “bullets.” In addition, give the Bolts from the Blue action the concussive trait, meaning that it deals bludgeoning or piercing damage, whichever would be more detrimental to each target (you may also want to refer to it as “Bullets from the Blue”). Finally, replace Hampering Fusillade with the following ability."
  - name: "Bullet Smog"
    desc: "⬺ The dwarven longshots fire their rifles in rapid succession to create a cloud of smoke within 120 feet. This cloud is a 20-foot burst and lasts for 1 minute or until it is dispersed by a strong wind, whichever comes first. All creatures within the cloud become [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]], and all creatures outside the cloud become concealed to creatures within it."
sourcebook: "_Battlecry!_, page 179."
```

```encounter-table
name: Dwarf Longshot Squad
creatures:
  - 1: Dwarf Longshot Squad
```
