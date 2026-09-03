---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Herexen"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Herexen"
level: 2
source: "Monster Core"
aon_id: "creature-3049"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3049"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Herexen"
level: "Creature 2"
size: "Medium"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Athletics +6, Deception +7, Religion +10, Stealth +6"
abilityMods: [2, 2, 1, 0, 4, 3]
abilities_top:
  - name: "Items"
    desc: "Dagger, defiled religious symbol of Pharasma"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +8; __Will__: +10"
hp: 30
health:
  - name: "HP"
    desc: "30 (void healing (page 360)); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Final Blasphemy"
    desc: "(divine, void) When the herexen is destroyed, it explodes in a wave of void energy with the effects of a 3-action _harm_ spell (DC 18). The herexen is destroyed, so it doesn't gain any Hit Points from this use of harm, and it doesn't need to have any harm spells remaining to use this ability."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +10 (Agile, versatile S) __Damage__ 1d6+4 piercing plus heretic's smite"
abilities_bot:
  - name: "Heretic's Smite"
    desc: "(Divine, Unholy) While wielding the favored weapon of its former deity (such as a dagger for an ex-Pharasmin herexen), the herexen's Strikes deal an additional 1d6 spirit damage to creatures with the holy trait. Herexen Lairs Most herexens settle down in a particular town or region to corrupt the local populace. Powerful herexens may boldly lair in a defiled temple, creating a vile parody of the building's former glory. However, most herexens hide in decrepit places such as ruins, forgotten basements, or tombs."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 18 - __1st__ Harm (×4) __Cleric Domain Spells 1 Focus Point,__ DC 18 - __1st__ Death's Call"
sourcebook: "_Monster Core_, page 195."
```

```encounter-table
name: Herexen
creatures:
  - 1: Herexen
```
