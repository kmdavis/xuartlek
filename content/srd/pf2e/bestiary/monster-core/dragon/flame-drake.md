---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Flame Drake"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/large
statblock: inline
name: "Flame Drake"
level: 5
source: "Monster Core"
aon_id: "creature-2959"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2959"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Flame Drake"
level: "Creature 5"
size: "Large"
trait_01: "Dragon"
trait_02: "Fire"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, scent (imprecise) 30 feet, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [5, 1, 3, -1, 3, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a flame drake's vision; they ignore [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]] from smoke."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +12; __Ref__: +10; __Will__: +10"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲ Fangs only."
speed: "20 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +14 __Damage__ 2d8+5 piercing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ tail +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+5 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The flame drake makes two fangs Strikes and one tail Strike in any order."
  - name: "Fireball Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The flame drake expels a ball of flame to a range of 180 feet that explodes in a 20-foot burst. Creatures in the burst take 6d6 fire damage (DC 22 basic Reflex save). The flame drake can't use Fireball Breath again for 1d6 rounds."
  - name: "Speed Surge"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]])"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The flame drake Strides or Flies twice."
sourcebook: "_Monster Core_, page 129."
```

```encounter-table
name: Flame Drake
creatures:
  - 1: Flame Drake
```
