---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin War Chanter"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Goblin War Chanter"
level: 1
source: "Monster Core"
aon_id: "creature-3027"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3027"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Goblin War Chanter"
level: "Creature 1"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +4, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [2, 3, 2, 1, 0, 4]
abilities_top:
  - name: "Items"
    desc: "dogslicer, Leather Armor, Shortbow (10 arrows)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +8; __Will__: +5"
hp: 16
health:
  - name: "HP"
    desc: "16"
abilities_mid:
  - name: "Goblin Scuttle"
    desc: "⬲"
  - name: "Trigger"
    desc: "A goblin ally ends a move action adjacent to the goblin"
  - name: "Effect"
    desc: "The goblin Steps."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dogslicer +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/backstabber|Backstabber]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Goblin Song"
    desc: "⬻ The war chanter sings annoying goblin songs, distracting foes with silly and repetitive lyrics. The chanter attempts a [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] check against the Will DCs of up to two enemies within 30 feet. This has the usual traits and restrictions for a Performance check."
  - name: "Critical Success"
    desc: "The target takes a –1 status penalty to Perception checks and Will saves for 1 minute."
  - name: "Success"
    desc: "As critical success, but the target is affected for only 1 round."
  - name: "Critical Failure"
    desc: "The target is temporarily immune to Goblin Song for 1 hour."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 17, attack +7 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/courageous-anthem|Courageous Anthem]], [[srd/pf2e/compendium/spells/cantrips/message|Message]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/bless|Bless]], [[srd/pf2e/compendium/spells/rank-1/soothe|Soothe]] (2 slots)"
sourcebook: "_Monster Core_, page 175."
```

```encounter-table
name: Goblin War Chanter
creatures:
  - 1: Goblin War Chanter
```
