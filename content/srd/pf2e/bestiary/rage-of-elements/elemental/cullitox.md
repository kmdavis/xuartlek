---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cullitox"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/small
statblock: inline
name: "Cullitox"
level: 3
source: "Rage of Elements"
aon_id: "creature-2623"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2623"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Cullitox"
level: "Creature 3"
size: "Small"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; crystal scent (imprecise) 60 feet, darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [2, 2, 1, -2, 2, 1]
abilities_top:
  - name: "Crystal Scent"
    desc: "A cullitox can sense crystals or gems within 60 feet as if using the scent ability."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +9; __Will__: +9"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "25 feet, burrow 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ crystal stinger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+5 piercing"
  - name: "Ranged"
    desc: "⬻ tail spike +10 (range increment 60 feet) __Damage__ 1d6+5 piercing and sink into stone"
abilities_bot:
  - name: "Rock Stride"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|Teleportation]]) The cullitox phases into adjacent rock that is large enough to accommodate it. Then, the cullitox senses similar or larger rocks within 60 feet and emerges from one. The cullitox can't use this ability again for 1 minute."
  - name: "Sink into Stone"
    desc: "The spikes fired from a cullitox's tail phase into stone, pinning enemies in place. Enemies standing on or adjacent to a stone surface who are struck by a critical hit on a tail spike Strike are [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]]. The DC to Escape is 17. Internal Gems When a cullitox dies, its body breaks into fragments of crystal. Some of these pieces are valuable, but potentially more lucrative are the gems the cullitox has stored inside its body to produce offspring. It takes semiprecious and precious stones worth 500 gp to produce an infant cullitox, though most slain cullitoxes have only a fraction of this amount stored. Once the stones become a new cullitox, they transform into the crystal of the infant's body, no longer the treasured material they once were."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]] (chiming; clinking; or rattling sounds only), [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]]"
sourcebook: "_Rage of Elements_, page 103."
```

```encounter-table
name: Cullitox
creatures:
  - 1: Cullitox
```
