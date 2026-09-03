---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Cinder Dragon"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Cinder Dragon"
level: 19
source: "Monster Core 2"
aon_id: "creature-4347"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4347"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ancient Cinder Dragon"
level: "Creature 19"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
trait_04: "Uncommon"
modifier: 35
perception:
  - name: "Perception"
    desc: "Perception +35; darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "Common, Draconic, Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Athletics +38, Diplomacy +35, Intimidation +37, Nature +36, Stealth +37"
abilityMods: [10, 4, 8, 5, 6, 7]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder dragon's vision; they ignore the concealed condition from smoke."
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +34; __Ref__: +30; __Will__: +32 +2 status to all saves vs. primal"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ fire, paralyzed, sleep; __Weaknesses__ cold 20"
abilities_mid:
  - name: "Dragon Heat"
    desc: "(aura, fire, primal) 5 feet, 4d6 fire damage (DC 37 basic Reflex save)"
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 90 feet, DC 37"
  - name: "Boiling Blood"
    desc: "⬲ (fire)"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon's superheated blood spills onto the attacker. The target takes 10d6 fire damage (DC 41 basic Reflex save)."
  - name: "Reactive Strike"
    desc: "⬲ Jaws only"
speed: "60 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +36 (Fire, magical, reach 20 feet) __Damage__ 4d12+12 piercing plus 1d8 persistent fire"
  - name: "Melee"
    desc: "⬻ horn +34 (Magical, reach 20 feet) __Damage__ 3d12+16 piercing"
  - name: "Melee"
    desc: "⬻ claw +36 (Agile, magical, reach 15 feet) __Damage__ 4d10+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +34 (Magical, reach 25 feet) __Damage__ 4d8+12 bludgeoning"
  - name: "Melee"
    desc: "⬻ wing +34 (Agile, magical, reach 20 feet) __Damage__ 4d8+12 slashing"
abilities_bot:
  - name: "All Becomes Flame"
    desc: "⬻ (Curse, fire, primal) The dragon curses a creature within 60 feet to have its magic replaced with primordial flames. The creature must attempt a DC 39 Will save. Regardless of the result, the target becomes temporarily immune for 1 day."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is cursed for 1 round. While cursed, any damage the cursed creature would deal by any means becomes fire damage, regardless of the original damage type. The cursed creature can temporarily suppress the curse for 1 round as an action."
  - name: "Failure"
    desc: "As success, but the curse's duration is 1 hour."
  - name: "Critical Failure"
    desc: "As success, but the curse's duration is 1 day."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Pyre Breath whenever they score a critical hit with a Strike."
  - name: "Pyre Breath"
    desc: "⬺ (Fire, primal) The dragon breathes a blast of flame that deals 18d6 fire damage in a 60-foot cone (DC 41 basic Reflex save). Creatures that critically fail their save catch fire, taking 2d6 persistent fire damage. The area then fills with black smoke for 1 minute. This has the effects of mist, except it fills the cone's area. The dragon can't use Pyre Breath again for 1d4 rounds."
  - name: "Stoke the Flames"
    desc: "⬻ (Fire, primal) The dragon intensifies nearby fires. Every foe within 60 feet that is taking persistent fire damage takes 5d6 fire damage."
sourcebook: "_Monster Core 2_, page 119."
```

```encounter-table
name: Ancient Cinder Dragon
creatures:
  - 1: Ancient Cinder Dragon
```
