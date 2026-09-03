---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tupilaq"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/small
statblock: inline
name: "Tupilaq"
level: 7
source: "Monster Core 2"
aon_id: "creature-4596"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4596"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tupilaq"
level: "Creature 7"
size: "Small"
trait_01: "Construct"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15"
abilityMods: [2, 6, 4, -5, 3, -5]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +17; __Ref__: +15; __Will__: +12"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], disease, [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Nonlethal|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Hardness__ 8"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, a tupilaq has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once a tupilaq is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, it loses its Hardness, and its Armor Class is reduced to 22."
speed: "40 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 2d8+5 piercing plus Grab"
abilities_bot:
  - name: "Carver's Curse"
    desc: "When a tupilaq is created, the curse imparted by its creator manifests in the form of a single 3rd-rank primal spell the tupilaq can cast three times per day. The particular spell is a reflection of the creator's wish for vengeance. By default, and for a found or summoned tupilaq, this spell is [[srd/pf2e/compendium/spells/rank-3/fireball|_fireball_]]. Relics Of The Past A tupilaq can last indefinitely once created, and it isn't uncommon for a tupilaq to be unearthed years, decades, or even centuries after its creator has passed away. Archaeologists working at northern dig sites might accidentally stumble across one of these fierce constructs, inadvertently awakening its vengeful curse."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 24 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]] (×3)"
sourcebook: "_Monster Core 2_, page 333."
```

```encounter-table
name: Tupilaq
creatures:
  - 1: Tupilaq
```
