---
noteType: pf2eMonster
aliases: "Anguished Flame"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/light
  - pf2e/creature/trait/large
statblock: inline
name: "Anguished Flame"
level: 13
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4523"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Anguished Flame"
level: "Creature 13"
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Light"
modifier: 28
perception:
  - name: "Perception"
    desc: "+28"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Pyric|Pyric]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +27, [[srd/pf2e/compendium/rules-elements/skills/Lore|Deity Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +27, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +27, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +23, [[srd/pf2e/compendium/rules-elements/skills/Lore|Plane of Fire Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +23"
abilityMods: [5, 7, 5, 4, 6, 8]
abilities_top:
  - name: "Eternal Luminosity"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Light|light]]) An anguished flame naturally sheds brilliant light like a [[srd/pf2e/compendium/equipment/adventuring-gear/Torch|torch]]. When other creatures target the anguished flame, they ignore the [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] condition from [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Perception and Detection#Darkness|darkness]], [[srd/pf2e/books/gm-core/chapter-2-building-games/Environment#Fog|fog]], mist, and [[srd/pf2e/books/gm-core/chapter-2-building-games/Environment#Smoke|smoke]]."
  - name: "Purifying Flame"
    desc: "An anguished flame can [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Wounds|Treat Wounds]] without a [[srd/pf2e/compendium/equipment/adventuring-gear/Healer's Toolkit|healer's toolkit]], instead healing the wounded with the gentle light of their touch."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +24; __Will__: +25"
hp: 260
health:
  - name: "HP"
    desc: "260; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]] 10"
abilities_mid:
  - name: "Solar Flare"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) 30 feet. When a creature ends its turn in the aura, it takes 2d6 fire damage (DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save). On a failed save, it also becomes [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] until the end of its next turn. The anguished flame can activate or deactivate this aura by using a single action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]] trait."
  - name: "Vulnerable to Blasphemy"
    desc: "If a creature the anguished flame can see and hear spends 1 action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|linguistic]] trait blaspheming against the gods, the anguished flame becomes [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1 until they Collect a Prayer from that creature."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flaming wing +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]) __Damage__ 3d10+11 fire"
  - name: "Ranged"
    desc: "⬻ shining ray +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Light|light]], range increment 60 feet) __Damage__ 3d6+6 fire plus 3d6 spirit"
abilities_bot:
  - name: "Collect Prayer"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) The anguished flame compels a creature they can see within 60 feet, who must attempt a DC 30 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature immediately uses its reaction to pray."
  - name: "Failure"
    desc: "The creature prays. It is [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] 1 and can't use reactions for 1 minute."
  - name: "Critical Failure"
    desc: "As failure, but the creature is slowed 2."
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]])"
  - name: "Requirements"
    desc: "The anguished flame's solar flare aura is active"
  - name: "Effect"
    desc: "The anguished flame fixes their fiery eyes on a creature they can see within 30 feet. The target must immediately attempt a Fortitude save against the anguished flame's solar flare. If the creature was already [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] by solar flare before attempting its save, a failed save causes it to become [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] until the end of its next turn. Ages In Darkness Over the eon of Lord [[srd/pf2e/compendium/deities/elemental-lords/Atreia|Atreia's]] imprisonment inside the Garnet Brand, temples to the Lambent King lay dormant and decaying across the [[srd/pf2e/compendium/gm/Planes#Plane of Fire|Plane of Fire]], and within those temples, his children, known as ygnaires, began to fade. Without the light of their Lord of Fire, these elementals who waned became known as anguished flames. They eventually turned to unmoving bronze, frozen until Atreia's light shone down on them again."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __7th__ [[srd/pf2e/compendium/spells/rank-3/Fireball|Fireball]] (×2), [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 30."
```

```encounter-table
name: Anguished Flame
creatures:
  - 1: Anguished Flame
```
