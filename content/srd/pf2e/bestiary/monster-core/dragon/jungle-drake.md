---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jungle Drake"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Jungle Drake"
level: 6
source: "Monster Core"
aon_id: "creature-2960"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2960"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Jungle Drake"
level: "Creature 6"
size: "Large"
trait_01: "Dragon"
trait_02: "Wood"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [5, 3, 4, -1, 1, 1]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +13; __Will__: +11"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Twisting Tail"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the jungle drake's stinger uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action or leaves a square during a move action they're using"
  - name: "Effect"
    desc: "The jungle drake Strikes the target with their stinger. If it hits, the jungle drake disrupts the creature's action."
speed: "20 feet, fly 50 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +17 __Damage__ 2d10+7 piercing plus Predatory Grab"
  - name: "Melee"
    desc: "⬻ stinger +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+7 piercing plus jungle drake venom"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The jungle drake makes one fangs Strike and two stinger Strikes in any order."
  - name: "Forest Passage"
    desc: "The jungle drake ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth. Even plants manipulated by magic don't impede their progress."
  - name: "Jungle Drake Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 24 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison and enfeebled 2 (1 round)"
  - name: "Predatory Grab"
    desc: "⬻ As Grab, but the jungle drake's Grab doesn't end if they move away. Instead, they carry the [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] creature with them. A jungle drake can't [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] while grabbing a creature unless that creature can also Fly."
  - name: "Speed Surge"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]])"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The jungle drake Strides or Flies twice."
  - name: "Spit Venom"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) A jungle drake can spit a sticky glob of their venom to a range of 50 feet that explodes in a 10-foot burst. Those in the burst must succeed at a DC 24 Reflex save or be exposed to jungle drake venom. The jungle drake can't use Spit Venom again for 1d6 rounds."
sourcebook: "_Monster Core_, page 130."
```

```encounter-table
name: Jungle Drake
creatures:
  - 1: Jungle Drake
```
