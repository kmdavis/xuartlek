---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Despair Dragon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/large
statblock: inline
name: "Young Despair Dragon"
level: 9
source: "Monster Core 2"
aon_id: "creature-4351"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4351"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Despair Dragon"
level: "Creature 9"
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, fearsense (imprecise) 60 feet, scent (imprecise) 30 feet"
languages: "Common, Draconic; telepathy 60 feet_truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Athletics +19, Deception +18, Diplomacy +18, Intimidation +20, Occultism +16, Society +16, Stealth +18"
abilityMods: [6, 3, 2, 3, 4, 5]
abilities_top:
  - name: "Fearsense"
    desc: "(emotion, mental, occult) The dragon senses all creatures with the frightened condition at the listed range."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +18; __Will__: +20 +2 status to all saves vs. occult"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ fear, paralyzed, sleep"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 60 feet, DC 28"
  - name: "Consume Fear"
    desc: "⬲ (occult)"
  - name: "Trigger"
    desc: "A creature within 60 feet loses the frightened condition"
  - name: "Effect"
    desc: "The dragon feasts upon the fear that leaves the triggering creature's body, gaining 4d8 temporary Hit Points that last for 1 minute."
  - name: "Unbidden Thoughts"
    desc: "⬲ (emotion, fear, mental, occult)"
  - name: "Trigger"
    desc: "The dragon is critically hit with a weapon or unarmed attack"
  - name: "Effect"
    desc: "The attacker's mind fills with visions of their worst fears that overwhelm their senses, and they must choose one of the following results: either the triggering attack becomes a normal success, or the critical hit is unaffected but the triggering creature becomes frightened 2."
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +19 (Magical, reach 10 feet) __Damage__ 2d10+12 piercing"
  - name: "Melee"
    desc: "⬻ claws +19 (Agile, magical, reach 5 feet) __Damage__ 2d8+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +17 (Magical, reach 15 feet) __Damage__ 2d6+10 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Shrieking Breath whenever they score a critical hit with a Strike."
  - name: "Shrieking Breath"
    desc: "⬺ (Mental, occult, sonic) The dragon lets out a cacophonous sound made of every scream the dragon has drawn from a terrified enemy, dealing 8d6 sonic damage in a 30-foot cone (DC 28 basic Will save). Creatures who fail their Will save must spend the first action of their next turn doing nothing but screaming. The dragon can't use Shrieking Breath again for 1d4 rounds."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 28 - __4th__ Fear (at will) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 122."
```

```encounter-table
name: Young Despair Dragon
creatures:
  - 1: Young Despair Dragon
```
