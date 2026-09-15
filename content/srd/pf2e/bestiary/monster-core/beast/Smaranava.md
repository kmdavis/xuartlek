---
noteType: pf2eMonster
aliases: "Smaranava"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Smaranava"
level: 7
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3103"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Smaranava"
level: "Creature 7"
size: "Large"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +16, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +19"
abilityMods: [2, 6, 4, 3, 2, 3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +15; __Ref__: +17; __Will__: +15"
hp: 115
health:
  - name: "HP"
    desc: "115"
speed: "30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d10+5 piercing plus smaranava venom"
  - name: "Melee"
    desc: "⬻ tail +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d8+5 bludgeoning plus coils of knowledge"
abilities_bot:
  - name: "Coils of Knowledge"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Force|Force]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) The naga's grip is more spiritual than physical. A creature hit by a smaranava's tail must succeed at a DC 25 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] by the tail until they [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]], the naga releases them with an Interact action, or the naga dies. A captive takes a –4 status penalty to Escape, but can choose to attempt an [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] or [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] check to Escape instead of the usual options without taking this penalty."
  - name: "Constrict"
    desc: "⬻ 2d8+5 bludgeoning, DC 25"
  - name: "Smaranava Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]]) When a [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] creature succeeds at a saving throw against this poison, it is immediately cured"
  - name: "Saving Throw"
    desc: "DC 25 Will"
  - name: "Maximum Duration"
    desc: "5 minutes"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]] (1 round)"
  - name: "Stage 2"
    desc: "slowed 2 (1 round)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] with no Perception check to wake up (1 minute)"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-3/Lightning Bolt|Lightning Bolt]], [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]]"
sourcebook: "_Monster Core_, page 236."
```

```encounter-table
name: Smaranava
creatures:
  - 1: Smaranava
```
