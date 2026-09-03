---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Flamboyant Thief"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Flamboyant Thief"
level: 15
source: "NPC Core"
aon_id: "creature-3436"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3436"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Flamboyant Thief"
level: "Creature 15"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +29, Athletics +26, Deception +28, Intimidation +26, Performance +28, Society +24, Stealth +31, Thievery +31, Underworld Lore +28"
abilityMods: [5, 6, 1, 3, 4, 5]
abilities_top:
  - name: "Flamboyant Performance"
    desc: "A flamboyant thief's attempts to Steal don't automatically fail even if a creature is in combat or on guard. While being observed, the thief gains a +2 circumstance bonus to Deception checks to Create a Diversion or Feint and to Thievery checks to Palm an Object or Steal. However, they are compelled to leave a tangible sign of their presence, such as a calling card or symbol—often in place of a stolen item."
  - name: "Vanishing Act"
    desc: "The flamboyant thief can Hide and Sneak even without having cover or being concealed."
  - name: "Items"
    desc: "_+2 striking returning dagger_, elite disguise kit, fine clothes, _+1 resilient leather armor_, _potion of flying_, greater smoke ball, infiltrator thieves' toolkit"
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +23; __Ref__: +30; __Will__: +26"
hp: 225
health:
  - name: "HP"
    desc: "225"
abilities_mid:
  - name: "Dramatic Entrance"
    desc: "⭓ (emotion, mental, visual)"
  - name: "Trigger"
    desc: "The flamboyant thief rolls initiative"
  - name: "Effect"
    desc: "The flamboyant thief draws all eyes to them. They attempt a Performance check, comparing the result against the Will DC of any number of creatures within 120 feet. Each creature the thief succeeds against is fascinated with the thief until the end of the thief's next turn."
  - name: "I Say When I'm Here"
    desc: "When any detection, revelation, or scrying magic would reveal the flamboyant thief, the thief becomes aware of it and can attempt to counteract the magic with a counteract rank of 8th level and using their Stealth as their counteract modifier. **Nimble Dodge ⬲"
  - name: "Trigger"
    desc: "The thief is targeted with a melee or ranged attack by an attacker it can see**"
  - name: "Effect"
    desc: "The thief gains a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +29 (Agile, Finesse, Magical, versatile S) __Damage__ 2d4+11 piercing plus spectacular attack"
  - name: "Melee"
    desc: "⬻ fist +27 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+11 bludgeoning plus spectacular attack"
  - name: "Ranged"
    desc: "⬻ _dagger_ +29 (Agile, Magical, thrown 10 feet, versatile S) __Damage__ 2d4+11 piercing plus spectacular attack"
abilities_bot:
  - name: "Dancing Dagger"
    desc: "⬺ The flamboyant thief can Step, attempt a melee dagger Strike, and attempt a ranged dagger Strike, taking the actions in any order. Both Strikes count toward the thief's multiple attack penalty, but it doesn't increase until after both attacks."
  - name: "Dramatic Exit"
    desc: "⬽ The flamboyant thief throws down their smoke ball, then Hides, then Sneaks up to three times with a +2 circumstance bonus to their Stealth checks."
  - name: "Spectacular Attack"
    desc: "All the flamboyant thief's Strikes deal an additional 3d6 precision damage or 6d6 if the target is fascinated with the thief. After the thief Strikes a creature, that creature becomes fascinated with the thief until the end of the thief's next turn. Calling Cards Flamboyant thieves love to build personas for themselves and gain an infamous reputation. Their choice of calling card is the primary way they accomplish this. It must be something unique and difficult to replicate to prevent pretenders. Some calling cards may include the feather of a phoenix, a rare flower, an intricate clockwork toy, or a custom playing card."
sourcebook: "_NPC Core_, page 25."
```

```encounter-table
name: Flamboyant Thief
creatures:
  - 1: Flamboyant Thief
```
