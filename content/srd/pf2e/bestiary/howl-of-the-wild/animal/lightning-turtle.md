---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lightning Turtle"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Lightning Turtle"
level: 12
source: "Howl of the Wild"
aon_id: "creature-3284"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3284"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Lightning Turtle"
level: "Creature 12"
size: "Large"
trait_01: "Animal"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; low-light vision, greater electrolocation 20 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25"
abilityMods: [5, 1, 7, -4, 4, 1]
abilities_top:
  - name: "Deep Breath"
    desc: "The lightning turtle can [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Mounted Defenses|hold its breath]] for 30 minutes."
  - name: "Greater Electrolocation"
    desc: "A lightning turtle can sense minute electrical charges in living creatures, which it can use as a precise sense at a range of 20 feet. This distance increases to 100 feet against any creature that has used an [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] effect within the last minute."
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +25; __Ref__: +19; __Will__: +22"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]]"
abilities_mid:
  - name: "Shell Shock"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]])"
  - name: "Trigger"
    desc: "A lightning turtle is hit by a melee or an [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]] attack"
  - name: "Effect"
    desc: "The lightning turtle releases some of its stored electrical power, inflicting 7d6 electricity damage to the creature attacking it."
speed: "15 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]]) __Damage__ 2d12+5 piercing plus 2d6 electricity"
  - name: "Ranged"
    desc: "⬻ electrical burst +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], range 60 feet) __Damage__ 4d10 electricity"
abilities_bot:
  - name: "Healing Pulse"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|Healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The lightning turtle releases a pulse of low-intensity electricity from its body to promote healing. This restores 5d8 Hit Points to the turtle and each living ally within 10 feet, including creatures normally immune to electricity. The turtle can't use Healing Pulse again for 1 minute and is temporarily immune to the Healing Pulse of any lightning turtle for 1 minute."
  - name: "Sparking Shell"
    desc: "⬻ The lightning turtle withdraws into its shell. This increases its AC to 36, but it can't act except to use Shell Shock or reemerge as a single action. While in its shell, the turtle's Shell Shock deals another 4d6 damage and loses the [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] trait."
sourcebook: "_Howl of the Wild_, page 153."
```

```encounter-table
name: Lightning Turtle
creatures:
  - 1: Lightning Turtle
```
