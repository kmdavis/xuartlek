---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Artillerist"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Artillerist"
level: 3
source: "NPC Core"
aon_id: "creature-3459"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3459"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Artillerist"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; (10 if the artillerist is crewing a siege weapon)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Crafting +9, Diplomacy +9, Engineering Lore +11, Explosive Lore +9, Society +9, Thievery +8"
abilityMods: [3, 3, 1, 2, 1, 0]
abilities_top:
  - name: "Siege Acumen"
    desc: "The artillerist is permanently quickened. They can use this extra action only to Aim, Load, or Launch a siege weapon."
  - name: "Items"
    desc: "Artisan's Toolkit (siege weaponry), Dueling Pistol (20 rounds), Light Hammer, Repair Toolkit"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +12; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Siege Shield"
    desc: "While adjacent to a siege weapon, the artillerist gains a +1 circumstance bonus to AC."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light hammer +10 (Agile) __Damage__ 1d6+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dueling pistol +10 (Concealable, Concussive, fatal d10, range increment 60 feet, reload 1) __Damage__ 1d6+3 piercing"
  - name: "Ranged"
    desc: "⬻ light hammer +10 (Agile, thrown 20 feet) __Damage__ 1d6+5 bludgeoning"
abilities_bot:
  - name: "Bombard"
    desc: "⬺ (Manipulate) The artillerist activates a shoulder-mounted artillery piece to launch an explosive shell up to 120 feet away that explodes in 10-foot burst. Creatures within the burst take 2d6 piercing damage and 2d6 fire damage with a DC 19 basic Reflex save. A creature that fails its save is also knocked prone. The artillerist can't use Bombard again until they reload the artillery with 2 Interact actions; these actions don't have to be consecutive. Siege Weapons The artillerist is meant to pair with siege weapons, and engineers in general often pair well with these large instruments of war. Siege weapons usually work best with multiple NPCs crewing them. Rules for siege weapons can be found here."
sourcebook: "_NPC Core_, page 44."
```

```encounter-table
name: Artillerist
creatures:
  - 1: Artillerist
```
