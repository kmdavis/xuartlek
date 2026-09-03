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
    desc: "Perception +28; greater darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +32, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +29, Heraldry Lore +26, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +32, Warfare Lore +26"
abilityMods: [8, 6, 5, 4, 4, 7]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +25; __Ref__: +30; __Will__: +28"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 10"
abilities_mid:
  - name: "Aura of Disquietude"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 30 feet, DC 35. As frightful presence, plus a creature [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] by the aura becomes suspicious; it doesn't count any other creature as its ally and can't [[srd/pf2e/compendium/rules-elements/actions/player-core#Aid|Aid]] or flank. On a critical failure, the creature also can't be a willing target for harmless or helpful magic."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatsword_ +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 3d12+16 slashing plus bloodbird"
  - name: "Melee"
    desc: "⬻ jaws +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d8+16 piercing plus bloodbird"
  - name: "Melee"
    desc: "⬻ talon +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d8+16 slashing plus bloodbird"
abilities_bot:
  - name: "Bloodbird"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) A creature hit by a vilderavn's melee attack becomes cursed. It takes 2d6 persistent bleed damage that's difficult to stanch. The DC to stop the bleeding using [[srd/pf2e/compendium/rules-elements/actions/player-core#Administer First Aid|Administer First Aid]] is 35, and healing the creature to full HP doesn't automatically end the bleeding. Removing the curse ends the bleeding."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The vilderavn takes on the appearance of a Small or Medium humanoid, wolf, dire wolf, or hybrid with both raven and wolf parts. The vilderavn can only use their jaws attack when in a form with a wolf's head, and their talon attack in a form with raven qualities. They can instead assume their raven knight form: a Medium humanoid in black full plate carrying a greatsword. They can use their jaws or talon Strikes only in a form that has that body part, and their greatsword only in knight form."
  - name: "Souleater"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) If the vilderavn kills a [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] with a critical hit using their jaws Strike, they rip out and devour the target's heart and soul as part of the attack. While the target is dead, the vilderavn can Change Shape into the target's form, gaining a +4 status bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|impersonate]] the target. If magic would resurrect the creature, the caster must succeed at a DC 34 counteract check to extract the target's soul from the vilderavn; otherwise, the spell fails. The Creation of Vilderavns Legends say a fey lord created the vilderavns as a weapon against those who ruined the land with their iron armaments. Vilderavns would exploit the hubris of mortals and devour their souls after death. With this goal, vilderavns hid in various forms to watch and learn human ways, and they executed their calling with great subtlety but no mercy. No mortal knows if this legend is true or spread by vilderavns to imply a purpose for their heartless cruelty."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __5th__ [[srd/pf2e/compendium/spells/rank-4/outcasts-curse|Outcast's Curse]] (at will), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] (at will), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]], [[srd/pf2e/compendium/spells/rank-5/wave-of-despair|Wave of Despair]] (at will), [[srd/pf2e/compendium/spells/rank-4/rewrite-memory|Rewrite Memory]] - __8th__ [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 340."
```

```encounter-table
name: Vilderavn
creatures:
  - 1: Vilderavn
```
