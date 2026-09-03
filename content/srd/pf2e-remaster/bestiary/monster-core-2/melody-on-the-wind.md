---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Melody On The Wind"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Melody On The Wind"
level: 10
source: "Monster Core 2"
aon_id: "creature-4381"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4381"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Melody On The Wind"
level: "Creature 10"
size: "Huge"
trait_01: "Air"
trait_02: "Elemental"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +22, Athletics +19, Performance +22, Stealth +22"
abilityMods: [4, 6, 2, 2, 5, 6]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +16; __Ref__: +22; __Will__: +19"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Hostile Duet"
    desc: "⬲"
  - name: "Trigger"
    desc: "A hostile creature within 30 feet creates an effect with the auditory trait that provides bonuses to itself or its allies"
  - name: "Effect"
    desc: "The melody on the wind recreates the effect, gaining the bonuses for itself and its allies as long as the original effect persists."
  - name: "Retune"
    desc: "⬲"
  - name: "Trigger"
    desc: "The melody on the wind is targeted by a spell that has the auditory trait"
  - name: "Effect"
    desc: "The melody on the wind attempts to counteract the spell with a Performance check. If it succeeds, the spell effect is caught in a blast of wind that sweeps it back to its origin, affecting the caster. Targets of the triggering effect other than the melody on the wind are still affected normally."
speed: "fly 100 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ wind gust +23 (Agile, finesse) __Damage__ 2d10+10 bludgeoning plus Push"
  - name: "Ranged"
    desc: "⬻ solid refrain +23 (range increment 70 feet) __Damage__ 2d8+10 sonic"
abilities_bot:
  - name: "Mesmerizing Melody"
    desc: "⬻ (Auditory, concentrate, mental, primal) The melody on the wind sings in a sonorous chorus. Any creature in a 30-foot emanation must attempt a DC 29 Will save to resist becoming fascinated by the melody on the wind. A creature that succeeds at its save is temporarily immune for 24 hours."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is fascinated by the melody on the wind for 1 round."
  - name: "Failure"
    desc: "The creature is fascinated by the melody on the wind for 4 rounds."
  - name: "Swiftness"
    desc: "The melody on the wind's movement doesn't trigger reactions."
sourcebook: "_Monster Core 2_, page 145."
```

```encounter-table
name: Melody On The Wind
creatures:
  - 1: Melody On The Wind
```
