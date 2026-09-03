---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bodach"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Bodach"
level: 6
source: "Monster Core 2"
aon_id: "creature-4285"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4285"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Bodach"
level: "Creature 6"
size: "Medium"
trait_01: "Fey"
trait_02: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +11, Deception +15, Diplomacy +11, Intimidation +13, Nature +13, Stealth +13, Thievery +15"
abilityMods: [2, 2, 4, 4, 3, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 staff_"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +12; __Will__: +17"
hp: 110
health:
  - name: "HP"
    desc: "110; __Weaknesses__ cold iron 5"
abilities_mid:
  - name: "Gray Aura"
    desc: "(aura, emotion, mental) 15 feet. The bodach is always surrounded by a pall of gloomy gray, like the air before it rains. A non-fey or non-hag creature entering the aura or beginning their turn in the aura must succeed at a DC 21 Will save or become slowed 1 for 1 round (slowed 2 on a critical failure). A creature who succeeds is temporarily immune to the aura for 1 minute."
speed: "25 feet, climb 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff_ +16 (Magical, two-hand d8) __Damage__ 2d4+6 bludgeoning"
abilities_bot:
  - name: "Implacable Curse"
    desc: "⬺ The bodach makes a staff Strike. If it hits, it deals an additional 2d8 spirit damage, and the target must attempt a save against either Mumbletongue or Stumblefoot (the bodach's choice)."
  - name: "Mumbletongue"
    desc: "⬺ (Auditory, concentrate, primal) The bodach mumbles a string of half-comprehensible nonsense, cursing creatures within a 10-foot emanation. Each creature in the area must succeed at a DC 24 Will save or become stupefied 1 for 1 minute (stupefied 2 on a critical failure)."
  - name: "Stumblefoot"
    desc: "⬺ (Concentrate, primal, visual) The bodach stares unblinkingly at its foes, cursing creatures within a 15-foot cone. Each creature in the area must succeed at a DC 24 Fortitude save or become clumsy 1 and enfeebled 1 for 1 minute (clumsy 2 and enfeebled 2 on a critical failure)."
  - name: "Unstoppable"
    desc: "A bodach reduces any penalty it takes to its Speed by 5 feet (to a minimum of 0 feet). A bodach can fit into tight spaces as if it were a Small creature. It can move at its full Speed while Squeezing. Gray Men And Red Caps Legend holds that the bodach is the redcap's cousin, and it's certainly true that these two types of fey get along better than most. Malicious redcaps enjoy having their prey softened up, while the bodach appreciates having someone around to do the dirty work of actual killing."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 24 - __2nd__ Mist (at will)"
sourcebook: "_Monster Core 2_, page 61."
```

```encounter-table
name: Bodach
creatures:
  - 1: Bodach
```
