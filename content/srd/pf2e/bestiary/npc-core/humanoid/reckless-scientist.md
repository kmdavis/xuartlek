---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Reckless Scientist"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Reckless Scientist"
level: 6
source: "NPC Core"
aon_id: "creature-3616"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3616"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Reckless Scientist"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Crafting +16, Deception +9, Engineering Lore +14, Medicine +10, Stealth +14, Underworld Lore +14"
abilityMods: [1, 4, 4, 4, 2, -1]
abilities_top:
  - name: "Unstable Collection"
    desc: "A reckless scientist carries a collection of poorly stowed alchemical items: 3 elixirs of life and 6 alchemical grenades. The scientist replenishes these items each day using scavenged materials. The alchemical grenades deal either acid, cold, or fire damage plus 2 persistent damage and 2 splash damage of the same type (typically the collection contains two of each grenade)."
  - name: "Items"
    desc: "Alchemist's Toolkit, _+1 sickle_, work coat (functions as leather armor)"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +16; __Ref__: +14; __Will__: +10 +1 status to all saves vs. poison"
hp: 95
health:
  - name: "HP"
    desc: "95; __Resistances__ poison 5"
abilities_mid:
  - name: "Unstable Explosion"
    desc: "When an attacker scores a critical hit against the reckless scientist, one of the scientist's alchemical items bursts. The GM determines the item randomly. If it was a bomb, the alchemist takes damage from the bomb, and any creature adjacent to the alchemist takes the splash damage. Any other item is wasted."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sickle +17 (Agile, Finesse, Magical, Trip) __Damage__ 1d4+7 slashing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ alchemical grenade +16 (range increment 20 feet, Splash) __Damage__ 2d6 acid, cold, or fire plus 2 persistent damage and 2 splash damage of the same type"
abilities_bot:
  - name: "Quick Grenadier"
    desc: "⬻ The reckless scientist Interacts to draw an alchemical grenade with an Interact action and throws it as a ranged Strike."
  - name: "Reckless Alchemy"
    desc: "⬺ (Concentrate, Manipulate) The reckless scientist attempts to combine two alchemical grenades or two elixirs of life into one item. They can Interact to draw the items if necessary. They attempt a DC 22 Crafting check, destroying both component items to create one new item."
  - name: "Success"
    desc: "The new item has the full effect of both component items, and the reckless scientist can Activate it. If they don't Activate it before the end of their turn, the item explodes (as critical failure)."
  - name: "Failure"
    desc: "The new item is inert."
  - name: "Critical Failure"
    desc: "The unstable item explodes, dealing 3d6 piercing damage to the reckless scientist"
sourcebook: "_NPC Core_, page 158."
```

```encounter-table
name: Reckless Scientist
creatures:
  - 1: Reckless Scientist
```
