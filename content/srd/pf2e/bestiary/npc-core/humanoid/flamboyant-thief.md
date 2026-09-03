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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +29, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +26, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +28, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +28, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +31, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +31, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +28"
abilityMods: [5, 6, 1, 3, 4, 5]
abilities_top:
  - name: "Flamboyant Performance"
    desc: "A flamboyant thief's attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Steal|Steal]] don't automatically fail even if a creature is in combat or on guard. While being [[srd/pf2e/compendium/rules-elements/conditions#Observed|observed]], the thief gains a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Create a Diversion|Create a Diversion]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|Feint]] and to [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Palm an Object|Palm an Object]] or Steal. However, they are compelled to leave a tangible sign of their presence, such as a calling card or symbol—often in place of a stolen item."
  - name: "Vanishing Act"
    desc: "The flamboyant thief can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] and [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneak]] even without having cover or being [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]]."
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/runes/returning|returning]] [[srd/pf2e/compendium/equipment/weapons/knife/dagger|dagger]]_, elite disguise kit, fine clothes, _+1 [[srd/pf2e/compendium/equipment/runes/resilient-major|resilient]] [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]_, _[[srd/pf2e/compendium/equipment/consumables/potion-of-flying-greater|potion of flying]]_, [[srd/pf2e/compendium/equipment/alchemical-items/smoke-ball-greater|greater smoke ball]], infiltrator thieves' toolkit"
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
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]])"
  - name: "Trigger"
    desc: "The flamboyant thief rolls initiative"
  - name: "Effect"
    desc: "The flamboyant thief draws all eyes to them. They attempt a [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] check, comparing the result against the Will DC of any number of creatures within 120 feet. Each creature the thief succeeds against is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the thief until the end of the thief's next turn."
  - name: "I Say When I'm Here"
    desc: "When any [[srd/pf2e/compendium/rules-elements/traits/player-core/detection|detection]], [[srd/pf2e/compendium/rules-elements/traits/player-core/revelation|revelation]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/scrying|scrying]] magic would reveal the flamboyant thief, the thief becomes aware of it and can attempt to counteract the magic with a counteract rank of 8th level and using their [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] as their counteract modifier. **Nimble Dodge ⬲"
  - name: "Trigger"
    desc: "The thief is targeted with a melee or ranged attack by an attacker it can see**"
  - name: "Effect"
    desc: "The thief gains a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d4+11 piercing plus spectacular attack"
  - name: "Melee"
    desc: "⬻ fist +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+11 bludgeoning plus spectacular attack"
  - name: "Ranged"
    desc: "⬻ _dagger_ +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d4+11 piercing plus spectacular attack"
abilities_bot:
  - name: "Dancing Dagger"
    desc: "⬺ The flamboyant thief can Step, attempt a melee dagger Strike, and attempt a ranged dagger Strike, taking the actions in any order. Both Strikes count toward the thief's multiple attack penalty, but it doesn't increase until after both attacks."
  - name: "Dramatic Exit"
    desc: "⬽ The flamboyant thief throws down their smoke ball, then [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hides]], then Sneaks up to three times with a +2 circumstance bonus to their [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] checks."
  - name: "Spectacular Attack"
    desc: "All the flamboyant thief's Strikes deal an additional 3d6 precision damage or 6d6 if the target is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the thief. After the thief Strikes a creature, that creature becomes fascinated with the thief until the end of the thief's next turn. Calling Cards Flamboyant thieves love to build personas for themselves and gain an infamous reputation. Their choice of calling card is the primary way they accomplish this. It must be something unique and difficult to replicate to prevent pretenders. Some calling cards may include the feather of a [[srd/pf2e/bestiary/monster-core/beast/phoenix|phoenix]], a rare flower, an intricate clockwork toy, or a custom playing card."
sourcebook: "_NPC Core_, page 25."
```

```encounter-table
name: Flamboyant Thief
creatures:
  - 1: Flamboyant Thief
```
