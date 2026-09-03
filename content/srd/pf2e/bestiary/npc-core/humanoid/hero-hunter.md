---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hero Hunter"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Hero Hunter"
level: 13
source: "NPC Core"
aon_id: "creature-3621"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3621"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Hero Hunter"
level: "Creature 13"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +26, Crafting +24, Deception +19, Nature +21, Stealth +27, Survival +25"
abilityMods: [5, 4, 3, 3, 2, 0]
abilities_top:
  - name: "Prepared Trapper"
    desc: "A hero hunter carries the materials to Craft two alarm snares, two grasping snares, one snagging hook snare, and one stunning snare. The hero hunter replenishes any used supplies each time they make their daily preparations. Snare rules can be found here."
  - name: "Items"
    desc: "_+1 striking greataxe_, _+1 striking hand crossbow_ (20 bolts), _+1 resilient studded leather_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +25; __Will__: +21"
hp: 230
health:
  - name: "HP"
    desc: "230"
abilities_mid:
  - name: "Nimble Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The hero hunter is targeted with a melee or ranged attack by an attacker they can see"
  - name: "Effect"
    desc: "The hero hunter gains a +2 circumstance bonus to AC against the triggering attack."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, climb 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greataxe_ +27 (Magical, Sweep) __Damage__ 2d12+13 slashing plus hunter's precision"
  - name: "Melee"
    desc: "⬻ fist +26 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+13 bludgeoning plus hunter's precision"
  - name: "Ranged"
    desc: "⬻ _hand crossbow_ +26 (Magical, range increment 60 feet, reload 1) __Damage__ 2d6+8 piercing plus hunter's precision"
abilities_bot:
  - name: "Deadly Snares"
    desc: "⬽ (Manipulate) The hero hunter Crafts a snare that would normally take 1 minute or less to Craft. The Stealth DC to locate the snare and DC to disable it with Thievery are equal to the hero hunter's Crafting DC if it's higher than the snare's DC."
  - name: "Felling Shot"
    desc: "⬻ The hero hunter makes a ranged Strike. If it hits and deals damage to a flying target, the target falls up to 120 feet but takes no damage from the fall. The creature can't Fly, Leap, levitate or otherwise leave the ground until the end of the hero hunter's next turn."
  - name: "Hunter's Precision"
    desc: "⬻ (Stance) The hero hunter knows how to hunt and kill any game. While in this stance, all the hero hunter's Strikes deal an additional 2d8 precision damage, and the range increment for their ranged weapon Strikes is 20 feet longer than normal. If the hunter gets a critical hit with a weapon Strike, the target also takes 2d6 persistent bleed damage. Home Advantage A cocky hero hunter may attack the heroes on their own turf, simply trusting in their skills to win the battle. However, their best move is to lure the PCs to a battlefield they are familiar with, where they've had time to set up their traps. A hero hunter can choose an advantageous place to set their ambush and place snares. They rarely call in allies to assist them unless it's to keep their prey from escaping."
sourcebook: "_NPC Core_, page 162."
```

```encounter-table
name: Hero Hunter
creatures:
  - 1: Hero Hunter
```
