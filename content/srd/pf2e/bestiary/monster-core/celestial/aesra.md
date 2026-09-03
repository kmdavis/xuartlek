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
languages: "Diabolic, Draconic, Empyrean, Utopian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +14, Diplomacy +16, Intimidation +16, Religion +13, Survival +14"
abilityMods: [5, 2, 4, 1, 2, 5]
abilities_top:
  - name: "Items"
    desc: "Full Plate"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +11; __Will__: +15 +1 status to all saves vs. magical"
hp: 100
health:
  - name: "HP"
    desc: "100; __Immunities__ fear; __Resistances__ fire 15; __Weaknesses__ unholy 10"
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
    desc: "⬻ flame of justice +18 (Holy, Magical, versatile P) __Damage__ 2d10+5 slashing plus 1d6 fire and flame of justice"
  - name: "Ranged"
    desc: "⬻ flame of justice +15 (Holy, Magical, range increment 30 feet, versatile P) __Damage__ 2d10+5 slashing plus 1d6 fire and flame of justice"
abilities_bot:
  - name: "Flame of Justice"
    desc: "(Divine, Holy) An aesra's spirit of righteousness manifests as a two-handed sword of fire. If disarmed or thrown as a ranged weapon, the flame of justice vanishes after landing or dealing damage and reappears in the aesra's hands again instantly. On a critical hit, the target also takes 2d6 persistent fire damage."
  - name: "Flaming Slash"
    desc: "⬺ (Divine, Fire, Holy, Manipulate) The aesra sweeps their sword, creating a 15-foot cone of sacred flame that deals 5d6 fire damage with a DC 23 basic Reflex save."
  - name: "Maintain Formation"
    desc: "When an aesra casts _translocate_, they can bring an adjacent willing archon along with them. That archon appears in an empty space adjacent to the aesra's new space."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24 - __Cantrips (4th)__ Light, Message - __1st__ Sure Strike (×3) - __4th__ Translocate (at will) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 27."
```

```encounter-table
name: Aesra
creatures:
  - 1: Aesra
```
