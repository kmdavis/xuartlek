---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sacristan"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/medium
statblock: inline
name: "Sacristan"
level: 10
source: "Monster Core 2"
aon_id: "creature-4609"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4609"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sacristan"
level: "Creature 10"
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; greater darkvision, painsight"
languages: "Common, Diabolic, Shadowtongue"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Athletics +22, Intimidation +18, Stealth +21, Torture Lore +16"
abilityMods: [6, 5, 6, 0, 3, 2]
abilities_top:
  - name: "Painsight"
    desc: "(divine) A velstrac automatically knows whether a creature it sees has any of the doomed, dying, and wounded conditions as well as the value of those conditions."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +22; __Ref__: +19; __Will__: +17 +1 status to all saves vs. magic"
hp: 175
health:
  - name: "HP"
    desc: "175 , regeneration 10 (deactivated by holy or silver); __Immunities__ cold; __Weaknesses__ holy 10, silver 10"
abilities_mid:
  - name: "Staggering Servitude"
    desc: "(aura, divine, fear, mental, visual) 30 feet. When a creature ends its turn in the aura, it sees a vision of the sacristan groveling in pitiable servitude. The creature must succeed at a DC 27 Will save or become stunned 1."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ barbed chain +22 (Magical, reach 10 feet, trip, unholy, versatile S) __Damage__ 2d8+9 piercing plus 1d6 spirit and 2d6 persistent bleed"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, divine, fear, mental, visual) The sacristan eerily stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against staggering servitude. In addition, if the creature was already stunned, on a failed save, its revulsion toward the sacristan's presence causes it to be stupefied 2 for 1 minute. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the sacristan's next turn."
  - name: "Shadow Scream"
    desc: "⬽ (Aura, concentrate, darkness, divine, mental, sonic)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The sacristan opens their mouth to unloose the wailing howls and mind-twisting darkness of the Netherworld. This creates a 30- foot emanation of darkness and wailing sounds around the sacristan. Creatures with darkvision can't see through this darkness. The sacristan can Sustain Shadow Scream for up to 1 minute. Non-velstrac creatures in the area when the ability is used, as well as those who enter or start their turn in the area, must attempt a DC 28 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is then temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is deafened for 1 round."
  - name: "Failure"
    desc: "The creature is confused and deafened for 1 round."
  - name: "Critical Failure"
    desc: "The creature takes 20 mental damage, and is confused and deafened for 1 round."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __3rd__ Fear - __5th__ Chilling Darkness"
sourcebook: "_Monster Core 2_, page 347."
```

```encounter-table
name: Sacristan
creatures:
  - 1: Sacristan
```
