---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skulltaker"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Skulltaker"
level: 18
source: "Monster Core"
aon_id: "creature-3198"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3198"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Skulltaker"
level: "Creature 18"
size: "Huge"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 33
perception:
  - name: "Perception"
    desc: "Perception +33; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]; Skeletal Lore languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +34, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +35, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +30, Skeletal Lore +30, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +32"
abilityMods: [8, 6, 6, 2, 8, 7]
abilities_top:
  - name: "Skeletal Lore"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A skulltaker taps into the memories of the creatures whose bones make up its body. This gives it the Skeletal Lore skill, which it can use to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] of any kind. In addition, it can speak and understand all the languages known by the creatures whose bones make up its body (typically including [[srd/pf2e/compendium/rules-elements/languages#Common|Common]] and the regional language of the skulltaker's home region). The skulltaker can use Skeletal Lore as the primary skill check for the [[srd/pf2e/compendium/spells/rituals/collective-memories|_collective memories_]] ritual, and it can cast _collective memories_ without secondary casters."
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +31; __Ref__: +33; __Will__: +35 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]"
hp: 300
health:
  - name: "HP"
    desc: "300 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ piercing 15, slashing 15"
abilities_mid:
  - name: "Shard Storm"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 10 feet. A cloud of bone shards surrounds the skulltaker. When a creature moves into the emanation or begins its turn there, shard storm deals 4d6 slashing damage and 4d6 void damage to the creature, with a DC 40 basic Reflex save. If the creature has resistance or immunity to void damage, or an effect that protects it against [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, or an effect that protects it against the [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] or [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] condition, the creature must first succeed at a DC 40 Will save or have all such benefits suppressed for 1 minute."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d10+14 piercing plus 3d6 void and vitality drain"
  - name: "Melee"
    desc: "⬻ claw +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d6+14 slashing plus 3d6 void and vitality drain"
  - name: "Ranged"
    desc: "⬻ bone javelin +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 100 feet]]) __Damage__ 3d8+6 piercing plus 3d6 void"
abilities_bot:
  - name: "Bonetaker"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) Whenever a creature dies within 60 feet of a skulltaker, the skulltaker draws a portion of the creature's bones into its shard storm. The creature must succeed at a DC 40 Will save or rise as a [[srd/pf2e/bestiary/monster-core/undead/skeletal-champion|skeletal champion]] in 1d4 rounds. These skeletal champions are controlled by the skulltaker."
  - name: "Splintered Ground"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The skulltaker causes splintered bones to erupt from all solid surfaces in a 100-foot emanation, except for surfaces of worked stone. A creature moving through the bones takes 10 piercing damage and 10 void damage for every 5 feet of movement. The first time each round a creature takes piercing damage from these splintered bones, it must succeed at a DC 40 Reflex save or take a –10-foot circumstance penalty to all Speeds for 10 minutes, or a –15-foot circumstance penalty for 24 hours on a critical failure. The bones remain in place until the skulltaker uses this action again or the bones are manually removed, which takes 10 minutes for each 5-foot square."
  - name: "Vitality Drain"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) When a skulltaker hits with a melee Strike, the target must succeed at a DC 40 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 2]] and [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed 1]]. Skulltaker Insight The cooperation of a skulltaker is a powerful asset, for this whirling mass of death retains the collective memories of the creatures whose bones form its body. Because mountain travelers come from far and wide, a skulltaker's knowledge is often vast, spanning a range of topics."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40 - __8th__ [[srd/pf2e/compendium/spells/rank-8/desiccate|Desiccate]] (×2), [[srd/pf2e/compendium/spells/rank-7/execute|Execute]] (×2), [[srd/pf2e/compendium/spells/rank-8/punishing-winds|Punishing Winds]] (×2) - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 40 - __7th__ [[srd/pf2e/compendium/spells/rituals/collective-memories|Collective Memories]] (see Skeletal Lore)"
sourcebook: "_Monster Core_, page 314."
```

```encounter-table
name: Skulltaker
creatures:
  - 1: Skulltaker
```
