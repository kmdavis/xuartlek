---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Phalanx Formation"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Phalanx Formation"
level: 6
source: "NPC Core"
aon_id: "creature-3527"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3527"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Phalanx Formation"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +11"
abilityMods: [5, 0, 2, 1, 2, 2]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +16; __Ref__: +12; __Will__: +14"
hp: 99
health:
  - name: "HP"
    desc: "99 (4 segments); __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Hurl Javelins"
    desc: "⬺ The troop's members throw a volley of spears. Each creature in a 10-foot burst within 30 feet of the troop takes 2d6+5 piercing damage with a DC 21 basic Reflex save. When the phalanx formation is reduced to 2 or fewer segments, this area decreases to a 5-foot burst. __Spears Out!__"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The phalanx formation thrusts their longspears out in all directions, striking all unfortunate enough to be near them. Each enemy in a 10-foot emanation must attempt a DC 21 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8+2 piercing damage ⬺ 2d8+5 piercing damage ⬽ 3d8+5 piercing damage __Shields Up!__ ⬻ The phalanx formation raises their shields to protect one another. The formation gains a +2 circumstance bonus to AC and Reflex until the start of their next turn. This bonus increases to +3 against physical ranged attacks."
sourcebook: "_NPC Core_, page 91."
```

```encounter-table
name: Phalanx Formation
creatures:
  - 1: Phalanx Formation
```
