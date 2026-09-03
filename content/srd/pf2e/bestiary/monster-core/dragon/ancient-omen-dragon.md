---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Omen Dragon"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Ancient Omen Dragon"
level: 16
source: "Monster Core"
aon_id: "creature-2955"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2955"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ancient Omen Dragon"
level: "Creature 16"
size: "Huge"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: "Uncommon"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +28, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +29, Fortune-Telling Lore +33, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +31, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +33, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +31"
abilityMods: [8, 6, 7, 9, 7, 5]
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +27; __Ref__: +28; __Will__: +29 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]"
hp: 280
health:
  - name: "HP"
    desc: "280; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Untethered to Fate"
    desc: "The dragon can choose to negate any [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]] effects that would affect them; other creatures remain affected normally."
  - name: "Challenge Fate"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Trigger"
    desc: "The dragon is targeted by an attack"
  - name: "Effect"
    desc: "This fate is not set in stone. The attacker rolls the triggering attack twice and uses the worse result."
speed: "60 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d8+14 piercing plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ claw +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+14 slashing plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ tail +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d8+14 bludgeoning plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ wing +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+14 slashing plus 1d8 mental"
abilities_bot:
  - name: "Destiny Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The dragon breathes a translucent mist of potentialities that overwhelms creatures with visions of possible features, dealing 15d6 mental damage in a 40-foot cone (DC 39 Will save). A creature that fails its save is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round (or slowed 2 on a critical failure) as it struggles with the visions. The dragon can't use Destiny Breath again for 1d4 rounds."
  - name: "Impending Fate"
    desc: "The dragon's attacks bring their foes closer to their eventual fates. When the dragon critically hits with a Strike or a creature critically fails against the dragon's Destiny Breath, the creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed 1]], or increases its doomed value by 1 if it was already doomed."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Destiny Breath whenever they score a critical hit with a Strike."
  - name: "Prophetic Wings"
    desc: "The dragon or any ally can glimpse into the future through the dragon's wings in a process that requires 10 minutes of concentration. This casts a 8th-rank [[srd/pf2e/compendium/spells/rank-2/augury|_augury_]] spell, except that the wings can predict results up to 1 day into the future and the dragon always speaks a few cryptic words related to the result of the prediction. The dragon can use their wings in this way only once per hour, and a given creature can seek a future in the wings only once per week. A creature can also choose to predict events up to 1 month into the future—the dragon can view a month ahead in their own wings only once per day. A creature can also choose to predict events up to 1 year into the future—the dragon can view a year ahead in their own wings only once per day."
  - name: "Walk the Timelines"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The dragon splits themself into two versions with different fates. Each copy Strides or [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] from the dragon's current space, then takes a single action. If the actions are both attacks, they use the same multiple attack penalty and count as one attack toward the dragon's multiple attack penalty. After both actions, the dragon chooses one of the two locations as their actual destination and the other version of themself disappears."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 39 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/guidance|Guidance]] - __7th__ [[srd/pf2e/compendium/spells/rank-1/ill-omen|Ill Omen]] (at will), [[srd/pf2e/compendium/spells/rank-1/mindlink|Mindlink]] (at will), [[srd/pf2e/compendium/spells/rank-7/true-target|True Target]] (×2) - __8th__ [[srd/pf2e/compendium/spells/rank-7/retrocognition|Retrocognition]]"
sourcebook: "_Monster Core_, page 125."
```

```encounter-table
name: Ancient Omen Dragon
creatures:
  - 1: Ancient Omen Dragon
```
