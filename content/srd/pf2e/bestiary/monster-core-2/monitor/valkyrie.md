---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Valkyrie"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aesir
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Valkyrie"
level: 12
source: "Monster Core 2"
aon_id: "creature-4017"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4017"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Valkyrie"
level: "Creature 12"
size: "Medium"
trait_01: "Aesir"
trait_02: "Monitor"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]; ravenspeaker, [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +23, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +22"
abilityMods: [7, 5, 5, 3, 4, 5]
abilities_top:
  - name: "Claimer of the Slain"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) Valkyries can detect the souls of those recently slain in combat. A valkyrie can spend 10 minutes praying over the body of a creature who has been dead for no more than 12 hours, and if that creature is worthy of becoming an [[srd/pf2e/bestiary/monster-core-2/monitor/einherji|einherji]], the valkyrie transforms that creature into an einherji."
  - name: "Ravenspeaker"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) Valkyries use ravens as servants and spies. They can speak with [[srd/pf2e/compendium/gm/creature-families/raven|ravens]], and they can have up to three raven servitors who follow their commands. Valkyries can constantly observe whatever their commanded ravens sense."
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/armor/magic-armor-3-major-resilient|+1 resilient]] [[srd/pf2e/compendium/equipment/armor#Breastplate|breastplate]]_, _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/runes/returning|returning]] [[srd/pf2e/compendium/equipment/weapons/spear/spear|spear]]_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +24; __Ref__: +20; __Will__: +23"
hp: 215
health:
  - name: "HP"
    desc: "215; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 15"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Recall the Fallen"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "An allied creature within 60 feet who isn't a [[srd/pf2e/compendium/rules-elements/traits/player-core/construct|construct]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]] is reduced to 0 Hit Points, and their [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]] value is 2 or less; Effect The valkyrie restores 5d10 Hit Points to the target."
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spear_ +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d6+15 piercing plus 1d12 electricity"
  - name: "Ranged"
    desc: "⬻ _spear_ +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 2d6+15 piercing plus 1d12 electricity"
abilities_bot:
  - name: "Storm of Battle"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]]) The valkyrie hurls their spear into the air, creating a massive storm in a 100-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]]. Spears of lightning rain down upon enemies in the area, dealing 4d12 electricity damage (DC 32 basic Reflex save). Boneyard Advocates While praying to claim a slain warrior, a valkyrie fractures their own consciousness into two parts: mind and soul. They send their mind spinning along the River of Souls to collect and advocate on behalf of the slain warrior's soul. When the prayer ends, the valkyrie reunites their mind and body, and they join the warrior's body and soul into a single form as a new einherji."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/augury|Augury]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/heroism|Heroism]], [[srd/pf2e/compendium/spells/rank-3/safe-passage|Safe Passage]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/status|Status]] - __5th__ [[srd/pf2e/compendium/spells/rank-1/infuse-vitality|Infuse Vitality]] - __6th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]], [[srd/pf2e/compendium/spells/rank-3/heroism|Heroism]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (self and mount only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 15."
```

```encounter-table
name: Valkyrie
creatures:
  - 1: Valkyrie
```
