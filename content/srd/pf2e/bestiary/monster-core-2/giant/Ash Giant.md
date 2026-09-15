---
noteType: pf2eMonster
aliases: "Ash Giant"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Ash Giant"
level: 11
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4410"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ash Giant"
level: "Creature 11"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 21
perception:
  - name: "Perception"
    desc: "+21; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +16, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +21"
abilityMods: [7, 3, 6, -1, 4, -2]
abilities_top:
  - name: "Vermin Empathy"
    desc: "The ash giant can ask questions of, receive answers from, and use the Diplomacy skill with insects, arachnids, and similar creatures."
  - name: "Items"
    desc: "piggy clod (6), _[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/flail/War Flail|war flail]]_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +23; __Ref__: +18; __Will__: +21 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]"
hp: 240
health:
  - name: "HP"
    desc: "240"
abilities_mid:
  - name: "Tumor Pop"
    desc: "When the ash giant takes piercing damage while they have a swollen tumor, the tumor explodes automatically, with the effect of Blastboil."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ war flail +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|trip]]) __Damage__ 2d10+13 bludgeoning plus Gore Grinder"
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|unarmed]]) __Damage__ 2d4+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ piggy clod +24 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 40 feet]]) __Damage__ 2d8+7 slashing plus 5 slashing [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage"
abilities_bot:
  - name: "Blastboil"
    desc: "⬻ The ash giant pops one of the massive, swollen pustules on their body. Each creature in a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] takes 5d8 poison damage with a DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save. A creature that fails its save is also [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1 (or sickened 2 on a critical failure). This ability and tumor pop can't be used again until another tumor swells to a suitable size in 1d4 rounds."
  - name: "Gore Grinder"
    desc: "⬻"
  - name: "Requirements"
    desc: "The ash giant's last action was a successful war flail Strike"
  - name: "Effect"
    desc: "The ash giant wraps the chain of the flail around the target and grinds its flesh. The creature takes 2d10 slashing damage and 2d8 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent bleed damage]] with a DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save."
  - name: "Tangle-Topple"
    desc: "⬺ The ash giant makes a piggy clod Strike. If it hits, the target is tangled in ragged scrap. It's [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]], can't leave the ground, and falls to the ground if it's flying. This ends if the creature [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] or the metal is [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Forced Open]] (DC 28). Chitinous Chariots Ash giants ride giant insects and other vermin to battle. They especially love to cover their mounts' exoskeletons with metal harnesses, armor plates, and jagged spikes added just for sadism's sake. Mounts they use frequently include the [[srd/pf2e/bestiary/monster-core/animal/Ankhrav Hive Mother|ankhrav hive mother]] and [[srd/pf2e/bestiary/monster-core/animal/Deadly Mantis|deadly mantis]]. Smaller creatures, including the narrik and the shriezyx, are harnessed into teams to pull forward their roving mechanisms of war."
sourcebook: "_Monster Core 2_, page 163."
```

```encounter-table
name: Ash Giant
creatures:
  - 1: Ash Giant
```
