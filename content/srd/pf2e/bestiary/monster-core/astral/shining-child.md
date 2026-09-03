---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shining Child"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/astral
  - pf2e/creature/trait/medium
statblock: inline
name: "Shining Child"
level: 12
source: "Monster Core"
aon_id: "creature-3190"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3190"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Shining Child"
level: "Creature 12"
size: "Medium"
trait_01: "Astral"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision"
languages: "Aklo; telepathy 120 feet"
skills:
  - name: "Skills"
    desc: "Arcana +18, Deception +23, Diplomacy +21, Intimidation +21, Occultism +18"
abilityMods: [2, 5, 6, 2, 5, 7]
abilities_top:
  - name: "Radiance Dependence"
    desc: "The shining child is off-guard while in areas of darkness."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +19; __Will__: +19"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ blinded, dazzled, fire"
abilities_mid:
  - name: "Blinding Aura"
    desc: "(arcane, aura, incapacitation, light) 60 feet. The shining child sheds bright light. Any creature that starts its turn in the aura must succeed at a DC 29 Fortitude save. If it fails, it is blinded for 1 minute, and if it critically fails, it's permanently blinded. A creature that succeeds at its save is temporarily immune to this effect for 24 hours."
  - name: "Overwhelming Light"
    desc: "⬲ (light)"
  - name: "Trigger"
    desc: "The shining child enters an area of magical darkness or begins its turn in an area of magical darkness"
  - name: "Effect"
    desc: "The shining child attempts to counteract the magical darkness (counteract rank 7, counteract modifier +23)."
speed: "30 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +25 (Agile, Finesse, Magical) __Damage__ 3d4+5 bludgeoning plus 4d6 fire and 2d4 persistent fire"
  - name: "Melee"
    desc: "⬻ fire ray +25 (Arcane, Magical, range 100 feet) __Damage__ 3d10+3 fire, plus 2d10 vitality damage if the target is undead"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33 - __Cantrips (6th)__ Light - __2nd__ Illusory Object (at will) - __4th__ Translocate (at will) - __5th__ False Vision, Mirage, Translocate - __6th__ Dispel Magic, Vibrant Pattern, Wall of Force - __7th__ Sunburst (x2) Ancient Guardians The practice of conjuring and binding shining children to serve as guardians of important locations was a popular one in Thassilon. Even today, thousands of years after this empire's fall, adventurers can still encounter shining children in ancient ruins, guarding treasures and forgotten lore from the distant past."
sourcebook: "_Monster Core_, page 308."
```

```encounter-table
name: Shining Child
creatures:
  - 1: Shining Child
```
