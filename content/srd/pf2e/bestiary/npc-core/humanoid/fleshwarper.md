---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fleshwarper"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Fleshwarper"
level: 7
source: "NPC Core"
aon_id: "creature-3617"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3617"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Fleshwarper"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Aberration Lore]] +15, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +17, [[srd/pf2e/compendium/rules-elements/skills/lore|Fleshwarping Lore]] +17, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +16, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [3, 4, 2, 4, 2, -1]
abilities_top:
  - name: "Items"
    desc: "fleshwarping concoction (5), [[srd/pf2e/compendium/equipment/adventuring-gear/healers-toolkit-expanded|Healer's Toolkit]], _+1 scalpel_ (functions as a [[srd/pf2e/compendium/equipment/weapons/knife/dagger|dagger]])"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +15; __Will__: +15"
hp: 110
health:
  - name: "HP"
    desc: "110"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scalpel_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+9 piercing"
  - name: "Melee"
    desc: "⬻ fist +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ fleshwarping concoction +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/alchemical|Alchemical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], range increment 20 feet) __Damage__ 4d6 poison plus flesh mutation"
  - name: "Ranged"
    desc: "⬻ _scalpel_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+9 piercing"
abilities_bot:
  - name: "Conduct the Experiment"
    desc: "⬻ The fleshwarper assesses vulnerabilities in a creature's anatomy. They attempt a [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] check against the Fortitude DC of one living creature they can see within 60 feet. On a success, the fleshwarper's melee Strikes deal an extra 2d8 precision damage against that creature for 1 minute or until the fleshwarper critically hits that creature, whichever comes first. Using this action again designates a new target and ends the effect for any previous target. A fleshwarper can target an individual no more than once per day with this ability."
  - name: "Flesh Mutation"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/alchemical|Alchemical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/morph|Morph]]) A creature made of flesh that's hit by a fleshwarping concoction Strike is subject to a random fleshwarping mutation determined by rolling 1d4 and consulting the list below. The creature attempts a DC 25 Fortitude save at the end of each of its turns, ending the mutation on a success. A creature that becomes mutated is thereafter temporarily immune to flesh mutation for 1 day."
  - name: "Spongy Flesh"
    desc: "The creature has weakness 5 to physical damage."
  - name: "Caustic Blood"
    desc: "The creature takes 2d4 persistent acid damage that can't be removed normally, but ends when the mutation does."
  - name: "Sprouting Eyes"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]], but also immune to flanking."
  - name: "Mutated Mind"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]]. It can still recover as noted in the condition, but if it does it remains [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] until the mutation ends."
  - name: "Restore My Masterpiece"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|Healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The fleshwarper is holding or wearing a healer's toolkit"
  - name: "Effect"
    desc: "The fleshwarper stitches the wounds of an adjacent, willing aberration or creature they modified using fleshwarping. The creature regains 20 HP and is then temporarily immune for 1 day. Warped Menagerie A fleshwarper is a master at their dark craft, and creating monsters is practically second nature to them. However, they have no great skill at controlling monsters. Some may keep their creations caged for further study, or to use as grim guard dogs. The especially careless may simply abandon their awful abominations in the wild to become someone else's problem. Classically, their creations are fleshwarps like the [[srd/pf2e/bestiary/monster-core/aberration/grothlut|grothlut]] and [[srd/pf2e/bestiary/monster-core/aberration/irnakurse|irnakurse]]. Other created creatures might resemble [[srd/pf2e/bestiary/monster-core/construct/charnel-creation|charnel creations]], [[srd/pf2e/bestiary/monster-core/ooze/globster|globsters]], or [[srd/pf2e/bestiary/monster-core/aberration/sinspawn|sinspawn]]."
sourcebook: "_NPC Core_, page 159."
```

```encounter-table
name: Fleshwarper
creatures:
  - 1: Fleshwarper
```
