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
languages: "Common, Draconic; five additional common languages"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Arcana +23, Athletics +21, Crafting +21, Diplomacy +18, Linguistics Lore +21, Performance +20, Rune Lore +23, Society +19, Survival +19"
abilityMods: [4, 4, 5, 6, 4, 3]
abilities_top:
  - name: "Magic Sense"
    desc: "(arcane) The rune dragon is aware of any active magical abilities and effects within the listed range. When the dragon Seeks, it gains the benefits of a 4th-rank _detect magic_ spell within the listed range (in addition to the normal benefits of Seeking)."
  - name: "Runic Scales"
    desc: "The rune dragon's scales function as _runestones_. The rune dragon can't use the effects or abilities of the runes etched on its scales, but they can transfer these runes to appropriate objects. Transferring a rune to or from an item in this way requires 1 minute, during which the dragon is off-guard. The process is automatic and doesn't require a check, but if the dragon stops or is interrupted in this process, the rune is destroyed. A rune dragon can have any number of runes etched on its scales, though they typically have only a handful of runes etched on their scales at a time."
  - name: "Items"
    desc: "3 common runes of 5th level or lower etched upon their scales"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +19; __Ref__: +17; __Will__: +21 +2 status to all saves vs. arcane"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ paralyzed, Shifting Runes, sleep"
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
    desc: "⬻ jaws +22 (Magical, reach 10 feet) __Damage__ 2d8+10 piercing plus detonating rune"
  - name: "Melee"
    desc: "⬻ claw +22 (Agile, magical) __Damage__ 2d6+10 slashing plus detonating rune"
  - name: "Melee"
    desc: "⬻ tail +20 (Magical, reach 15 feet) __Damage__ 2d10+10 bludgeoning plus Push 10 feet"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Runic Breath whenever they score a critical hit with a Strike."
  - name: "Detonating Rune"
    desc: "The rune dragon's Strikes and abilities can leave a detonating rune on their targets. If a creature would receive a detonating rune while they already have one, instead of adding another rune, their current detonating rune activates, dealing 4d6 damage to the target and expending the rune. The detonating rune's damage type matches the dragon's current Shifting Rune. A creature can use an Interact action to remove the rune. Detonating runes fade after 1 minute if not detonated."
  - name: "Runic Breath"
    desc: "⬺ (Arcane) The dragon launches hundreds of exploding runes that detonate upon impact, dealing 9d6 damage in a 30-foot cone (DC 29 basic Reflex save). The damage type of this ability is determined by Shifting Rune. Creatures who fail the save are also affected by detonating rune. The dragon can't use Runic Breath again for 1d4 rounds."
  - name: "Shifting Runes"
    desc: "⬻ The rune dragon chooses between acid, cold, electricity, fire, or sonic damage. T he runes etched upon the dragon shift, forming runes of that energy on its scales. The dragon gains immunity to that damage type, and their detonating runes and Runic Breath deal that damage type. Anyone trained in Arcana can immediately recognize the energy type of the etched rune without a check."
sourcebook: "_Monster Core 2_, page 131."
```

```encounter-table
name: Young Rune Dragon
creatures:
  - 1: Young Rune Dragon
```
