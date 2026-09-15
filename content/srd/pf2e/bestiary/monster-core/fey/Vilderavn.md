---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3229"
socialImage: og-image.png
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
    desc: "+28; greater darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +32, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +29, Heraldry Lore +26, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +24, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +32, Warfare Lore +26"
abilityMods: [8, 6, 5, 4, 4, 7]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +25; __Ref__: +30; __Will__: +28"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 10"
abilities_mid:
  - name: "Aura of Disquietude"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 30 feet, DC 35. As frightful presence, plus a creature [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] by the aura becomes suspicious; it doesn't count any other creature as its ally and can't [[srd/pf2e/compendium/rules-elements/actions/player-core#Aid|Aid]] or flank. On a critical failure, the creature also can't be a willing target for harmless or helpful magic."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatsword_ +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 3d12+16 slashing plus bloodbird"
  - name: "Melee"
    desc: "⬻ jaws +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 3d8+16 piercing plus bloodbird"
  - name: "Melee"
    desc: "⬻ talon +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 3d8+16 slashing plus bloodbird"
abilities_bot:
  - name: "Bloodbird"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) A creature hit by a vilderavn's melee attack becomes cursed. It takes 2d6 persistent bleed damage that's difficult to stanch. The DC to stop the bleeding using [[srd/pf2e/compendium/rules-elements/actions/player-core#Administer First Aid|Administer First Aid]] is 35, and healing the creature to full HP doesn't automatically end the bleeding. Removing the curse ends the bleeding."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The vilderavn takes on the appearance of a Small or Medium humanoid, wolf, dire wolf, or hybrid with both raven and wolf parts. The vilderavn can only use their jaws attack when in a form with a wolf's head, and their talon attack in a form with raven qualities. They can instead assume their raven knight form: a Medium humanoid in black full plate carrying a greatsword. They can use their jaws or talon Strikes only in a form that has that body part, and their greatsword only in knight form."
  - name: "Souleater"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) If the vilderavn kills a [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]] with a critical hit using their jaws Strike, they rip out and devour the target's heart and soul as part of the attack. While the target is dead, the vilderavn can Change Shape into the target's form, gaining a +4 status bonus to [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|impersonate]] the target. If magic would resurrect the creature, the caster must succeed at a DC 34 counteract check to extract the target's soul from the vilderavn; otherwise, the spell fails. The Creation of Vilderavns Legends say a fey lord created the vilderavns as a weapon against those who ruined the land with their iron armaments. Vilderavns would exploit the hubris of mortals and devour their souls after death. With this goal, vilderavns hid in various forms to watch and learn human ways, and they executed their calling with great subtlety but no mercy. No mortal knows if this legend is true or spread by vilderavns to imply a purpose for their heartless cruelty."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __5th__ [[srd/pf2e/compendium/spells/rank-4/Outcast's Curse|Outcast's Curse]] (at will), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]], [[srd/pf2e/compendium/spells/rank-5/Wave of Despair|Wave of Despair]] (at will), [[srd/pf2e/compendium/spells/rank-4/Rewrite Memory|Rewrite Memory]] - __8th__ [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 340."
```

```encounter-table
name: Vilderavn
creatures:
  - 1: Vilderavn
```
