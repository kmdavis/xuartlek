---
noteType: pf2eMonster
aliases: "Tabellia"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Tabellia"
level: 14
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2817"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tabellia"
level: "Creature 14"
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 26
perception:
  - name: "Perception"
    desc: "+26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +24, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +26, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +24"
abilityMods: [8, 4, 5, 4, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/hammer/Warhammer|warhammer]]_"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +26; __Will__: +22 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 285
health:
  - name: "HP"
    desc: "285; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 15"
abilities_mid:
  - name: "Traveler's Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) 20 feet. Creatures in the tabellia's aura are immune to ambient environmental damage from any plane, including severe and extreme heat and cold as well as more otherworldly dangers. The tabellia is never [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to creatures within their aura."
  - name: "Messenger's Amnesty"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A tabellia with a message to deliver is continually protected by the effect of [[srd/pf2e/compendium/spells/rank-1/Sanctuary|_sanctuary_]] (DC 32). If the angel breaks the sanctuary, the effect returns if the angel ceases hostility for 10 minutes."
speed: "40 feet, fly 75 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _holy_ _warhammer_ +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 2d8+14 bludgeoning plus 1d4 spirit (or 2d4 spirit vs. an [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] target)"
abilities_bot:
  - name: "Stunning Strike"
    desc: "⬻"
  - name: "Requirements"
    desc: "The tabellia hit a foe earlier this turn with a weapon Strike"
  - name: "Effect"
    desc: "The tabellia makes a weapon Strike against the foe. On a success, the foe must also succeed at a DC 34 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 1]] (or stunned 2 on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Ring of Truth|Ring of Truth]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-6/Blessed Boundary|Blessed Boundary]], [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-2/Clear Mind|Clear Mind]], [[srd/pf2e/compendium/spells/rank-7/Divine Decree|Divine Decree]], [[srd/pf2e/compendium/spells/rank-4/Divine Wrath|Divine Wrath]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 36 - __1st__ [[srd/pf2e/compendium/spells/rituals/Angelic Messenger|Angelic Messenger]]"
sourcebook: "_Monster Core_, page 16."
```

```encounter-table
name: Tabellia
creatures:
  - 1: Tabellia
```
