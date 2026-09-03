---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vilderavn"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Vilderavn"
level: 16
source: "Monster Core"
aon_id: "creature-3229"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3229"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vilderavn"
level: "Creature 16"
size: "Medium"
trait_01: "Fey"
trait_02: "Rare"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; greater darkvision, _truesight_"
languages: "Aklo, Common, Diabolic, Fey; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Athletics +32, Deception +29, Heraldry Lore +26, Society +24, Stealth +32, Warfare Lore +26"
abilityMods: [8, 6, 5, 4, 4, 7]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +25; __Ref__: +30; __Will__: +28"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ curse, death effects, drained, fear; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Aura of Disquietude"
    desc: "(aura, emotion, fear, mental) 30 feet, DC 35. As frightful presence, plus a creature frightened by the aura becomes suspicious; it doesn't count any other creature as its ally and can't Aid or flank. On a critical failure, the creature also can't be a willing target for harmless or helpful magic."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatsword_ +34 (Magical, versatile P) __Damage__ 3d12+16 slashing plus bloodbird"
  - name: "Melee"
    desc: "⬻ jaws +32 (Magical) __Damage__ 3d8+16 piercing plus bloodbird"
  - name: "Melee"
    desc: "⬻ talon +32 (Agile, Magical) __Damage__ 3d8+16 slashing plus bloodbird"
abilities_bot:
  - name: "Bloodbird"
    desc: "(Curse, Occult) A creature hit by a vilderavn's melee attack becomes cursed. It takes 2d6 persistent bleed damage that's difficult to stanch. The DC to stop the bleeding using Administer First Aid is 35, and healing the creature to full HP doesn't automatically end the bleeding. Removing the curse ends the bleeding."
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Occult, Polymorph) The vilderavn takes on the appearance of a Small or Medium humanoid, wolf, dire wolf, or hybrid with both raven and wolf parts. The vilderavn can only use their jaws attack when in a form with a wolf's head, and their talon attack in a form with raven qualities. They can instead assume their raven knight form: a Medium humanoid in black full plate carrying a greatsword. They can use their jaws or talon Strikes only in a form that has that body part, and their greatsword only in knight form."
  - name: "Souleater"
    desc: "(Occult) If the vilderavn kills a humanoid with a critical hit using their jaws Strike, they rip out and devour the target's heart and soul as part of the attack. While the target is dead, the vilderavn can Change Shape into the target's form, gaining a +4 status bonus to Deception checks to impersonate the target. If magic would resurrect the creature, the caster must succeed at a DC 34 counteract check to extract the target's soul from the vilderavn; otherwise, the spell fails. The Creation of Vilderavns Legends say a fey lord created the vilderavns as a weapon against those who ruined the land with their iron armaments. Vilderavns would exploit the hubris of mortals and devour their souls after death. With this goal, vilderavns hid in various forms to watch and learn human ways, and they executed their calling with great subtlety but no mercy. No mortal knows if this legend is true or spread by vilderavns to imply a purpose for their heartless cruelty."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __5th__ Outcast's Curse (at will), Suggestion (at will), Translocate, Wave of Despair (at will), Rewrite Memory - __8th__ Suggestion - __Constant (6th)__ Truesight, Truespeech"
sourcebook: "_Monster Core_, page 340."
```

```encounter-table
name: Vilderavn
creatures:
  - 1: Vilderavn
```
