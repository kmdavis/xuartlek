---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grioth Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/grioth
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Grioth Scout"
level: 1
source: "Monster Core 2"
aon_id: "creature-4425"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4425"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Grioth Scout"
level: "Creature 1"
size: "Medium"
trait_01: "Grioth"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; greater darkvision, echolocation (precise) 20 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], Grioth; telepathy 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [0, 4, 2, 1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/knife/kukri|voidglass kukri]]"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +7"
hp: 18
health:
  - name: "HP"
    desc: "18; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 3"
abilities_mid:
  - name: "Light Blindness"
    desc: ""
  - name: "No Breath"
    desc: "A grioth doesn't breathe except to speak and is immune to effects that require breathing (such as an inhaled poison)."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|trip]]) __Damage__ 1d6 slashing"
  - name: "Melee"
    desc: "⬻ jaws +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d4 piercing plus grioth venom"
abilities_bot:
  - name: "Grioth Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]])"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 1 (1 round)"
  - name: "Stage 2"
    desc: "frightened 2 (1 round)"
  - name: "Stage 3"
    desc: "frightened 3 (1 round)"
  - name: "Shock Mind"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The grioth scout makes a Strike with a voidglass weapon. If the Strike hits, it deals an additional 1d6 mental damage, and the target must succeed at a DC 17 Will save (this has the [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]] trait) or become [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 round."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 16, attack +8 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/phantom-pain|Phantom Pain]]"
sourcebook: "_Monster Core 2_, page 178."
```

```encounter-table
name: Grioth Scout
creatures:
  - 1: Grioth Scout
```
