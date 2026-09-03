---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Juggler"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Juggler"
level: 2
source: "NPC Core"
aon_id: "creature-3572"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3572"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Juggler"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +8, Circus Lore +8, Performance +11"
abilityMods: [2, 3, 1, 0, 1, 3]
abilities_top:
  - name: "Juggling Specialist"
    desc: "For encounters involving juggling and other circus acts, the juggler is a 5th-level challenge."
  - name: "Items"
    desc: "juggling club (3, functions as a light hammer), Dart (10), Torch (3)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +11; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30"
abilities_mid:
  - name: "Return Throw"
    desc: "⬲"
  - name: "Trigger"
    desc: "A physical ranged attack with a throwing weapon critically fails to hit the juggler"
  - name: "Effect"
    desc: "The juggler snatches the weapon from the air and immediately makes a ranged Strike against the attacker using that weapon."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ juggling club +9 (Agile) __Damage__ 1d6+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dart +10 (Agile, thrown 20 feet) __Damage__ 1d4+4 piercing"
  - name: "Ranged"
    desc: "⬻ juggling club +10 (Agile, thrown 20 feet) __Damage__ 1d6+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ torch +10 (thrown 10 feet) __Damage__ 1d4+4 bludgeoning plus 1 fire"
abilities_bot:
  - name: "Juggle"
    desc: "⬻ (Concentrate, Manipulate) The juggler begins juggling up to three items of light or negligible Bulk. They can choose items in their hands or Interact to draw items on their person or pick up unattended items in reach. While juggling, they can Interact to add up to two items to their juggle, though they must drop an item for each one they add. The juggler is wielding all items they juggle, but the only actions they can take that require their hands are Return Throw, Juggling Bounce, Strike using a juggled weapon, Interact to add items to their juggle, or Dismiss to stop juggling. When the juggler Dismisses Juggle, they can choose to continue to wield, drop, or stow each juggled item, though they can't wield more items than they have hands. If at any point the juggler isn't wielding any items or becomes restrained or unconscious, the juggle ends and the juggler drops all the items."
  - name: "Juggling Bounce"
    desc: "⬻ The juggler Strikes with a thrown weapon they're juggling. If the Strike hits, the weapon bounces to a different creature in the weapon's first range increment. The juggler repeats the Strike, which uses the same multiple attack penalty and doesn't increase their multiple attack penalty. Juggling Props The weapons presented in the juggler stat block are examples, but other good options include starknives, hatchets, daggers, and even alchemical bombs. Practically any item of light Bulk can work. Jugglers are proficient in any ranged Strikes they make with thrown weapons. Higher level versions of this NPC might increase their maximum number of props to four or five."
sourcebook: "_NPC Core_, page 125."
```

```encounter-table
name: Juggler
creatures:
  - 1: Juggler
```
