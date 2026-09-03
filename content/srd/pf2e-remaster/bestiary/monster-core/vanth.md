---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vanth"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Vanth"
level: 7
source: "Monster Core"
aon_id: "creature-3148"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3148"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vanth"
level: "Creature 7"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, lifesense 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +17, Boneyard Lore +15, Intimidation +15, Occultism +13, Religion +13, Stealth +17"
abilityMods: [6, 4, 2, 2, 4, 2]
abilities_top:
  - name: "Items"
    desc: "_+1 scythe_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +15; __Ref__: +13; __Will__: +17 +1 status to all saves vs. magic"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ death effects, disease; __Resistances__ poison 10, void 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 20 feet, DC 22"
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scythe_ +18 (deadly d10, Magical, Trip) __Damage__ 1d10+8 slashing plus 2d6 shepherd's touch"
  - name: "Melee"
    desc: "⬻ jaws +17 (Agile) __Damage__ 1d6+8 slashing plus 2d6 shepherd's touch"
abilities_bot:
  - name: "Infuse Weapon"
    desc: "(Divine) A vanth's scythe is its symbol of office and gains a measure of its personal power. This scythe becomes a _+1 scythe_ and is treated as if it were adamantine while the vanth wields it. A vanth whose scythe is taken or destroyed can infuse a new one with an hour of work."
  - name: "Shepherd's Touch"
    desc: "A vanth's Strikes have the benefit of a _ghost touch_ property rune and deal an additional 2d6 void damage to living creatures or 2d6 vitality damage to undead."
  - name: "Vanth's Curse"
    desc: "⬺ (Curse, Divine, Misfortune)"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The vanth bestows a curse on a creature by touching it with its scythe. The creature must attempt a DC 25 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected and is temporarily immune to Vanth's Curse for 24 hours."
  - name: "Success"
    desc: "The target feels a momentary shudder of doom and is stupefied 1 for 1 minute by the distracting sensation."
  - name: "Failure"
    desc: "The target becomes morose and glum as it accepts its own inevitable fate. For 1 hour, the target is stupefied 2. Each time the target gains the dying condition, the stupefied condition value increases by 1, to a maximum value of stupefied 4."
  - name: "Critical Failure"
    desc: "As failure, but the effect is permanent. Vanth Scythes Vanths' favored weapon is the scythe, a choice that further adds to their fearsome appearance and can lead to unfortunate associations with the Grim Reaper or Urgathoa among more superstitious mortals. Vanths find such comparisons to be ignorant at best or insulting at worst. Some vanths infuse their scythes with different qualities, such as cold iron or silver, depending on the nature of their most common enemies."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22 - __2nd__ Invisibility (at will; self only) - __3rd__ Holy Light (×3), Locate (×3) - __4th__ Translocate (at will) - __5th__ Translocate"
sourcebook: "_Monster Core_, page 275."
```

```encounter-table
name: Vanth
creatures:
  - 1: Vanth
```
