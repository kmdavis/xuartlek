---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Augur"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/tiny
statblock: inline
name: "Augur"
level: 1
source: "Monster Core 2"
aon_id: "creature-4606"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4606"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Augur"
level: "Creature 1"
size: "Tiny"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; greater darkvision, painsight"
languages: "Common, Diabolic, Shadowtongue; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Deception +6, Intimidation +7, Religion +4, Stealth +8, Torture Lore +7"
abilityMods: [-1, 3, 1, 2, 1, -1]
abilities_top:
  - name: "Painsight"
    desc: "(divine) A velstrac automatically knows whether a creature it sees has any of the doomed, dying, and wounded conditions as well as the value of those conditions."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +10; __Will__: +7"
hp: 15
health:
  - name: "HP"
    desc: "15 , regeneration 2 (deactivated by holy or silver); __Immunities__ cold; __Weaknesses__ holy 5, silver 5"
abilities_mid:
  - name: "Feel the Blades"
    desc: "(aura, divine, fear, mental, visual) 30 feet. When a creature ends its turn in the aura, it feels the sharp barbs of the augur's blades on its skin. The creature must succeed at a DC 17 Will save or become frightened 1 (frightened 2 on a critical failure)."
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ blade +8 (Agile, finesse, magical, unholy, versatile P) __Damage__ 1d4–1 slashing plus 1d4 persistent bleed"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, divine, fear, mental, visual) The augur stares at a creature they can see within 30 feet. The target must immediately attempt a Will save against feel the blades. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the augur's next turn."
  - name: "Whirling Slice"
    desc: "⬺ The augur Flies or Strides, whirling as they move. The augur deals the damage of their blade Strike to each creature whose space they enter (DC 16 basic Reflex save). Each creature is affected only once, even if the augur moves through its space multiple times."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Telekinetic Hand - __1st__ Harm (×3) - __2nd__ Augury (×2) - __4th__ Read Omens (once per week)"
sourcebook: "_Monster Core 2_, page 344."
```

```encounter-table
name: Augur
creatures:
  - 1: Augur
```
