---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brochmaw"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/huge
statblock: inline
name: "Brochmaw"
level: 13
source: "Rage of Elements"
aon_id: "creature-2632"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2632"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Brochmaw"
level: "Creature 13"
size: "Huge"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +28, Cooking Lore +24, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +24"
abilityMods: [8, 4, 8, 3, 5, 4]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +28; __Ref__: +20; __Will__: +23"
hp: 259
health:
  - name: "HP"
    desc: "259; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 15"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ skewer +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+8 piercing plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ hot oil +25 (range 30 feet) __Damage__ 3d6+7 fire damage plus 1d8 persistent fire damage plus 3 fire splash damage and marinade"
abilities_bot:
  - name: "Marinade"
    desc: "A creature taking persistent fire damage from the brochmaw's hot oil Strike is more readily cooked, taking a –2 circumstance penalty to Fortitude saves against Roast for as long as it is taking persistent fire damage."
  - name: "Roast"
    desc: "⬻ The brochmaw turns a skewer over their oven, cooking anything impaled on it. Creatures grabbed by the brochmaw's skewer take 3d6 fire damage (DC 32 basic Fortitude save). Creatures who have been Roasted take a –2 circumstance penalty to Fortitude saves against Serve for 1 minute."
  - name: "Serve"
    desc: "⬺"
  - name: "Requirements"
    desc: "The brochmaw has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The brochmaw eats their hard-earned meal off one of their skewers. The brochmaw bites down on one creature it has grabbed, dealing 12d6 piercing damage (DC 32 basic Fortitude save); the brochmaw regains Hit Points equal to half the damage dealt. The creature is then freed from the skewer."
  - name: "Skewer Master"
    desc: "The skewers of a brochmaw are more than long enough to hold multiple creatures. A brochmaw can have up to three creatures [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] on its skewer, and it can still make Strikes with its skewer even if it has creatures grabbed, though it can't target creatures it has grabbed. Planar Delicacies Though brochmaws love to devour new things, they still have favorite meals they like to keep on hand. Brochmaws love amphibian meat, though the origin of this appeal is a mystery. They will eagerly consume geniekin of all kinds because the magical blood produces a psychedelic effect. Brochmaws think celestials are as dangerous as they are delicious, requiring a precise cooking process to avoid killing the consumer. Most brochmaws are far too impatient to prepare celestial meat properly, often to disastrous results."
sourcebook: "_Rage of Elements_, page 127."
```

```encounter-table
name: Brochmaw
creatures:
  - 1: Brochmaw
```
