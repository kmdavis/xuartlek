---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Maftet Guardian"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/maftet
  - pf2e/creature/trait/medium
statblock: inline
name: "Maftet Guardian"
level: 6
source: "Monster Core 2"
aon_id: "creature-4470"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4470"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Maftet Guardian"
level: "Creature 6"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Maftet"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Sphinx"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Ruins Lore]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [5, 3, 4, 3, 2, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/sword/scimitar|Scimitar]] (2)"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +15; __Will__: +12"
hp: 90
health:
  - name: "HP"
    desc: "90"
abilities_mid:
  - name: "Runic Resistance"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]])"
  - name: "Trigger"
    desc: "The maftet takes damage from a Strike or spell effect"
  - name: "Effect"
    desc: "The maftet's protective runic tattoos glow, granting them [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Resistance|resistance]] 5 to one damage type dealt by the triggering attack. This resistance applies against the triggering effect and lasts for 1 minute or until the maftet uses this ability again, whichever comes first. If the triggering effect deals multiple damage types, the maftet chooses which type to resist."
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scimitar_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]]) __Damage__ 2d6+8 slashing"
abilities_bot:
  - name: "Paired Strike"
    desc: "Requirements__ The maftet is wielding two scimitars__ ⬺"
  - name: "Effect"
    desc: "The maftet makes two Strikes against the same target, one with each of their scimitars. The maftet combines the damage of any attacks that hit and applies resistances and weaknesses only once. This counts as one attack when calculating the maftet's multiple attack penalty."
  - name: "Powerful Scimitars"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]]) Any non-magical scimitar becomes a _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/sword/scimitar|scimitar]]_ while a maftet wields it."
  - name: "Raptor Dive"
    desc: "⬽"
  - name: "Requirements"
    desc: "The maftet is flying at least 10 feet above the target"
  - name: "Effect"
    desc: "The maftet Flies up to twice their [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Fly Speed|fly Speed]] and makes a Paired Strike at the end of the movement. If both Strikes hit, the target is also knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. Shared Duties Occasionally, maftets and [[srd/pf2e/compendium/gm/creature-families/girtablilu|girtablilus]] share a home. Since both groups respect locales and their history, they usually form a tacit partnership to guard ruins in tandem, with maftets keeping watch from the skies while girtablilus patrol the ground."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 23 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/sigil|Sigil]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/sanctuary|Sanctuary]] (×3), [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]]"
sourcebook: "_Monster Core 2_, page 218."
```

```encounter-table
name: Maftet Guardian
creatures:
  - 1: Maftet Guardian
```
