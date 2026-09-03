---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Omen Dragon"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/large
statblock: inline
name: "Young Omen Dragon"
level: 7
source: "Monster Core"
aon_id: "creature-2953"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2953"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Omen Dragon"
level: "Creature 7"
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +16, Diplomacy +13, Fortune-Telling Lore +19, Lore +17, Occultism +17, Society +17"
abilityMods: [5, 3, 4, 6, 4, 2]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +14; __Will__: +17 +2 status to all saves vs. occult"
hp: 100
health:
  - name: "HP"
    desc: "100; __Immunities__ confused, doomed, paralyzed, sleep"
abilities_mid:
  - name: "Untethered to Fate"
    desc: "The dragon can choose to negate any fortune or misfortune effects that would affect them; other creatures remain affected normally."
  - name: "Challenge Fate"
    desc: "⬲ (misfortune, occult)"
  - name: "Trigger"
    desc: "The dragon is targeted by an attack"
  - name: "Effect"
    desc: "This fate is not set in stone. The attacker rolls the triggering attack twice and uses the worse result."
speed: "40 feet, fly 100 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 (Magical, reach 10 feet) __Damage__ 2d8+5 piercing plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ claw +16 (Agile, Magical) __Damage__ 2d6+5 slashing plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ tail +14 (Magical, reach 15 feet) __Damage__ 2d8+5 bludgeoning plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ wing +14 (Agile, Magical, reach 10 feet) __Damage__ 1d8+5 slashing plus 1d8 mental"
abilities_bot:
  - name: "Destiny Breath"
    desc: "⬺ (Mental, Occult) The dragon breathes a translucent mist of potentialities that overwhelms creatures with visions of possible features, dealing 6d6 mental damage in a 20-foot cone (DC 25 Will save). A creature that fails its save is slowed 1 for 1 round (or slowed 2 on a critical failure) as it struggles with the visions. The dragon can't use Destiny Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Destiny Breath whenever they score a critical hit with a Strike."
  - name: "Prophetic Wings"
    desc: "The dragon or any ally can glimpse into the future through the dragon's wings in a process that requires 10 minutes of concentration. This casts a 4th-rank _augury_ spell, except that the wings can predict results up to 1 day into the future and the dragon always speaks a few cryptic words related to the result of the prediction. The dragon can use their wings in this way only once per hour, and a given creature can seek a future in the wings only once per week."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ Guidance - __3rd__ Ill Omen, Mindlink, Sure Strike (×2)"
sourcebook: "_Monster Core_, page 124."
```

```encounter-table
name: Young Omen Dragon
creatures:
  - 1: Young Omen Dragon
```
