---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ifrit"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/large
statblock: inline
name: "Ifrit"
level: 9
source: "Monster Core"
aon_id: "creature-3006"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3006"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ifrit"
level: "Creature 9"
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Genie"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "Common, Pyric; _truespeech_"
skills:
  - name: "Skills"
    desc: "Arcana +14, Athletics +22, Crafting +14, Deception +19, Diplomacy +17, Intimidation +19, Society +14"
abilityMods: [5, 3, 4, 1, 2, 4]
abilities_top:
  - name: "Items"
    desc: "Breastplate, _+1 striking scimitar_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +18; __Ref__: +17; __Will__: +20"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ fire; __Weaknesses__ cold 10, water 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scimitar_ +21 (Fire, Forceful, Magical, reach 10 feet, Sweep) __Damage__ 2d6+11 slashing plus 2d6 fire"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, Magical, reach 10 feet) __Damage__ 1d4+11 bludgeoning plus 2d6 fire"
abilities_bot:
  - name: "Burning Grasp"
    desc: "(Fire) When the ifrit grabsor restrainsa creature that creature takes 2d6 fire damage and takes 2d6 fire damage at the end of each of its turns until freed."
  - name: "Change Shape"
    desc: "⬻ (Arcane, Concentrate, Polymorph) The ifrit transforms into a Small or Medium fire elemental or reptile, such as a snake. This doesn't affect their statistics but could change the damage type of their Strikes."
  - name: "Combat Grab"
    desc: "⬻"
  - name: "Requirements"
    desc: "The ifrit has a hand free"
  - name: "Effect"
    desc: "The ifrit makes a melee Strike. If the Strike hits, the target is grabbed in the ifrit's free hand."
  - name: "Wings of Flame"
    desc: "⬻ (Arcane, Fire) The ifrit grows flaming wings from their back. They gain a fly Speed of 35 feet for 1 minute. The flames also create an aura in a 5-foot emanation around the ifrit. Any creature that ends its turn in the aura takes 2d6 fire damage with a DC 25 basic Reflex save. Ifrit Shuyookhs Ifrit shuyookhs twist the phrasing of wishes to maximize suffering. A wisher for a thousand pounds of gemstones might have the gems delivered as a bone-crushing avalanche. Ifrit shuyookhs add the following innate spells: __7th__ _volcanic eruption_; __5th__ _fireball_ (at will)."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 27, attack +19 - __Cantrips (5th)__ Detect Magic, Ignition - __4th__ Fireball, Invisibility (×2) - __7th__ Interplanar Teleport (to Astral Plane; Elemental Planes; or the Universe only) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 159."
```

```encounter-table
name: Ifrit
creatures:
  - 1: Ifrit
```
