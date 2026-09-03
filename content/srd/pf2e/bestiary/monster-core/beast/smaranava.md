---
obsidianUIMode: preview
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
aon_id: "creature-3103"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3103"
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
    desc: "Perception +15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +16, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +16, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19"
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
    desc: "⬻ fangs +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d10+5 piercing plus smaranava venom"
  - name: "Melee"
    desc: "⬻ tail +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+5 bludgeoning plus coils of knowledge"
abilities_bot:
  - name: "Coils of Knowledge"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/force|Force]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) The naga's grip is more spiritual than physical. A creature hit by a smaranava's tail must succeed at a DC 25 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the tail until they [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]], the naga releases them with an Interact action, or the naga dies. A captive takes a –4 status penalty to Escape, but can choose to attempt an [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] or [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] check to Escape instead of the usual options without taking this penalty."
  - name: "Constrict"
    desc: "⬻ 2d8+5 bludgeoning, DC 25"
  - name: "Smaranava Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) When a [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] creature succeeds at a saving throw against this poison, it is immediately cured"
  - name: "Saving Throw"
    desc: "DC 25 Will"
  - name: "Maximum Duration"
    desc: "5 minutes"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 round)"
  - name: "Stage 2"
    desc: "slowed 2 (1 round)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] with no Perception check to wake up (1 minute)"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-3/lightning-bolt|Lightning Bolt]], [[srd/pf2e/compendium/spells/rank-3/mind-reading|Mind Reading]]"
sourcebook: "_Monster Core_, page 236."
```

```encounter-table
name: Smaranava
creatures:
  - 1: Smaranava
```
