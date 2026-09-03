---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Warsworn"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Warsworn"
level: 16
source: "Monster Core"
aon_id: "creature-3232"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3232"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Warsworn"
level: "Creature 16"
size: "Gargantuan"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision"
languages: "Common; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +33"
abilityMods: [9, 5, 7, -1, 5, 5]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +29; __Ref__: +25; __Will__: +27 +1 status to all saves vs. vitality"
hp: 350
health:
  - name: "HP"
    desc: "350 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Animated Weapons"
    desc: "(aura, divine) 100 feet. The warsworn automatically controls unattended weapons in the aura, which levitate around the warsworn. The warsworn can telekinetically wield these weapons to make melee Strikes with a reach of 100 feet. These strikes deal four of the weapon's damage dice +9 and use the weapon's damage type."
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 100 feet, DC 35"
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ corpse wave +32 (Magical) __Damage__ 4d12+9 bludgeoning plus energy drain"
  - name: "Melee"
    desc: "⬻ animated weapon +30 (Agile, Magical, reach 100 feet) __Damage__ see animated weapons"
  - name: "Ranged"
    desc: "⬻ scrap ball +28 (Magical, range increment 100 feet) __Damage__ 4d12+9 bludgeoning plus plummet"
abilities_bot:
  - name: "Absorb"
    desc: "⭓ (Death, Divine, Void)"
  - name: "Trigger"
    desc: "The warsworn moves into a dying creature's space"
  - name: "Effect"
    desc: "The warsworn absorbs the dying creature into itself, instantly killing the creature and healing the warsworn for a number of Hit Points equal to the creature's level. As long as the warsworn still exists, absorbed creatures can't be resurrected except by _wish_ or a similarly powerful effect."
  - name: "Energy Drain"
    desc: "(Divine, Void) When a warsworn hits with a corpse wave Strike or damages a creature with Trample, the target must succeed at a DC 35 Fortitude save or become drained 2 and doomed 1. On a critical success, the target becomes temporarily immune to the warsworn's energy drain for 24 hours."
  - name: "Plummet"
    desc: "A creature hit by a warsworn's scrap ball Strike must attempt a DC 37 Reflex save. On a failure, the target falls prone; if the target was airborne, it falls up to 120 feet, taking damage from the fall and landing prone if the descent brings it to the ground. On a critical failure, the target is also held under a pile of scrap (Escape DC 37)."
  - name: "Trample"
    desc: "⬽ Huge or smaller, corpse wave, DC 37 Alternate Warsworns While uniquely terrible, war is not the only tragedy that can lead to mass deaths. Other forms of mass undead, similar to warsworn, can sometimes arise from causes such as famine or disaster. Flamesworn rise from large crowds killed by fire, while plagueborn rise when entire townships or even cities perish to disease."
sourcebook: "_Monster Core_, page 342."
```

```encounter-table
name: Warsworn
creatures:
  - 1: Warsworn
```
