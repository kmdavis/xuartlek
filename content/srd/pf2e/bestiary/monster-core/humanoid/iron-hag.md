---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Iron Hag"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Iron Hag"
level: 6
source: "Monster Core"
aon_id: "creature-3042"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3042"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Iron Hag"
level: "Creature 6"
size: "Large"
trait_01: "Hag"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +13, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +16"
abilityMods: [6, 4, 4, 1, 4, 3]
abilities_top:
  - name: "Coven"
    desc: "An iron hag adds [[srd/pf2e/compendium/spells/rank-3/earthbind|_earthbind_]], [[srd/pf2e/compendium/spells/rank-5/impaling-spike|_impaling spike_]], and [[srd/pf2e/compendium/spells/rank-6/spellwrack|_spellwrack_]] to their coven's spells. Their spell DC when leading a coven is 24."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +12; __Will__: +14 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 80
health:
  - name: "HP"
    desc: "80; __Resistances__ physical 3 (except adamantine)"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/gm-core/precious|cold iron]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+6 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ jaws +16 ([[srd/pf2e/compendium/rules-elements/traits/gm-core/precious|cold iron]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d6+6 piercing"
abilities_bot:
  - name: "Bonds of Iron"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The hag causes a cage built of cold iron fingernails to spring out of nothingness around one creature within 30 feet, attempting an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] against the target's Fortitude DC; if the target has a weakness to [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]], the iron hag gains a +2 circumstance bonus to this check. On a success, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the magical fingernails (or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] on a critical success). If the creature successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 24), the cage crumbles into rust. Any creature can attempt to destroy the cage by attacking it. It has an AC of 19, Hardness 10, and 40 Hit Points."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The iron hag can take on the appearance of any Medium female [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]]. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Embrace of Iron"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by the iron hag's claw"
  - name: "Effect"
    desc: "The hag's nails tear into their captured victim, dealing 2d8 piercing damage (the nails are cold iron). Then the hag can attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Reposition|Reposition]] the creature. If the creature is adjacent to the hag, they can then attempt a jaws Strike against it."
sourcebook: "_Monster Core_, page 190."
```

```encounter-table
name: Iron Hag
creatures:
  - 1: Iron Hag
```
