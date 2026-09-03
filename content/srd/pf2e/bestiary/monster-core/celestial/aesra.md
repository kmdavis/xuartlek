---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aesra"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Aesra"
level: 7
source: "Monster Core"
aon_id: "creature-2834"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2834"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Aesra"
level: "Creature 7"
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Utopian; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +14"
abilityMods: [5, 2, 4, 1, 2, 5]
abilities_top:
  - name: "Items"
    desc: "Full Plate"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +11; __Will__: +15 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]"
hp: 100
health:
  - name: "HP"
    desc: "100; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 10"
abilities_mid:
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 10 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flame of justice +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d10+5 slashing plus 1d6 fire and flame of justice"
  - name: "Ranged"
    desc: "⬻ flame of justice +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 30 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d10+5 slashing plus 1d6 fire and flame of justice"
abilities_bot:
  - name: "Flame of Justice"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]]) An aesra's spirit of righteousness manifests as a two-handed sword of fire. If disarmed or thrown as a ranged weapon, the flame of justice vanishes after landing or dealing damage and reappears in the aesra's hands again instantly. On a critical hit, the target also takes 2d6 persistent fire damage."
  - name: "Flaming Slash"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The aesra sweeps their sword, creating a 15-foot cone of sacred flame that deals 5d6 fire damage with a DC 23 basic Reflex save."
  - name: "Maintain Formation"
    desc: "When an aesra casts [[srd/pf2e/compendium/spells/rank-4/translocate|_translocate_]], they can bring an adjacent willing [[srd/pf2e/compendium/gm/creature-families/archon|archon]] along with them. That archon appears in an empty space adjacent to the aesra's new space."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/message|Message]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] (×3) - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 27."
```

```encounter-table
name: Aesra
creatures:
  - 1: Aesra
```
