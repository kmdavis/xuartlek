---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animate Dream"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/dream
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Animate Dream"
level: 8
source: "Monster Core 2"
aon_id: "creature-4057"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4057"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Animate Dream"
level: "Creature 8"
size: "Medium"
trait_01: "Dream"
trait_02: "Incorporeal"
trait_03: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Deception +18, Intimidation +18, Occultism +12, Stealth +18"
abilityMods: [-5, 4, 3, 0, 2, 6]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +18; __Will__: +14 +1 status to all saves vs. magic"
hp: 110
health:
  - name: "HP"
    desc: "110; __Immunities__ bleed, disease, paralyzed, poison, precision, sleep; __Resistances__ all 5 (except &amp;lt;%TRAITS%610%%&amp;gt; force &amp;lt;%END>, &amp;lt;%TREASURE%2840%%&amp;gt; _ghost touch_ &amp;lt;%END>, &amp;lt;%TRAITS%737%%&amp;gt; spirit &amp;lt;%END>, or &amp;lt;%TRAITS%510%%&amp;gt; void &amp;lt;%END>) double resistance vs. non-magical)"
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ nightmare tendril +20 (Agile, Finesse) __Damage__ 4d8 void plus endless nightmare"
abilities_bot:
  - name: "Endless Nightmare"
    desc: "(Curse, Emotion, Fear, Mental, Occult) An animate dream's touch fills the victim's mind with terrifying visions"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Stage 1"
    desc: "fatigued (1 day)"
  - name: "Stage 2"
    desc: "fatigued and stupefied 1 (1 day)"
  - name: "Stage 3"
    desc: "The victim falls asleep and can't be awakened as long as they remain at this stage (1 day). Enslaved Dreams Cuckoo hags have been known to enslave animate dreams, forcing them to feed upon themselves. These captives break down into a fearful essence used for the hag's rituals."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26 - __3rd__ Fear - __4th__ Confusion, Nightmare, Sleep, Translocate (at will), Vision of Death"
sourcebook: "_Monster Core 2_, page 31."
```

```encounter-table
name: Animate Dream
creatures:
  - 1: Animate Dream
```
