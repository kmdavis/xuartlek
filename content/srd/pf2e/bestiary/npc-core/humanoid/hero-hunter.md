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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +23, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +26, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +24, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +19, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +21, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +25"
abilityMods: [5, 4, 3, 3, 2, 0]
abilities_top:
  - name: "Prepared Trapper"
    desc: "A hero hunter carries the materials to [[srd/pf2e/compendium/rules-elements/actions/player-core#Craft|Craft]] two [[srd/pf2e/compendium/equipment/snares/alarm-snare|alarm snares]], two [[srd/pf2e/compendium/equipment/snares/grasping-snare|grasping snares]], one [[srd/pf2e/compendium/equipment/snares/snagging-hook-snare|snagging hook snare]], and one [[srd/pf2e/compendium/equipment/snares/stunning-snare|stunning snare]]. The hero hunter replenishes any used supplies each time they make their daily preparations. Snare rules can be found [[srd/pf2e/books/player-core-2/snares/index|here]]."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/axe/greataxe|greataxe]]_, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/crossbow/hand-crossbow|hand crossbow]]_ (20 bolts), _+1 [[srd/pf2e/compendium/equipment/runes/resilient-major|resilient]] [[srd/pf2e/compendium/equipment/armor#Studded Leather Armor|studded leather]]_"
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
    desc: "⬻ _greataxe_ +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 2d12+13 slashing plus hunter's precision"
  - name: "Melee"
    desc: "⬻ fist +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+13 bludgeoning plus hunter's precision"
  - name: "Ranged"
    desc: "⬻ _hand crossbow_ +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 60 feet, reload 1) __Damage__ 2d6+8 piercing plus hunter's precision"
abilities_bot:
  - name: "Deadly Snares"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The hero hunter [[srd/pf2e/compendium/rules-elements/actions/player-core#Craft|Crafts]] a snare that would normally take 1 minute or less to Craft. The [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] DC to locate the snare and DC to disable it with [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] are equal to the hero hunter's [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] DC if it's higher than the snare's DC."
  - name: "Felling Shot"
    desc: "⬻ The hero hunter makes a ranged Strike. If it hits and deals damage to a flying target, the target falls up to 120 feet but takes no damage from the fall. The creature can't [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]], Leap, levitate or otherwise leave the ground until the end of the hero hunter's next turn."
  - name: "Hunter's Precision"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/stance|Stance]]) The hero hunter knows how to hunt and kill any game. While in this stance, all the hero hunter's Strikes deal an additional 2d8 precision damage, and the range increment for their ranged weapon Strikes is 20 feet longer than normal. If the hunter gets a critical hit with a weapon Strike, the target also takes 2d6 persistent bleed damage. Home Advantage A cocky hero hunter may attack the heroes on their own turf, simply trusting in their skills to win the battle. However, their best move is to lure the PCs to a battlefield they are familiar with, where they've had time to set up their traps. A hero hunter can choose an advantageous place to set their ambush and place snares. They rarely call in allies to assist them unless it's to keep their prey from escaping."
sourcebook: "_NPC Core_, page 162."
```

```encounter-table
name: Hero Hunter
creatures:
  - 1: Hero Hunter
```
