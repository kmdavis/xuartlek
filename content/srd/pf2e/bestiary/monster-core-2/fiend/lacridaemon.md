---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lacridaemon"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Lacridaemon"
level: 3
source: "Monster Core 2"
aon_id: "creature-4304"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4304"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Lacridaemon"
level: "Creature 3"
size: "Medium"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [1, 4, 2, 0, 1, 2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +12; __Will__: +6 +1 status to all saves vs. magic"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
abilities_mid:
  - name: "Weeping Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 60 feet. The sounds of crying constantly surround a lacridaemon. A creature that first enters the area must attempt a DC 17 Will save as the sounds cause major disorientation. On a failure, the creature takes a –2 status penalty to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Direction|Sense Direction]] (–4 on a critical failure) for 1 day. After attempting the save, the creature is temporarily immune to the lacridaemon's weeping aura for 1 day. The penalties from multiple weeping auras can increase up to a cumulative total of –10. __Steal Bearings ⬲ Trigger A creature within 30 feet Strides__ Effect The lacridaemon attempts to redirect the triggering creature so it eventually becomes as lost as the lacridaemon. The triggering creature attempts a DC 17 Will save. Regardless of the result, the creature becomes temporarily immune to all attempts to Steal Bearings for 1 minute."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature treats all squares as [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] for its [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Stride]]."
  - name: "Critical Failure"
    desc: "As failure, except that the lacridaemon determines where the target moves during the Stride, though it can't move it into [[srd/pf2e/books/gm-core/chapter-1-running-the-game/running-exploration#Hazardous Terrain|hazardous terrain]] or a place it can't stand."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 1d8+4 piercing plus 1d6 cold and lacridaemon venom"
  - name: "Melee"
    desc: "⬻ claw +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 1d6+4 slashing plus 1d6 cold"
abilities_bot:
  - name: "Lacridaemon Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]])"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 (1 round)"
  - name: "Stage 3"
    desc: "1d8 poison damage, [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]], and stupefied 1 (1 round)"
  - name: "Venomous Spray"
    desc: "⬺ The lacridaemon's begins to weep, spraying its venom-filled tears at all creatures within 30 feet. The creatures are immediately exposed to lacridaemon venom. Other lacridaemons are immune to this venom. Those Who Die Alone The most common souls that spawn lacridaemons are those of wicked individuals abandoned to lonely deaths. Dangerous, reclusive villains who meet their ends at the hands of adventurers in remote lairs tend to become lacridaemons. In addition, those who die exposed to the natural elements, be it from intense heat, freezing temperatures, or thirst, can end up as lacridaemons."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __1st__ [[srd/pf2e/compendium/spells/rank-1/fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/vanishing-tracks|Vanishing Tracks]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]]"
sourcebook: "_Monster Core 2_, page 78."
```

```encounter-table
name: Lacridaemon
creatures:
  - 1: Lacridaemon
```
