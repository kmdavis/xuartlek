---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Exiled Revolutionary"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Exiled Revolutionary"
level: 10
source: "NPC Core"
aon_id: "creature-3519"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3519"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Exiled Revolutionary"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; (20 to Sense Motive)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +18, Athletics +15, Deception +19, Diplomacy +19, Intimidation +17, Lore +22, Society +20, Stealth +20, Thievery +18"
abilityMods: [4, 5, 0, 3, 2, 4]
abilities_top:
  - name: "Former Courtier"
    desc: "An exiled revolutionary remembers well their former realm. In their home realm, be it a manor, castle, or capital city, the exiled revolutionary gains a +4 circumstance bonus to Perception checks and Will saves, and to Deception, Diplomacy, Intimidation, and Stealth checks, and is a 12th-level challenge in the arena of noble politics."
  - name: "Items"
    desc: "_+1 composite longbow_ (20 arrows), Leather Armor, _+1 striking longsword_, signet ring, Thieves' Toolkit, Wyvern Poison (2)"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +20; __Will__: +17"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Follow Me"
    desc: "(aura, visual) 20 feet. This aura is active only while in the exiled revolutionary's home realm, as they share knowledge to avoid guard patrols and get past checkpoints. Any ally in the aura gets a +2 circumstance bonus to Deception and Stealth checks. __It's… You!__ (emotion, mental) When the exiled revolutionary sees or hears someone who was part of their downfall in person, they break cover and attack their betrayer immediately, even if their actions would doom them and their allies. The revolutionary must succeed at a DC 35 Will save or be fascinated by their betrayer and unable to cease targeting them exclusively until the betrayer is defeated. An ally can convince the revolutionary to forgo their vengeance with a DC 30 Diplomacy check to make a Request. This lasts for 1 minute, but talking the revolutionary down after that time requires more thorough engagement."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +21 (Magical, versatile P) __Damage__ 2d8+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +21 (deadly d10, Propulsive, Magical, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 1d8+8 piercing"
abilities_bot:
  - name: "Darting Feint"
    desc: "⬺ The exiled revolutionary Feints, Steps, and Strikes in any order."
  - name: "Sneak Attack"
    desc: "The exiled revolutionary deals an additional 2d6 precision damage to off-guard creatures. Betraying The Betrayed Exiled revolutionaries can make for valuable allies, especially if their goals align with the PCs. However, the exiled revolutionary has been a victim of extreme betrayal and constantly guards against it. PCs should take care when considering going back on their word with an exiled revolutionary. Should anyone act in a way that the exiled revolutionary might perceive as a betrayal, the revolutionary will dedicate their life to avenging the perceived transgression, even becoming a villainous instrument of evil should that become necessary."
sourcebook: "_NPC Core_, page 85."
```

```encounter-table
name: Exiled Revolutionary
creatures:
  - 1: Exiled Revolutionary
```
