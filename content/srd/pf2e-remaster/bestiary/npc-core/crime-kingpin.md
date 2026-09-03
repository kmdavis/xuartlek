---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Crime Kingpin"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Crime Kingpin"
level: 12
source: "NPC Core"
aon_id: "creature-3435"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3435"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Crime Kingpin"
level: "Creature 12"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; (24 to Sense Motive)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +25, Deception +24, Diplomacy +22, Intimidation +28, Society +24, Stealth +23, Thievery +24, Underworld Lore +24"
abilityMods: [3, 5, 3, 2, 2, 6]
abilities_top:
  - name: "Items"
    desc: "_+1 striking hand crossbow_ (10 bolts), _+1 leather armor_, _potion of flying_, _moderate potion of healing_ (2), _+1 striking rapier_"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +23; __Ref__: +23; __Will__: +22"
hp: 250
health:
  - name: "HP"
    desc: "250"
abilities_mid:
  - name: "Kingpin's Presence"
    desc: "(aura, emotion, mental) 30 feet. Allies in the aura gain a +2 status bonus to saving throws against mental effects."
  - name: "Deny Advantage"
    desc: "The kingpin isn't off-guard to creatures of 12th level or lower that are hidden, undetected, flanking, or using surprise attack."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "You'll Pay for That"
    desc: "⬲ (auditory, concentrate, emotion, linguistic, mental)"
  - name: "Trigger"
    desc: "An enemy damages the kingpin"
  - name: "Effect"
    desc: "The kingpin issues a vendetta against the enemy. Each of the kingpin's allies who hears the command gains a +5 status bonus to their next damage roll against that enemy."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +26 (deadly d8, Disarm, Finesse, Magical) __Damage__ 2d6+11 piercing"
  - name: "Melee"
    desc: "⬻ fist +26 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _hand crossbow_ +26 (Magical, range increment 60 feet, reload 1) __Damage__ 2d6+8 piercing"
abilities_bot:
  - name: "Fencing Brawl"
    desc: "⬺ The kingpin attempts a rapier Strike followed by a Disarm or Grapple attempt against the same enemy. These count as one attack for the kingpin's multiple attack penalty, and the penalty doesn't increase until after both attacks."
  - name: "Kick Away"
    desc: "⬲"
  - name: "Trigger"
    desc: "The kingpin knocks an item out of a creature's grasp using Disarm"
  - name: "Effect"
    desc: "The kingpin kicks the weapon up to 20 feet in any direction. If the kingpin kicks the weapon into an ally's square, that ally can catch the weapon as a free action, Releasing anything else they're holding if necessary."
  - name: "Kingpin's Command"
    desc: "⬻ (Auditory, Concentrate, Linguistic, Mental) The crime kingpin shouts a command to an ally of their choice. That ally can spend a reaction to Stride and Strike. The ally becomes immune to Kingpin's Command for 24 hours."
  - name: "Sneak Attack"
    desc: "The crime kingpin deals an additional 3d6 precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 24."
```

```encounter-table
name: Crime Kingpin
creatures:
  - 1: Crime Kingpin
```
