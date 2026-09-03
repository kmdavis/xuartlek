---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skaveling"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Skaveling"
level: 5
source: "Monster Core 2"
aon_id: "creature-4545"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4545"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Skaveling"
level: "Creature 5"
size: "Large"
trait_01: "Undead"
trait_02: "Unholy"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, echolocation 40 feet"
languages: "Aklo, Sakvroth"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +13, Intimidation +11"
abilityMods: [6, 4, 2, 1, 6, 2]
abilities_top:
  - name: "Echolocation"
    desc: "A skaveling can use their hearing as a precise sense at the listed range."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +13; __Will__: +15"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious"
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +15 __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ wing +15 (Agile) __Damage__ 2d4+8 bludgeoning"
abilities_bot:
  - name: "Bone-Chilling Screech"
    desc: "⬺ (Auditory, emotion, fear, mental, occult) The skaveling unleashes a horrifying screech that chills the very bones of those close enough to feel it. The screech can be heard for miles, but each creature in a 20-foot emanation must also attempt a DC 22 Will save. The skaveling can't use Bone-Chilling Screech again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune to Bone-Chilling Screech for 24 hours."
  - name: "Success"
    desc: "The creature is frightened 1."
  - name: "Failure"
    desc: "The creature is frightened 2."
  - name: "Critical Failure"
    desc: "The creature is frightened 2 and stunned 1 by fear."
  - name: "Consume Flesh"
    desc: "⬻ (Manipulate)"
  - name: "Requirements"
    desc: "The skaveling is adjacent to the corpse of a creature that died within the last hour"
  - name: "Effect"
    desc: "The skaveling devours a chunk of the corpse and regains 1d6 Hit Points plus 1d6 for every 2 levels the skaveling has. They can regain Hit Points from any given corpse only once."
  - name: "Feast on Fear"
    desc: "⬲ (occult Trigger The skaveling deals damage to a frightened creature with a fangs Strike) Effect The skaveling draws power from the fear infusing a creature's flesh. The frightened creature must attempt a DC 22 Fortitude saving throw."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes a –5-foot status penalty to its Speed, and the skaveling gains a +5-foot status bonus to their Speeds until the end of their next turn."
  - name: "Failure"
    desc: "The creature takes a –10-foot status penalty to its Speed, and the skaveling gains a +10-foot status bonus to their Speeds until the end of their next turn."
  - name: "Critical Failure"
    desc: "The creature is slowed 1, and the skaveling can immediately Fly, Step, or Stride as a free action; this movement doesn't trigger reactions."
  - name: "Swift Dart"
    desc: "⬻ (Move) The skaveling Flies up to half their Speed. This movement doesn't trigger reactions. Skaveling Intellect As a curious side effect of their creation, skavelings absorb many memories of the ghoul brains on which they were fed. While merely an oversized animal in life, in undeath these memories coalesce into a strange form of intelligence that affords skavelings the ability to speak and reason, all the better to serve their urdefhan masters. Skavelings remain loyal to urdefhans and never take actions in a fight that would harm their creators."
sourcebook: "_Monster Core 2_, page 287."
```

```encounter-table
name: Skaveling
creatures:
  - 1: Skaveling
```
