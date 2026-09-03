---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dezullon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/medium
statblock: inline
name: "Dezullon"
level: 10
source: "Monster Core"
aon_id: "creature-2912"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2912"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dezullon"
level: "Creature 10"
size: "Medium"
trait_01: "Plant"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +21"
abilityMods: [5, 7, 3, -4, 2, -1]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +17; __Ref__: +21; __Will__: +16"
hp: 130
health:
  - name: "HP"
    desc: "130 , regeneration 15 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]); __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 20"
abilities_mid:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 27"
speed: "25 feet; climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ vine +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 3d6+8 bludgeoning plus 3d6 acid and Grab"
  - name: "Ranged"
    desc: "⬻ acid glob +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], range 30 feet) __Damage__ 4d8 acid plus amnesia venom"
abilities_bot:
  - name: "Amnesia Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 29 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 2"
    desc: "off-guard and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]] (1 round)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]], off-guard, and clumsy 2 (1 round)"
  - name: "Stage 4"
    desc: "as Stage 3 and permanently forget the last hour (1 round)"
  - name: "Constrict"
    desc: "⬻ 2d6+2 bludgeoning, DC 29"
  - name: "Root"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) Until the next time it acts, the dezullon appears to be a normal pitcher plant. It has an automatic result of 41 (44 in forests or swamps) on [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to pass as a non-creature plant. Dezullon Venom The dezullon is most well known for the psychoactive effects of its secretions. Affected creatures suffer amnesia, briefly forgetting where they are and why they are in pain. Some creatures, desperate to escape the past, willingly expose themselves to a dezullon's amnesia venom in an effort to make their painful memories fade."
sourcebook: "_Monster Core_, page 94."
```

```encounter-table
name: Dezullon
creatures:
  - 1: Dezullon
```
