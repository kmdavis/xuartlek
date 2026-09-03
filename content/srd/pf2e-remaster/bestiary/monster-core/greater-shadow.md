---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Greater Shadow"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Greater Shadow"
level: 7
source: "Monster Core"
aon_id: "creature-3187"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3187"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Greater Shadow"
level: "Creature 7"
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Stealth +20"
abilityMods: [-5, 5, 0, 0, 2, 4]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +18; __Will__: +15"
hp: 75
health:
  - name: "HP"
    desc: "75 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, precision, unconscious; __Resistances__ all 10 (except force, _ghost touch_, spirit, or vitality; double resistance vs. non-magical); __Weaknesses__ light vulnerability"
abilities_mid:
  - name: "Light Vulnerability"
    desc: "Attacks against the shadow are treated as magical if made by a creature who is in magical light or with an object that is in magical light (such as from the _light_ spell)."
speed: "fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shadow hand +18 (Finesse, Magical) __Damage__ 2d10+6 void"
abilities_bot:
  - name: "Shadow Spawn"
    desc: "When a creature's shadow is pulled free by Steal Shadow, it becomes a shadow spawn under the command of the shadow that created it. This shadow spawn doesn't have Steal Shadow. If the creature the shadow spawn was pulled from dies, the shadow spawn becomes a full-fledged, autonomous shadow. If the creature recovers from its enfeeblement, its shadow returns to it and the shadow spawn is extinguished."
  - name: "Slink in Shadows"
    desc: "The shadow can Hide or end its Sneak in a creature's or object's shadow."
  - name: "Steal Shadow"
    desc: "⬻ (Divine)"
  - name: "Requirements"
    desc: "The shadow hit a living creature with a shadow hand Strike on its previous action"
  - name: "Effect"
    desc: "The shadow pulls at the target's shadow, making the creature enfeebled 2 (or enfeebled 3 on a critical hit). This is cumulative with other enfeebled conditions from shadows, to a maximum of enfeebled 4. If this increases a creature's enfeebled value to 3 or more, the target's shadow is separated from its body (see shadow spawn). The enfeebled value from Steal Shadow decreases by 1 every hour."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __2nd__ Darkness (at will)"
sourcebook: "_Monster Core_, page 306."
```

```encounter-table
name: Greater Shadow
creatures:
  - 1: Greater Shadow
```
