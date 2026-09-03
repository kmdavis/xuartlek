---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Caligni Caller"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/caligni
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Caligni Caller"
level: 6
source: "Monster Core 2"
aon_id: "creature-4289"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4289"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Caligni Caller"
level: "Creature 6"
size: "Medium"
trait_01: "Caligni"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; greater darkvision, light blindness"
languages: "Caligni, [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +9, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [2, 5, 1, 1, 1, 4]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/knife/dagger|Dagger]]"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +9; __Ref__: +15; __Will__: +11"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Death Umbra"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/darkness|darkness]]) When the caller dies, an explosion of shadow devours their body. Each creature in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must attempt a DC 22 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 for 1 minute."
  - name: "Failure"
    desc: "The creature is enfeebled 2 and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 for 1 minute."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing plus 1d6 void"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The caller's Strikes deal an additional 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/void-warp|Void Warp]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/chilling-darkness|Chilling Darkness]] (×2), [[srd/pf2e/compendium/spells/rank-1/grim-tendrils|Grim Tendrils]] (×3) - __4th__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/umbral-journey|Umbral Journey]]"
  - name: "Rituals"
    desc: "DC 24 - __3rd__ [[srd/pf2e/compendium/spells/rituals/owb-pact|Owb Pact]]"
sourcebook: "_Monster Core 2_, page 65."
```

```encounter-table
name: Caligni Caller
creatures:
  - 1: Caligni Caller
```
