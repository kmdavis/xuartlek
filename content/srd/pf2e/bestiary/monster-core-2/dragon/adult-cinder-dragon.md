---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Cinder Dragon"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Cinder Dragon"
level: 14
source: "Monster Core 2"
aon_id: "creature-4346"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4346"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Cinder Dragon"
level: "Creature 14"
size: "Huge"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "Common, Draconic, Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +29, Diplomacy +25, Intimidation +27, Nature +26, Stealth +23"
abilityMods: [8, 2, 6, 3, 4, 5]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder dragon's vision; they ignore the concealed condition from smoke."
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +27; __Ref__: +23; __Will__: +25 +2 status to all saves vs. primal"
hp: 310
health:
  - name: "HP"
    desc: "310; __Immunities__ fire, paralyzed, sleep; __Weaknesses__ cold 15"
abilities_mid:
  - name: "Dragon Heat"
    desc: "(aura, fire, primal) 5 feet, 3d6 fire damage (DC 30 basic Reflex save)"
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 90 feet, DC 32"
  - name: "Boiling Blood"
    desc: "⬲ (fire)"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon's superheated blood spills onto the attacker. The target takes 8d6 fire damage (DC 34 basic Reflex save)."
  - name: "Reactive Strike"
    desc: "⬲ Jaws only"
speed: "50 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +29 (Fire, magical, reach 15 feet) __Damage__ 3d12+12 piercing plus 1d8 persistent fire"
  - name: "Melee"
    desc: "⬻ horn +27 (Magical, reach 20 feet) __Damage__ 3d12+16 piercing"
  - name: "Melee"
    desc: "⬻ claw +29 (Agile, magical, reach 10 feet) __Damage__ 3d10+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +27 (Magical, reach 20 feet) __Damage__ 3d12+12 bludgeoning"
  - name: "Melee"
    desc: "⬻ wing +27 (Agile, magical, reach 15 feet) __Damage__ 3d8+12 slashing"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Pyre Breath whenever they score a critical hit with a Strike."
  - name: "Pyre Breath"
    desc: "⬺ (Fire, primal) The dragon breathes a blast of flame that deals 13d6 fire damage in a 50-foot cone (DC 34 basic Reflex save). Creatures that critically fail their save catch fire, taking 2d6 persistent fire damage. The area then fills with black smoke for 1 minute. This has the effects of mist, except it fills the cone's area. The dragon can't use Pyre Breath again for 1d4 rounds."
  - name: "Stoke the Flames"
    desc: "⬻ (Fire, primal) The dragon intensifies nearby fires. Every foe within 60 feet that is taking persistent fire damage takes 4d6 fire damage."
sourcebook: "_Monster Core 2_, page 118."
```

```encounter-table
name: Adult Cinder Dragon
creatures:
  - 1: Adult Cinder Dragon
```
