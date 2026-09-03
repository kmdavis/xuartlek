---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aghash"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/div
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Aghash"
level: 4
source: "Monster Core 2"
aon_id: "creature-4340"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4340"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Aghash"
level: "Creature 4"
size: "Medium"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; greater darkvision"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +9, Athletics +8, Deception +12, Intimidation +12, Religion +10, Stealth +10"
abilityMods: [3, 4, 3, 1, 2, 4]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +9; __Ref__: +10; __Will__: +12 +1 status to all saves vs. magic"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ curse; __Weaknesses__ cold iron 5, holy 5"
abilities_mid:
  - name: "Hatred of Art"
    desc: "While aghashes hate all mortals, they particularly despise beautiful objects and artistic mortals. When not in physical peril, an aghash is compelled to destroy art and other works of beauty. An aghash can't enter an area of pristine beauty without first marring it in some way. Given a choice, an aghash will attack a foe who is an obvious crafter or performer of some kind. A bard casting a composition spell, a runesmith tracing a rune, a street magician performing a daring escape, and similar abilities as determined by the GM draw the aghash's ire. If the aghash is barred from attacking such foes, either by force or some magical effect, they take 1d6 mental damage at the end of their turn."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +14 (Agile, finesse, magical, unholy) __Damage__ 2d6+5 slashing"
abilities_bot:
  - name: "Cursed Gaze"
    desc: "⬺ (Concentrate, curse, divine, emotion, fear, mental, visual) The aghash fixes their gaze on one creature they can see within 20 feet. The creature must attempt a DC 21 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes 2d6 mental damage and becomes frightened 1."
  - name: "Failure"
    desc: "The creature takes 4d6 mental damage and becomes either frightened 2 or stunned 1 (the aghash's choice)."
  - name: "Critical Failure"
    desc: "The creature takes 8d6 mental damage and becomes frightened 2 and stunned 2."
  - name: "Sandstorm"
    desc: "⬽ (Divine, earth)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The aghash creates a temporary sandstorm in a 30-foot emanation that lasts for 1 minute. Creatures within the emanation take a –4 circumstance penalty to Perception checks and must succeed at a DC 18 Fortitude save. On a failure, they're forced to hold their breath or else they start suffocating. A creature within the sandstorm at the end of its turn takes 1d6 slashing damage. Divs are immune to all effects of an aghash's Sandstorm."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ Detect Magic - __1st__ Illusory Object (at will) - __2nd__ Stupefy (at will) - __4th__ Outcast's Curse, Translocate"
  - name: "Rituals"
    desc: "DC 21 - __1st__ Div Pact"
sourcebook: "_Monster Core 2_, page 111."
```

```encounter-table
name: Aghash
creatures:
  - 1: Aghash
```
