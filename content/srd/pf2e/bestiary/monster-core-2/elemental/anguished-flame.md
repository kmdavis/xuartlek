---
obsidianUIMode: preview
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
aon_id: "creature-4523"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4523"
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
    desc: "Perception +28"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +27, [[srd/pf2e/compendium/rules-elements/skills/lore|Deity Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +27, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +27, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +23, [[srd/pf2e/compendium/rules-elements/skills/lore|Plane of Fire Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +23"
abilityMods: [5, 7, 5, 4, 6, 8]
abilities_top:
  - name: "Eternal Luminosity"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]]) An anguished flame naturally sheds brilliant light like a [[srd/pf2e/compendium/equipment/adventuring-gear/torch|torch]]. When other creatures target the anguished flame, they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from [[srd/pf2e/books/player-core/chapter-8-playing-the-game/perception-and-detection#Darkness|darkness]], [[srd/pf2e/books/gm-core/chapter-2-building-games/environment#Fog|fog]], mist, and [[srd/pf2e/books/gm-core/chapter-2-building-games/environment#Smoke|smoke]]."
  - name: "Purifying Flame"
    desc: "An anguished flame can [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Wounds|Treat Wounds]] without a [[srd/pf2e/compendium/equipment/adventuring-gear/healers-toolkit-expanded|healer's toolkit]], instead healing the wounded with the gentle light of their touch."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +24; __Will__: +25"
hp: 260
health:
  - name: "HP"
    desc: "260; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] 10"
abilities_mid:
  - name: "Solar Flare"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. When a creature ends its turn in the aura, it takes 2d6 fire damage (DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save). On a failed save, it also becomes [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] until the end of its next turn. The anguished flame can activate or deactivate this aura by using a single action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait."
  - name: "Vulnerable to Blasphemy"
    desc: "If a creature the anguished flame can see and hear spends 1 action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]] trait blaspheming against the gods, the anguished flame becomes [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 until they Collect a Prayer from that creature."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flaming wing +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) __Damage__ 3d10+11 fire"
  - name: "Ranged"
    desc: "⬻ shining ray +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]], range increment 60 feet) __Damage__ 3d6+6 fire plus 3d6 spirit"
abilities_bot:
  - name: "Collect Prayer"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) The anguished flame compels a creature they can see within 60 feet, who must attempt a DC 30 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature immediately uses its reaction to pray."
  - name: "Failure"
    desc: "The creature prays. It is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 and can't use reactions for 1 minute."
  - name: "Critical Failure"
    desc: "As failure, but the creature is slowed 2."
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]])"
  - name: "Requirements"
    desc: "The anguished flame's solar flare aura is active"
  - name: "Effect"
    desc: "The anguished flame fixes their fiery eyes on a creature they can see within 30 feet. The target must immediately attempt a Fortitude save against the anguished flame's solar flare. If the creature was already [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] by solar flare before attempting its save, a failed save causes it to become [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] until the end of its next turn. Ages In Darkness Over the eon of Lord Atreia's imprisonment inside the Garnet Brand, temples to the Lambent King lay dormant and decaying across the [[srd/pf2e/compendium/gm/planes#Plane of Fire|Plane of Fire]], and within those temples, his children, known as ygnaires, began to fade. Without the light of their Lord of Fire, these elementals who waned became known as anguished flames. They eventually turned to unmoving bronze, frozen until Atreia's light shone down on them again."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __7th__ [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]] (×2), [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 30."
```

```encounter-table
name: Anguished Flame
creatures:
  - 1: Anguished Flame
```
