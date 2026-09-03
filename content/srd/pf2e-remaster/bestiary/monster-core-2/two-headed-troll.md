---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Two-Headed Troll"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Two-Headed Troll"
level: 8
source: "Monster Core 2"
aon_id: "creature-4593"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4593"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Two-Headed Troll"
level: "Creature 8"
size: "Large"
trait_01: "Earth"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Troll"
trait_05: "Uncommon"
trait_06: "Wood"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +18, Intimidation +17"
abilityMods: [6, 1, 6, -2, 4, 3]
abilities_top:
  - name: "Easily Misled"
    desc: "The two-headed troll takes a –4 circumstance penalty to their Perception DC against Deception checks."
  - name: "Independent Brains"
    desc: "Each of a two-headed troll’s heads rolls their own initiative and has their own turn. Neither head can Delay. At the start of a head’s turn, that head gets 2 actions and 1 reaction. Each brain controls one arm, but both can move the legs. Any ability or item that would sever a two-headed troll’s head (such as a _vorpal_ weapon) doesn’t cause the two-headed troll to die if they still have their other head, but does cause them to lose the turns, actions, and reactions of the severed head. Mental effects that target a single creature affect only one of the troll’s heads."
  - name: "Items"
    desc: "Club"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +19; __Ref__: +15; __Will__: +14"
hp: 190
health:
  - name: "HP"
    desc: "190 , regeneration 20 (deactivated by electricity or fire); __Weaknesses__ electricity 10, fire 10"
abilities_mid:
  - name: "Head Regrowth"
    desc: "A two-headed troll's regeneration can regrow a severed head. After regaining Hit Points from regeneration, the two-headed troll attempts a DC 10 flat check. On a success, a missing head is fully restored. If a two-headed troll loses their last remaining head, they die immediately."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 (reach 10 feet) __Damage__ 2d12+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +18 (Agile, reach 10 feet) __Damage__ 2d8+8 slashing"
  - name: "Melee"
    desc: "⬻ club +18 (reach 10 feet) __Damage__ 2d6+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ club +13 (thrown 10 feet) __Damage__ 2d6+8 bludgeoning"
abilities_bot:
  - name: "Collaborative Chomp"
    desc: "⬺ The troll makes a claw Strike and Grabs a single target. If both are successful, the other head can use their reaction to make a jaws Strike against that creature. Severed Spiral Although most two-headed trolls have difficulty seeing past their confusion and rage, some have founded a nuanced faith emulating the dualistic gods Gozreh, Nethys, and Pharasma. The obscure philosophy seeks enlightenment at menhirs of black and white stones, most notably the Severed Spiral in Mendev."
sourcebook: "_Monster Core 2_, page 329."
```

```encounter-table
name: Two-Headed Troll
creatures:
  - 1: Two-Headed Troll
```
