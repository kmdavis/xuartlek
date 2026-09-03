---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pakalchi"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Pakalchi"
level: 9
source: "Monster Core 2"
aon_id: "creature-4536"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4536"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Pakalchi"
level: "Creature 9"
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, _truesight_"
languages: "Chthonian, Diabolic, Empyrean, Requian; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +18, Deception +21, Diplomacy +21, Intimidation +21, Stealth +18"
abilityMods: [4, 5, 4, 2, 3, 6]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the _binding circle_ ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +17; __Ref__: +18; __Will__: +20"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ fear, poison; __Weaknesses__ holy 5"
abilities_mid:
  - name: "Entangling Train"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature moves adjacent to the pakalchi"
  - name: "Effect"
    desc: "Writhing, pitch-black vines wrap around the creature. The creature takes 1d6 slashing damage and a –15-foot circumstance penalty to its Speeds until the end of its next turn."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ vine +18 (Finesse, magical, reach 10 feet, versatile P, unholy) __Damage__ 2d10+6 slashing plus 1d6 spirit, 1d6 persistent bleed, and betrayal toxin"
  - name: "Melee"
    desc: "⬻ claw +18 (Agile, finesse, magical, unholy) __Damage__ 2d10+6 slashing plus 1d6 spirit"
  - name: "Ranged"
    desc: "⬻ thorn +18 (Agile, magical, range increment 50 feet, unholy) __Damage__ 2d4+6 piercing plus 1d6 spirit, 1d6 persistent bleed, and betrayal toxin"
abilities_bot:
  - name: "Betrayal Toxin"
    desc: "(Divine, mental, poison) A creature affected by betrayal toxin hears whispers of incessant doubt in their head and can't treat any creature as their ally"
  - name: "Saving Throw"
    desc: "DC 28 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "stupefied 2 (1 round)"
  - name: "Skip Between"
    desc: "⬻ (Divine, teleportation) The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30 - __Cantrips (5th)__ Detect Magic - __5th__ Calm, Charm, Suggestion (at will) - __6th__ Dominate - __7th__ Mask of Terror (self only) - __Constant (6th)__ Truesight, Truespeech"
sourcebook: "_Monster Core 2_, page 276."
```

```encounter-table
name: Pakalchi
creatures:
  - 1: Pakalchi
```
