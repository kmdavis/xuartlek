---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Umbral Gnome Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Umbral Gnome Scout"
level: 1
source: "Monster Core"
aon_id: "creature-3021"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3021"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Umbral Gnome Scout"
level: "Creature 1"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Gnomish|Gnomish]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5"
abilityMods: [2, 4, 2, 0, 2, -1]
abilities_top:
  - name: "Items"
    desc: "Light Pick, Sling (20 bullets)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +9; __Will__: +5"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light pick +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d8]]) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ sling +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Hidden Movement"
    desc: "If the umbral gnome scout starts their turn [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] or [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] to a creature, that creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the umbral gnome scout's attacks until the end of the turn."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 14 - __1st__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]]"
sourcebook: "_Monster Core_, page 172."
```

```encounter-table
name: Umbral Gnome Scout
creatures:
  - 1: Umbral Gnome Scout
```
