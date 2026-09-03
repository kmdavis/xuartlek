---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Harpy"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/air
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Harpy"
level: 5
source: "Monster Core"
aon_id: "creature-3046"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3046"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Harpy"
level: "Creature 5"
size: "Medium"
trait_01: "Air"
trait_02: "Beast"
trait_03: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; wind's whispers"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +13"
abilityMods: [1, 4, 0, -1, 1, 2]
abilities_top:
  - name: "Wind's Whispers"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) When a harpy speaks, they can choose one creature within 90 feet. That creature can hear the harpy's words over any other sound, but no other creature hears the words at all."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +15; __Will__: +12"
hp: 75
health:
  - name: "HP"
    desc: "75"
abilities_mid:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 21"
speed: "20 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 2d8+4 piercing plus putrid plague"
  - name: "Melee"
    desc: "⬻ talon +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 2d6+4 slashing"
abilities_bot:
  - name: "Hungry Winds"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The harpy uses the wind to pull its prey closer. A target within 20 feet must succeed at a DC 21 Fortitude save or be pulled adjacent to the harpy, where they make a jaws Strike against the target. If the target was pulled off the ground and can't fly, it then falls as normal."
  - name: "Putrid Plague"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) The [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] and [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] conditions from putrid plague can't end or be reduced until the disease is cured"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1d4 hours)"
  - name: "Stage 2"
    desc: "sickened 1 (1 day)"
  - name: "Stage 3"
    desc: "sickened 1 and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 day)"
  - name: "Stage 4"
    desc: "unconscious (1 day)"
  - name: "Stage 5"
    desc: "dead Harpy Exiles Most harpies are cruel and sadistic, but now and then a harpy manages to escape from its family and becomes exposed to the wider world. Eyes opened, these harpy exiles are almost always more mild-mannered, hygienic, and open to non-combat interactions."
sourcebook: "_Monster Core_, page 193."
```

```encounter-table
name: Harpy
creatures:
  - 1: Harpy
```
