---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gluttonous Geode"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/tiny
statblock: inline
name: "Gluttonous Geode"
level: 1
source: "Rage of Elements"
aon_id: "creature-2624"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2624"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Gluttonous Geode"
level: "Creature 1"
size: "Tiny"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +4, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [3, -1, 3, -4, 1, -3]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +4; __Will__: +6"
hp: 25
health:
  - name: "HP"
    desc: "25; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ crystal teeth +9 __Damage__ 1d4+4 piercing plus Attach"
abilities_bot:
  - name: "Attach"
    desc: "⬺ The geode Leaps up to 15 feet and makes a crystal teeth Strike. If it hits a creature larger than itself, it can attach to that creature. Doing so is like Grabbing the creature (Escape DC 17), but the geode moves with that creature rather than holding it in place. The geode is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] while attached. If the geode is killed or pushed away while attached to a creature, that creature takes 1 persistent bleed damage. Escaping the attached geode or removing the geode in other ways doesn't cause bleed damage."
  - name: "Gnaw"
    desc: "⬻"
  - name: "Requirements"
    desc: "The geode is attached to a creature"
  - name: "Effect"
    desc: "The geode deals 1d4+2 bludgeoning damage to the creature it's attached to (DC 17 basic Fortitude save)."
sourcebook: "_Rage of Elements_, page 104."
```

```encounter-table
name: Gluttonous Geode
creatures:
  - 1: Gluttonous Geode
```
