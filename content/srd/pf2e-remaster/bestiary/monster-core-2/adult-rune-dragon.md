---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Rune Dragon"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Rune Dragon"
level: 14
source: "Monster Core 2"
aon_id: "creature-4364"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4364"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Rune Dragon"
level: "Creature 14"
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision, magic sense (imprecise) 60 feet, scent (imprecise) 60 feet"
languages: "Common, Draconic; seven additional common languages"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Arcana +29, Athletics +27, Crafting +27, Diplomacy +25, Linguistics Lore +27, Performance +27, Rune Lore +29, Society +25, Survival +25"
abilityMods: [6, 6, 7, 8, 6, 4]
abilities_top:
  - name: "Magic Sense"
    desc: "(arcane) The rune dragon is aware of any active magical abilities and effects within the listed range. When the dragon Seeks, it gains the benefits of a 4th-rank _detect magic_ spell within the listed range (in addition to the normal benefits of Seeking)."
  - name: "Runic Scales"
    desc: "The rune dragon's scales function as _runestones_. The rune dragon can't use the effects or abilities of the runes etched on its scales, but they can transfer these runes to appropriate objects. Transferring a rune to or from an item in this way requires 1 minute, during which the dragon is off-guard. The process is automatic and doesn't require a check, but if the dragon stops or is interrupted in this process, the rune is destroyed. A rune dragon can have any number of runes etched on its scales, though they typically have only a handful of runes etched on their scales at a time."
  - name: "Items"
    desc: "3 common runes of 9th level or lower etched upon their scales"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +25; __Ref__: +23; __Will__: +27 +2 status to all saves vs. arcane"
hp: 255
health:
  - name: "HP"
    desc: "255; __Immunities__ paralyzed, Shifting Runes, sleep"
abilities_mid:
  - name: "Canceling Rune"
    desc: "⬲ (arcane)"
  - name: "Trigger"
    desc: "The dragon is the target of a spell that requires a saving throw"
  - name: "Effect"
    desc: "The dragon attempts to unmake the spell's foundational runes. They attempt to counteract the spell (counteract rank 7th, counteract modifier +26). If successful, the dragon is unaffected by the spell; other subjects are affected by the spell normally. The dragon can't use Canceling Rune again for 1d4 rounds."
  - name: "Retributive Rune"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 15 feet damages the rune dragon"
  - name: "Effect"
    desc: "With a burst of runic magic, the rune dragon uses their detonating rune ability on the triggering creature and immediately causes the rune to detonate if it didn't automatically do so."
speed: "70 feet, fly 140 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +28 (Magical, reach 15 feet) __Damage__ 3d8+14 piercing plus detonating rune"
  - name: "Melee"
    desc: "⬻ claw +28 (Agile, magical, reach 10 feet) __Damage__ 3d6+14 slashing plus detonating rune"
  - name: "Melee"
    desc: "⬻ tail +26 (Magical, reach 20 feet) __Damage__ 3d10+14 bludgeoning plus Improved Push 10 feet"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Runic Breath whenever they score a critical hit with a Strike."
  - name: "Detonating Rune"
    desc: "The rune dragon's Strikes and abilities can leave a detonating rune on their targets. If a creature would receive a detonating rune while they already have one, instead of adding another rune, their current detonating rune activates, dealing 5d6 damage to the target and expending the rune. The detonating rune's damage type matches the dragon's current Shifting Rune. A creature can use an Interact action to remove the rune. Detonating runes fade after 1 minute if not detonated."
  - name: "Entangling Rune"
    desc: "⬻ (Arcane) The rune dragon creates a large trapping rune in a 10-foot burst within 60 feet. A creature other than the dragon that enters a trapped area or ends their turn in the trapped area activates the rune, causing it to entangle them. That creature must succeed at a DC 34 Reflex save or become immobilized for 1 minute or until it Escapes. The rune can trap only a single creature at a time. The rune vanishes either when a creature succeeds against the rune, when a creature successfully Escapes the rune, or after 1 minute. A creature adjacent to the rune can use an Interact action to remove the rune."
  - name: "Runic Breath"
    desc: "⬺ (Arcane) The dragon launches hundreds of exploding runes that detonate upon impact, dealing 12d6 damage in a 40-foot cone (DC 34 basic Reflex save). The damage type of this ability is determined by Shifting Rune. Creatures who fail the save are also affected by detonating rune. The dragon can't use Runic Breath again for 1d4 rounds."
  - name: "Shifting Runes"
    desc: "⬻ The rune dragon chooses between acid, cold, electricity, fire, or sonic damage. T he runes etched upon the dragon shift, forming runes of that energy on its scales. The dragon gains immunity to that damage type, and their detonating runes and Runic Breath deal that damage type. Anyone trained in Arcana can immediately recognize the energy type of the etched rune without a check."
sourcebook: "_Monster Core 2_, page 132."
```

```encounter-table
name: Adult Rune Dragon
creatures:
  - 1: Adult Rune Dragon
```
