---
obsidianUIMode: preview
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
aon_id: "creature-2817"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2817"
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
    desc: "Perception +26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +24, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +26, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +24"
abilityMods: [8, 4, 5, 4, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/hammer/warhammer|warhammer]]_"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +26; __Will__: +22 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 285
health:
  - name: "HP"
    desc: "285; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 15"
abilities_mid:
  - name: "Traveler's Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 20 feet. Creatures in the tabellia's aura are immune to ambient environmental damage from any plane, including severe and extreme heat and cold as well as more otherworldly dangers. The tabellia is never [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to creatures within their aura."
  - name: "Messenger's Amnesty"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A tabellia with a message to deliver is continually protected by the effect of [[srd/pf2e/compendium/spells/rank-1/sanctuary|_sanctuary_]] (DC 32). If the angel breaks the sanctuary, the effect returns if the angel ceases hostility for 10 minutes."
speed: "40 feet, fly 75 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _holy_ _warhammer_ +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 2d8+14 bludgeoning plus 1d4 spirit (or 2d4 spirit vs. an [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] target)"
abilities_bot:
  - name: "Stunning Strike"
    desc: "⬻"
  - name: "Requirements"
    desc: "The tabellia hit a foe earlier this turn with a weapon Strike"
  - name: "Effect"
    desc: "The tabellia makes a weapon Strike against the foe. On a success, the foe must also succeed at a DC 34 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]] (or stunned 2 on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/ring-of-truth|Ring of Truth]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-6/blessed-boundary|Blessed Boundary]], [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-2/clear-mind|Clear Mind]], [[srd/pf2e/compendium/spells/rank-7/divine-decree|Divine Decree]], [[srd/pf2e/compendium/spells/rank-4/divine-wrath|Divine Wrath]], [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 36 - __1st__ [[srd/pf2e/compendium/spells/rituals/angelic-messenger|Angelic Messenger]]"
sourcebook: "_Monster Core_, page 16."
```

```encounter-table
name: Tabellia
creatures:
  - 1: Tabellia
```
