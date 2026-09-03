---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Rune Dragon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Rune Dragon"
level: 10
source: "Monster Core 2"
aon_id: "creature-4363"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4363"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Rune Dragon"
level: "Creature 10"
size: "Large"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, magic sense (imprecise) 60 feet, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]; five additional common languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +23, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +21, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/lore|Linguistics Lore]] +21, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +20, [[srd/pf2e/compendium/rules-elements/skills/lore|Rune Lore]] +23, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +19, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +19"
abilityMods: [4, 4, 5, 6, 4, 3]
abilities_top:
  - name: "Magic Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]]) The rune dragon is aware of any active magical abilities and effects within the listed range. When the dragon [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seeks]], it gains the benefits of a 4th-rank [[srd/pf2e/compendium/spells/cantrips/detect-magic|_detect magic_]] spell within the listed range (in addition to the normal benefits of Seeking)."
  - name: "Runic Scales"
    desc: "The rune dragon's scales function as [[srd/pf2e/compendium/equipment/consumables/runestone|_runestones_]]. The rune dragon can't use the effects or abilities of the runes etched on its scales, but they can transfer these runes to appropriate objects. Transferring a rune to or from an item in this way requires 1 minute, during which the dragon is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]]. The process is automatic and doesn't require a check, but if the dragon stops or is interrupted in this process, the rune is destroyed. A rune dragon can have any number of runes etched on its scales, though they typically have only a handful of runes etched on their scales at a time."
  - name: "Items"
    desc: "3 common runes of 5th level or lower etched upon their scales"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +19; __Ref__: +17; __Will__: +21 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]]"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], Shifting Runes, [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Retributive Rune"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 15 feet damages the rune dragon"
  - name: "Effect"
    desc: "With a burst of runic magic, the rune dragon uses their detonating rune ability on the triggering creature and immediately causes the rune to detonate if it didn't automatically do so."
speed: "60 feet, fly 100 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+10 piercing plus detonating rune"
  - name: "Melee"
    desc: "⬻ claw +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d6+10 slashing plus detonating rune"
  - name: "Melee"
    desc: "⬻ tail +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+10 bludgeoning plus Push 10 feet"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Runic Breath whenever they score a critical hit with a Strike."
  - name: "Detonating Rune"
    desc: "The rune dragon's Strikes and abilities can leave a detonating rune on their targets. If a creature would receive a detonating rune while they already have one, instead of adding another rune, their current detonating rune activates, dealing 4d6 damage to the target and expending the rune. The detonating rune's damage type matches the dragon's current Shifting Rune. A creature can use an [[srd/pf2e/compendium/rules-elements/actions/player-core#Interact|Interact]] action to remove the rune. Detonating runes fade after 1 minute if not detonated."
  - name: "Runic Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]]) The dragon launches hundreds of exploding runes that detonate upon impact, dealing 9d6 damage in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage type of this ability is determined by Shifting Rune. Creatures who fail the save are also affected by detonating rune. The dragon can't use Runic Breath again for 1d4 rounds."
  - name: "Shifting Runes"
    desc: "⬻ The rune dragon chooses between [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] damage. T he runes etched upon the dragon shift, forming runes of that energy on its scales. The dragon gains immunity to that damage type, and their detonating runes and Runic Breath deal that damage type. Anyone trained in Arcana can immediately recognize the energy type of the etched rune without a check."
sourcebook: "_Monster Core 2_, page 131."
```

```encounter-table
name: Young Rune Dragon
creatures:
  - 1: Young Rune Dragon
```
