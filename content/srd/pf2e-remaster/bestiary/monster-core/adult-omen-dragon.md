---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Omen Dragon"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Omen Dragon"
level: 11
source: "Monster Core"
aon_id: "creature-2954"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2954"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Omen Dragon"
level: "Creature 11"
size: "Huge"
trait_01: "Dragon"
trait_02: "Occult"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Fey, Jotun"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Athletics +22, Diplomacy +20, Fortune-Telling Lore +26, Lore +24, Occultism +24, Society +22"
abilityMods: [7, 4, 5, 7, 6, 3]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +20; __Ref__: +19; __Will__: +23 +2 status to all saves vs. occult"
hp: 185
health:
  - name: "HP"
    desc: "185; __Immunities__ confused, doomed, paralyzed, sleep"
abilities_mid:
  - name: "Untethered to Fate"
    desc: "The dragon can choose to negate any fortune or misfortune effects that would affect them; other creatures remain affected normally."
  - name: "Challenge Fate"
    desc: "⬲ (misfortune, occult)"
  - name: "Trigger"
    desc: "The dragon is targeted by an attack"
  - name: "Effect"
    desc: "This fate is not set in stone. The attacker rolls the triggering attack twice and uses the worse result."
speed: "50 feet, fly 130 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 (Magical, reach 10 feet) __Damage__ 2d8+11 piercing plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ claw +22 (Agile, Magical) __Damage__ 2d6+11 slashing plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ tail +20 (Magical, reach 15 feet) __Damage__ 2d8+11 bludgeoning plus 1d8 mental"
  - name: "Melee"
    desc: "⬻ wing +20 (Agile, Magical, reach 10 feet) __Damage__ 1d8+11 slashing plus 1d8 mental"
abilities_bot:
  - name: "Destiny Breath"
    desc: "⬺ (Mental, Occult) The dragon breathes a translucent mist of potentialities that overwhelms creatures with visions of possible features, dealing 10d6 mental damage in a 30-foot cone (DC 30 Will save). A creature that fails its save is slowed 1 for 1 round (or slowed 2 on a critical failure) as it struggles with the visions. The dragon can't use Destiny Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Destiny Breath whenever they score a critical hit with a Strike."
  - name: "Prophetic Wings"
    desc: "The dragon or any ally can glimpse into the future through the dragon's wings in a process that requires 10 minutes of concentration. This casts a 6th-rank _augury_ spell, except that the wings can predict results up to 1 day into the future and the dragon always speaks a few cryptic words related to the result of the prediction. The dragon can use their wings in this way only once per hour, and a given creature can seek a future in the wings only once per week. A creature can choose to predict events up to 1 month into the future—the dragon can view a month ahead in their own wings only once per day."
  - name: "Walk the Timelines"
    desc: "⬺ (Occult)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The dragon splits themself into two versions with different fates. Each copy Strides or Flies from the dragon's current space, then takes a single action. If the actions are both attacks, they use the same multiple attack penalty and count as one attack toward the dragon's multiple attack penalty. After both actions, the dragon chooses one of the two locations as their actual destination and the other version of themself disappears."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30 - __Cantrips (4th)__ Guidance - __5th__ Ill Omen (at will), Mindlink (at will), Sure Strike (×2)"
sourcebook: "_Monster Core_, page 124."
```

```encounter-table
name: Adult Omen Dragon
creatures:
  - 1: Adult Omen Dragon
```
