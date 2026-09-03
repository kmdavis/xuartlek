---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Earth Scamp"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/small
statblock: inline
name: "Earth Scamp"
level: 1
source: "Monster Core"
aon_id: "creature-2986"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2986"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Earth Scamp"
level: "Creature 1"
size: "Small"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision, tremorsense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +2"
abilityMods: [3, -1, 2, -2, 0, -1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +4; __Will__: +3"
hp: 20
health:
  - name: "HP"
    desc: "20 (fast healing 2 (while underground)); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "20 feet, burrow 20 feet, fly 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ body +8 __Damage__ 1d6+3 bludgeoning"
abilities_bot:
  - name: "Scree Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]]) The earth scamp breathes rocks in a 15-foot cone that deals 2d6 bludgeoning damage to each creature within the area (DC 17 basic Reflex save). The earth scamp can't use Scree Breath again for 1d4 rounds."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/enlarge|Enlarge]] (self only) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/one-with-stone|One with Stone]]"
sourcebook: "_Monster Core_, page 146."
```

```encounter-table
name: Earth Scamp
creatures:
  - 1: Earth Scamp
```
