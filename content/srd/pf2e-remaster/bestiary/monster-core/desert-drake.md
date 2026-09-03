---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Desert Drake"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/large
statblock: inline
name: "Desert Drake"
level: 8
source: "Monster Core"
aon_id: "creature-2963"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2963"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Desert Drake"
level: "Creature 8"
size: "Large"
trait_01: "Dragon"
trait_02: "Earth"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, sandstorm sight, scent (imprecise) 30 feet"
languages: "Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +18, Intimidation +13, Stealth +15, Survival +15"
abilityMods: [6, 3, 5, -1, 3, 1]
abilities_top:
  - name: "Sandstorm Sight"
    desc: "Sandstorms don't impair a desert drake's vision; they ignore concealmentfrom sandstorms. They also are immune to being dazzled or blinded by sand or other grit."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +15; __Will__: +13"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ paralyzed, sleep; __Resistances__ cold 10, fire 10 **Wing Deflection ⬲"
abilities_mid:
  - name: "Trigger"
    desc: "The desert drake is targeted with an attack**"
  - name: "Effect"
    desc: "The desert drake raises their wing, gaining a +2 circumstance bonus to AC against the triggering attack. If the desert drake is flying at the time they're attacked, they descend 10 feet after the attack is complete."
speed: "20 feet; burrow 20 feet (sand only), fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +19 __Damage__ 2d12+10 piercing"
  - name: "Melee"
    desc: "⬻ tail +19 (reach 10 feet) __Damage__ 2d8+10 bludgeoning plus Push 5 feet"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The desert drake makes two fangs Strikes and one tail Strike in any order."
  - name: "Sandstorm Breath"
    desc: "⬺ (Earth, Primal) The desert drake spits a ball of abrasive sand with a range of 60 feet that explodes into a cloud with a 15-foot-radius burst. Creatures in the area take 9d6 slashing damage (DC 27 basic Reflex save). The desert drake can't use Sandstorm Breath again for 1d6 rounds, during which the sandstorm lingers in the area. This lingering sandstorm grants concealmentto everything within it and conceals everything outside from them."
  - name: "Speed Surge"
    desc: "⬻ (Move)"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The desert drake Strides or Flies twice."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted yet are off-guard to the desert drake."
sourcebook: "_Monster Core_, page 133."
```

```encounter-table
name: Desert Drake
creatures:
  - 1: Desert Drake
```
